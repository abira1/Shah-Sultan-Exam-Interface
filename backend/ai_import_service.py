"""
AI Import Service
Handles validation and creation of tracks from AI-extracted JSON
"""

from fastapi import APIRouter, HTTPException, Depends
from pydantic import BaseModel, validator, Field, ValidationError
from typing import List, Optional, Literal, Dict, Any
import uuid
from datetime import datetime
from motor.motor_asyncio import AsyncIOMotorDatabase
from difflib import get_close_matches

router = APIRouter()

# ============================================
# PYDANTIC MODELS
# ============================================

# Legacy type name mapping for backward compatibility
LEGACY_TYPE_MAPPING = {
    # ============ READING TYPE VARIATIONS ============
    # TRUE/FALSE/NOT GIVEN variations
    "true_false_not_given": "identifying_information_true_false_not_given",
    "yes_no_not_given": "identifying_information_true_false_not_given",
    "tfng": "identifying_information_true_false_not_given",
    "ynng": "identifying_information_true_false_not_given",
    "identifying_information": "identifying_information_true_false_not_given",
    "true_false": "identifying_information_true_false_not_given",
    "yes_no": "identifying_information_true_false_not_given",
    
    # Sentence completion variations
    "short_answer_reading": "sentence_completion_reading",
    "short_answer": "sentence_completion_reading",
    "sentence_completion": "sentence_completion_reading",
    "complete_sentences": "sentence_completion_reading",
    
    # Matching headings variations
    "matching_headings_reading": "matching_headings",
    "heading_matching": "matching_headings",
    "match_headings": "matching_headings",
    "paragraph_headings": "matching_headings",
    
    # Matching features variations
    "matching_features_reading": "matching_features",
    "feature_matching": "matching_features",
    "match_features": "matching_features",
    
    # Matching sentence endings variations
    "matching_sentence_endings_reading": "matching_sentence_endings",
    "sentence_endings": "matching_sentence_endings",
    "match_endings": "matching_sentence_endings",
    
    # Summary completion variations
    "summary_completion": "summary_completion_selecting_from_list",
    "summary_list": "summary_completion_selecting_from_list",
    "summary_from_list": "summary_completion_selecting_from_list",
    "summary_text": "summary_completion_selecting_words_from_text",
    "summary_from_text": "summary_completion_selecting_words_from_text",
    "summary_from_passage": "summary_completion_selecting_words_from_text",
    "sentence_completion_wordlist": "summary_completion_selecting_from_list",
    
    # Table completion variations
    "table_completion": "table_completion_reading",
    "complete_table": "table_completion_reading",
    "table_reading": "table_completion_reading",
    
    # Note completion variations
    "note_completion_reading": "note_completion",
    "complete_notes": "note_completion",
    "notes": "note_completion",
    
    # Flowchart variations
    "flowchart_completion": "flowchart_completion_selecting_words_from_text",
    "flowchart": "flowchart_completion_selecting_words_from_text",
    "flowchart_reading": "flowchart_completion_selecting_words_from_text",
    
    # Multiple choice variations
    "multiple_choice_reading": "multiple_choice_one_answer_reading",
    "mcq_reading": "multiple_choice_one_answer_reading",
    "multiple_choice_multiple_reading": "multiple_choice_more_than_one_answer_reading",
    "mcq_multiple_reading": "multiple_choice_more_than_one_answer_reading",
    
    # ============ LISTENING TYPE VARIATIONS ============
    # Fill in the gaps variations
    "fill_gaps": "fill_in_the_gaps",
    "fill_blank": "fill_in_the_gaps",
    "gap_fill": "fill_in_the_gaps",
    "short_answer_listening": "fill_in_the_gaps_short_answers",
    
    # Form completion variations
    "form": "form_completion",
    "complete_form": "form_completion",
    "form_filling": "form_completion",
    
    # Map labeling variations
    "labelling_map": "labelling_on_a_map",
    "map_labeling": "labelling_on_a_map",
    "label_map": "labelling_on_a_map",
    "map": "labelling_on_a_map",
    
    # Matching variations
    "matching": "matching_listening",
    "match_listening": "matching_listening",
    
    # Multiple choice variations
    "multiple_choice_listening": "multiple_choice_one_answer_listening",
    "mcq_listening": "multiple_choice_one_answer_listening",
    "multiple_choice_multiple_listening": "multiple_choice_more_than_one_answer_listening",
    
    # Sentence completion variations
    "sentence_completion_listening": "sentence_completion_listening",
    "complete_sentences_listening": "sentence_completion_listening",
    
    # Table completion variations
    "table_completion_listening": "table_completion_listening",
    "table_listening": "table_completion_listening",
    
    # Flowchart variations
    "flowchart_listening": "flowchart_completion_listening",
    "flowchart_completion_listen": "flowchart_completion_listening",
    
    # ============ WRITING TYPE VARIATIONS ============
    "writing_task_1": "writing_part_1",
    "writing_1": "writing_part_1",
    "task_1": "writing_part_1",
    "writing_task_2": "writing_part_2",
    "writing_2": "writing_part_2",
    "task_2": "writing_part_2",
    "writing_task": "writing_part_1",  # Default to part 1 if ambiguous
}

class QuestionImport(BaseModel):
    """Individual question in the import - ALL 24 QTI Question Types + Legacy Types"""
    index: int = Field(..., ge=1, description="Question number (1-40 for L/R, 1-2 for W)")
    type: str  # Changed from Literal to str to accept legacy types
    prompt: str = Field(..., min_length=1, description="Question text")
    answer_key: Optional[Any] = Field(None, description="Correct answer (string, list, or null for writing)")
    max_words: Optional[int] = Field(None, ge=1, le=10, description="Max words allowed")
    min_words: Optional[int] = Field(None, ge=50, le=500, description="Min words required (writing)")
    options: Optional[Any] = Field(None, description="Multiple choice options (array of dicts or strings)")
    wordlist: Optional[List[str]] = Field(None, description="Word bank for summary completion (legacy field name)")
    image_url: Optional[str] = Field(None, description="URL for map/diagram/flowchart images")
    word_list: Optional[List[str]] = Field(None, description="Word bank for summary completion")
    headings: Optional[List[Dict[str, str]]] = Field(None, description="Headings for matching [{value:'i', text:'...'}]")
    features: Optional[List[Dict[str, str]]] = Field(None, description="Features for matching [{value:'A', text:'...'}]")
    endings: Optional[List[Dict[str, str]]] = Field(None, description="Sentence endings [{value:'A', text:'...'}]")
    task_number: Optional[int] = Field(None, ge=1, le=2, description="Writing task number")
    chart_image: Optional[str] = Field(None, description="Chart image for writing task 1")
    instructions: Optional[str] = Field(None, description="Task instructions (writing)")
    table_data: Optional[Dict[str, Any]] = Field(None, description="Table structure for completion questions")
    form_fields: Optional[List[Dict[str, Any]]] = Field(None, description="Form fields for form_completion")
    max_choices: Optional[int] = Field(None, ge=2, le=5, description="Number of choices for multiple answer questions")

    @validator('type', pre=True)
    def normalize_question_type(cls, v):
        """Convert legacy type names to QTI standard names with smart normalization"""
        if not v:
            raise ValueError("Question type is required")
        
        # Normalize input: lowercase, strip, replace spaces/hyphens with underscores
        v_normalized = v.lower().strip().replace(' ', '_').replace('-', '_')
        
        # Check direct match in legacy mapping first
        if v_normalized in LEGACY_TYPE_MAPPING:
            return LEGACY_TYPE_MAPPING[v_normalized]
        
        # Check if already valid QTI type
        valid_types = {
            "fill_in_the_gaps",
            "fill_in_the_gaps_short_answers",
            "flowchart_completion_listening",
            "form_completion",
            "labelling_on_a_map",
            "matching_listening",
            "multiple_choice_more_than_one_answer_listening",
            "multiple_choice_one_answer_listening",
            "sentence_completion_listening",
            "table_completion_listening",
            "flowchart_completion_selecting_words_from_text",
            "identifying_information_true_false_not_given",
            "matching_features",
            "matching_headings",
            "matching_sentence_endings",
            "multiple_choice_more_than_one_answer_reading",
            "multiple_choice_one_answer_reading",
            "note_completion",
            "sentence_completion_reading",
            "summary_completion_selecting_from_list",
            "summary_completion_selecting_words_from_text",
            "table_completion_reading",
            "writing_part_1",
            "writing_part_2"
        }
        
        if v_normalized in valid_types:
            return v_normalized
        
        # If not found, provide helpful error with suggestions
        suggestions = get_close_matches(v_normalized, valid_types, n=3, cutoff=0.6)
        
        error_msg = f"Invalid question type: '{v}'."
        
        if suggestions:
            error_msg += f" Did you mean: {', '.join(suggestions)}?"
        else:
            # Show legacy mapping options if no close matches
            legacy_options = list(LEGACY_TYPE_MAPPING.keys())[:10]  # Show first 10 as examples
            error_msg += f" Example valid types: {', '.join(legacy_options)}..."
        
        error_msg += " See documentation for complete list of 24 supported question types."
        
        raise ValueError(error_msg)
    
    @validator('type')
    def validate_question_type_final(cls, v):
        """Final validation - should not fail if normalize_question_type worked correctly"""
        return v
    
    @validator('options', pre=True)
    def normalize_options(cls, v):
        """Auto-convert any option format to standard dict array"""
        if v is None:
            return None
        
        # Already correct format (list of dicts with value/text)
        if isinstance(v, list) and v and isinstance(v[0], dict) and 'value' in v[0]:
            return v
        
        # String array → Dict array (most common case)
        if isinstance(v, list) and v and isinstance(v[0], str):
            return [{"value": opt, "text": opt} for opt in v]
        
        # Single string → Dict array
        if isinstance(v, str):
            return [{"value": v, "text": v}]
        
        # Dict without proper structure → Try to fix
        if isinstance(v, list) and v and isinstance(v[0], dict):
            result = []
            for item in v:
                if 'value' in item and 'text' in item:
                    result.append(item)
                elif 'value' in item:
                    result.append({"value": item['value'], "text": str(item['value'])})
                elif len(item) >= 1:
                    # Take first key-value pair
                    key = list(item.keys())[0]
                    value = item[key]
                    result.append({"value": key, "text": str(value)})
            return result if result else None
        
        return v
    
    @validator('word_list')
    def merge_wordlist_fields(cls, v, values):
        """Merge legacy 'wordlist' field into 'word_list'"""
        # If word_list is None but wordlist exists, use wordlist
        if v is None and 'wordlist' in values and values['wordlist']:
            return values['wordlist']
        return v

    @validator('answer_key')
    def validate_answer_key(cls, v, values):
        """Answer key required for all types except writing types"""
        q_type = values.get('type')
        # Writing types don't need answer keys (manual grading)
        if q_type in ['writing_part_1', 'writing_part_2']:
            return None
        if not v:
            raise ValueError(f"answer_key is required for question type '{q_type}'")
        return v


class SectionImport(BaseModel):
    """Section with questions"""
    index: int = Field(..., ge=1, le=4, description="Section number")
    title: str = Field(..., min_length=1, description="Section title")
    instructions: str = Field(..., min_length=1, description="Section instructions")
    passage_text: Optional[str] = Field(None, description="Full passage text (reading only)")
    questions: List[QuestionImport] = Field(..., min_items=1, description="Questions in section")

    @validator('questions')
    def validate_questions_sequential(cls, v):
        """Ensure question indices are unique within section"""
        if not v:
            raise ValueError("Section must have at least one question")
        indices = [q.index for q in v]
        if len(indices) != len(set(indices)):
            raise ValueError("Duplicate question indices found in section")
        return v


class AIImportRequest(BaseModel):
    """Complete import request from AI"""
    test_type: Literal["listening", "reading", "writing"]
    title: str = Field(..., min_length=3, max_length=200)
    description: str = Field(..., min_length=10, max_length=1000)
    duration_seconds: int = Field(..., ge=60, le=7200, description="Test duration (1 min - 2 hours)")
    audio_url: Optional[str] = Field(None, description="Audio URL (required for listening)")
    sections: List[SectionImport] = Field(..., min_items=1, description="Test sections")

    @validator('sections')
    def validate_sections_by_type(cls, v, values):
        """Validate section count and question count by test type"""
        test_type = values.get('test_type')
        if not v:
            raise ValueError("Must have at least one section")
        
        # Validate section count
        section_count_rules = {
            "listening": 4,
            "reading": 3,
            "writing": 2
        }
        expected_sections = section_count_rules.get(test_type)
        if len(v) != expected_sections:
            raise ValueError(
                f"{test_type.title()} test must have exactly {expected_sections} sections (found {len(v)})"
            )
        
        # Validate total question count
        total_questions = sum(len(section.questions) for section in v)
        question_count_rules = {
            "listening": 40,
            "reading": 40,
            "writing": 2
        }
        expected_questions = question_count_rules.get(test_type)
        if total_questions != expected_questions:
            raise ValueError(
                f"{test_type.title()} test must have exactly {expected_questions} questions (found {total_questions})"
            )
        
        # Validate question indices are globally sequential (1 to N)
        all_indices = []
        for section in v:
            all_indices.extend([q.index for q in section.questions])
        all_indices.sort()
        expected_indices = list(range(1, len(all_indices) + 1))
        if all_indices != expected_indices:
            raise ValueError(
                f"Question indices must be sequential from 1 to {len(all_indices)}. Found: {all_indices}"
            )
        
        # Validate reading tests have passage_text
        if test_type == "reading":
            for i, section in enumerate(v, 1):
                if not section.passage_text or len(section.passage_text) < 100:
                    raise ValueError(
                        f"Reading test Section {i} must have passage_text (at least 100 characters)"
                    )
        
        return v

    @validator('audio_url')
    def validate_audio_url_for_listening(cls, v, values):
        """Audio URL required for listening tests"""
        test_type = values.get('test_type')
        if test_type == "listening" and not v:
            raise ValueError("Listening test requires audio_url")
        return v

    @validator('duration_seconds')
    def validate_duration_by_type(cls, v, values):
        """Validate duration is reasonable for test type"""
        test_type = values.get('test_type')
        duration_rules = {
            "listening": (1500, 2400),
            "reading": (3000, 4200),
            "writing": (3000, 4200)
        }
        if test_type in duration_rules:
            min_dur, max_dur = duration_rules[test_type]
            if not (min_dur <= v <= max_dur):
                raise ValueError(
                    f"{test_type.title()} test duration should be between "
                    f"{min_dur//60}-{max_dur//60} minutes (got {v//60} minutes)"
                )
        return v


class TrackCreateResponse(BaseModel):
    """Response after successful track creation"""
    success: bool
    track_id: str
    exam_id: str
    questions_created: int
    sections_created: int
    message: str


class ValidationResponse(BaseModel):
    """Response for validation-only request"""
    valid: bool
    test_type: Optional[str] = None
    title: Optional[str] = None
    total_questions: Optional[int] = None
    total_sections: Optional[int] = None
    duration_minutes: Optional[int] = None
    has_audio: Optional[bool] = None
    section_breakdown: Optional[List[Dict[str, Any]]] = None
    errors: Optional[List[str]] = None


# ============================================
# HELPER FUNCTIONS
# ============================================

def get_database() -> AsyncIOMotorDatabase:
    """Get database instance from server.py"""
    from server import db
    return db


async def create_exam_from_import(db: AsyncIOMotorDatabase, import_data: AIImportRequest) -> str:
    """Create exam document in database"""
    exam_id = f"ielts-{import_data.test_type}-{uuid.uuid4().hex[:8]}"
    
    exam_data = {
        "_id": exam_id,
        "id": exam_id,
        "title": import_data.title,
        "description": import_data.description,
        "exam_type": import_data.test_type,
        "audio_url": import_data.audio_url,
        "audio_source_method": "url" if import_data.audio_url else None,
        "loop_audio": False,
        "duration_seconds": import_data.duration_seconds,
        "published": True,
        "is_active": False,
        "started_at": None,
        "stopped_at": None,
        "question_count": sum(len(s.questions) for s in import_data.sections),
        "submission_count": 0,
        "created_at": datetime.utcnow().isoformat() + "Z",
        "updated_at": datetime.utcnow().isoformat() + "Z",
        "is_demo": False
    }
    
    await db.exams.replace_one({"_id": exam_id}, exam_data, upsert=True)
    return exam_id


async def create_sections_from_import(
    db: AsyncIOMotorDatabase,
    exam_id: str,
    sections: List[SectionImport]
) -> List[str]:
    """Create section documents in database"""
    section_ids = []
    
    for section in sections:
        section_id = f"{exam_id}-section-{section.index}"
        section_data = {
            "_id": section_id,
            "id": section_id,
            "exam_id": exam_id,
            "index": section.index,
            "title": section.title,
            "instructions": section.instructions
        }
        
        # Add passage_text for reading tests
        if section.passage_text:
            section_data["passage_text"] = section.passage_text
        
        await db.sections.replace_one({"_id": section_id}, section_data, upsert=True)
        section_ids.append(section_id)
    
    return section_ids


async def create_questions_from_import(
    db: AsyncIOMotorDatabase,
    exam_id: str,
    sections: List[SectionImport]
) -> int:
    """Create question documents in database"""
    questions_created = 0
    
    for section in sections:
        section_id = f"{exam_id}-section-{section.index}"
        
        for question in section.questions:
            question_id = f"{exam_id}-q{question.index}"
            
            # Build payload
            payload = {
                "prompt": question.prompt,
                "answer_key": question.answer_key
            }
            
            # Add optional fields if present
            if question.max_words is not None:
                payload["max_words"] = question.max_words
            if question.min_words is not None:
                payload["min_words"] = question.min_words
            if question.options:
                payload["options"] = question.options
            if question.image_url:
                payload["image_url"] = question.image_url
            if question.wordlist:
                payload["wordlist"] = question.wordlist
            if question.task_number is not None:
                payload["task_number"] = question.task_number
            if question.chart_image:
                payload["chart_image"] = question.chart_image
            if question.instructions:
                payload["instructions"] = question.instructions
            
            question_data = {
                "_id": question_id,
                "id": question_id,
                "section_id": section_id,
                "exam_id": exam_id,
                "index": question.index,
                "type": question.type,
                "payload": payload,
                "marks": 1,
                "created_by": "admin",
                "is_demo": False
            }
            
            await db.questions.replace_one({"_id": question_id}, question_data, upsert=True)
            questions_created += 1
    
    return questions_created


async def create_track_record(
    db: AsyncIOMotorDatabase,
    import_data: AIImportRequest,
    exam_id: str,
    admin_email: str = "admin@example.com"
) -> str:
    """Create track document in database"""
    track_id = str(uuid.uuid4())
    
    track_data = {
        "_id": track_id,
        "id": track_id,
        "track_type": import_data.test_type,
        "title": import_data.title,
        "description": import_data.description,
        "exam_id": exam_id,
        "created_by": admin_email,
        "created_at": datetime.utcnow().isoformat() + "Z",
        "updated_at": datetime.utcnow().isoformat() + "Z",
        "status": "published",
        "version": 1,
        "metadata": {
            "question_count": sum(len(s.questions) for s in import_data.sections),
            "duration_seconds": import_data.duration_seconds,
            "has_audio": import_data.audio_url is not None,
            "audio_url": import_data.audio_url,
            "sections_count": len(import_data.sections),
            "total_submissions": 0,
            "average_score": None
        },
        "tags": [],
        "source": "ai_import"
    }
    
    await db.tracks.replace_one({"_id": track_id}, track_data, upsert=True)
    return track_id


# ============================================
# API ENDPOINTS
# ============================================

@router.post("/api/tracks/validate-import", response_model=ValidationResponse)
async def validate_import(import_data: AIImportRequest):
    """
    Validate AI-generated JSON without creating anything
    Returns validation summary with section breakdown
    """
    # Build section breakdown
    section_breakdown = []
    for section in import_data.sections:
        # Count question types
        question_types = {}
        for q in section.questions:
            question_types[q.type] = question_types.get(q.type, 0) + 1
        
        section_breakdown.append({
            "section_number": section.index,
            "title": section.title,
            "question_count": len(section.questions),
            "question_types": question_types,
            "has_passage": section.passage_text is not None and len(section.passage_text) > 0
        })
    
    return ValidationResponse(
        valid=True,
        test_type=import_data.test_type,
        title=import_data.title,
        total_questions=sum(len(s.questions) for s in import_data.sections),
        total_sections=len(import_data.sections),
        duration_minutes=import_data.duration_seconds // 60,
        has_audio=import_data.audio_url is not None,
        section_breakdown=section_breakdown
    )


@router.post("/api/tracks/import-from-ai", response_model=TrackCreateResponse)
async def import_track_from_ai(import_data: AIImportRequest, db: AsyncIOMotorDatabase = Depends(get_database)):
    """
    Create track from AI-generated JSON
    Steps:
    1. Validate JSON structure (Pydantic)
    2. Create exam document
    3. Create section documents
    4. Create question documents
    5. Create track record
    6. Return success response
    """
    try:
        # Step 1: Create exam
        exam_id = await create_exam_from_import(db, import_data)
        
        # Step 2: Create sections
        section_ids = await create_sections_from_import(db, exam_id, import_data.sections)
        
        # Step 3: Create questions
        questions_created = await create_questions_from_import(db, exam_id, import_data.sections)
        
        # Step 4: Create track record
        track_id = await create_track_record(db, import_data, exam_id)
        
        # Step 5: Return success
        return TrackCreateResponse(
            success=True,
            track_id=track_id,
            exam_id=exam_id,
            questions_created=questions_created,
            sections_created=len(section_ids),
            message=f"Track '{import_data.title}' created successfully with {questions_created} questions"
        )
        
    except Exception as e:
        raise HTTPException(status_code=400, detail=f"Failed to create track: {str(e)}")


@router.post("/api/tracks/from-exam/{exam_id}")
async def convert_exam_to_track(exam_id: str, db: AsyncIOMotorDatabase = Depends(get_database)):
    """
    Convert existing exam to track
    Useful for converting the 3 existing tests to tracks if needed
    """
    try:
        # Get exam
        exam = await db.exams.find_one({"id": exam_id})
        if not exam:
            raise HTTPException(status_code=404, detail="Exam not found")
        
        # Check if track already exists for this exam
        existing_track = await db.tracks.find_one({"exam_id": exam_id})
        if existing_track:
            return {
                "success": True,
                "track_id": existing_track["_id"],
                "message": "Track already exists for this exam"
            }
        
        # Create track
        track_id = str(uuid.uuid4())
        track_data = {
            "_id": track_id,
            "id": track_id,
            "track_type": exam.get("exam_type", "listening"),
            "title": exam["title"],
            "description": exam["description"],
            "exam_id": exam_id,
            "created_by": "admin@example.com",
            "created_at": datetime.utcnow().isoformat() + "Z",
            "updated_at": datetime.utcnow().isoformat() + "Z",
            "status": "published",
            "version": 1,
            "metadata": {
                "question_count": exam.get("question_count", 0),
                "duration_seconds": exam.get("duration_seconds", 0),
                "has_audio": exam.get("audio_url") is not None,
                "audio_url": exam.get("audio_url"),
                "sections_count": await db.sections.count_documents({"exam_id": exam_id}),
                "total_submissions": exam.get("submission_count", 0),
                "average_score": None
            },
            "tags": ["official"],
            "source": "converted"
        }
        
        await db.tracks.replace_one({"_id": track_id}, track_data, upsert=True)
        
        return {
            "success": True,
            "track_id": track_id,
            "exam_id": exam_id,
            "message": f"Exam '{exam['title']}' converted to track successfully"
        }
        
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))


# Export router
def get_router():
    return router