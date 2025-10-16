# Backend Validation Reference - Complete Analysis

**Phase 1 - System Audit & Mapping**  
**File:** `/app/backend/ai_import_service.py`  
**Status:** Comprehensive validation analysis complete

---

## Table of Contents
1. [Overview](#overview)
2. [Validation Architecture](#validation-architecture)
3. [Question Type Validation](#question-type-validation)
4. [Field Requirements by Type](#field-requirements-by-type)
5. [Auto-Grading Logic](#auto-grading-logic)
6. [Legacy Type Support](#legacy-type-support)
7. [Error Handling](#error-handling)

---

## Overview

The backend validation system in `ai_import_service.py` provides comprehensive validation for all 24 QTI question types plus legacy type mapping. It uses Pydantic models for automatic validation and includes smart auto-normalization.

### Key Features
- ✅ **24 QTI Types:** All question types supported
- ✅ **Legacy Mapping:** Backward compatibility with 15+ legacy names
- ✅ **Auto-normalization:** Converts formats automatically
- ✅ **Smart Validation:** Detailed error messages with suggestions
- ✅ **Field Validation:** Type-specific required/optional fields

---

## Validation Architecture

### Pydantic Model Structure
```python
class QuestionImport(BaseModel):
    """Individual question validation model"""
    # Core fields (all types)
    index: int = Field(..., ge=1)
    type: str  # Accepts both QTI and legacy names
    prompt: str = Field(..., min_length=1)
    answer_key: Optional[Any] = None
    
    # Type-specific fields
    max_words: Optional[int] = Field(None, ge=1, le=10)
    min_words: Optional[int] = Field(None, ge=50, le=500)
    options: Optional[Any] = None
    word_list: Optional[List[str]] = None
    headings: Optional[List[Dict[str, str]]] = None
    # ... [20+ more type-specific fields]
```

### Validation Flow
1. **Pre-validation:** Normalize type names (legacy → QTI)
2. **Type validation:** Ensure type is in valid_types set
3. **Field validation:** Check required/optional fields per type
4. **Format validation:** Auto-normalize options, word lists, etc.
5. **Answer key validation:** Ensure present for non-writing types
6. **Cross-validation:** Check consistency between fields

---

## Question Type Validation

### Valid QTI Types (24 Total)

#### Listening Types (10)
```python
# LISTENING QUESTION TYPES
"fill_in_the_gaps"                              # Single blank, short answer
"fill_in_the_gaps_short_answers"                # Multiple blanks in passage  
"flowchart_completion_listening"                # Complete flowchart from audio
"form_completion"                               # Fill in form fields
"labelling_on_a_map"                           # Label locations on map
"matching_listening"                           # Match items from audio
"multiple_choice_more_than_one_answer_listening" # Choose 2+ answers
"multiple_choice_one_answer_listening"          # Choose 1 answer
"sentence_completion_listening"                 # Complete sentences from audio
"table_completion_listening"                    # Fill in table cells
```

#### Reading Types (12)
```python
# READING QUESTION TYPES  
"flowchart_completion_selecting_words_from_text"  # Complete flowchart with words
"identifying_information_true_false_not_given"    # TRUE/FALSE/NOT GIVEN
"matching_features"                               # Match features to descriptions
"matching_headings"                               # Match paragraph headings
"matching_sentence_endings"                       # Complete sentences by matching
"multiple_choice_more_than_one_answer_reading"    # Choose 2+ answers
"multiple_choice_one_answer_reading"              # Choose 1 answer
"note_completion"                                 # Complete notes/summary
"sentence_completion_reading"                     # Complete sentences from passage
"summary_completion_selecting_from_list"         # Complete summary from word list
"summary_completion_selecting_words_from_text"   # Complete summary from passage
"table_completion_reading"                        # Fill in table from passage
```

#### Writing Types (2)
```python
# WRITING QUESTION TYPES
"writing_part_1"                                # Chart/diagram description (150+ words)
"writing_part_2"                                # Essay writing (250+ words)
```

### Type Validation Logic
```python
@validator('type')
def validate_question_type(cls, v):
    """Ensure type is valid after normalization"""
    valid_types = {
        # [all 24 types listed above]
    }
    if v not in valid_types:
        raise ValueError(f"Invalid question type: '{v}'. Valid types: {list(valid_types)}")
    return v
```

---

## Field Requirements by Type

### Universal Fields (All Types)
```python
# Required for ALL question types
index: int          # Question number (sequential)
type: str           # Valid QTI type name
prompt: str         # Question text/prompt
```

### Answer Key Requirements
```python
# Required for ALL EXCEPT writing types
answer_key: Any     # Correct answer (string, list, null for writing)

# Writing types ONLY
answer_key: null    # Always null for writing_part_1 and writing_part_2
```

### Type-Specific Field Map

#### Fill in the Gaps Types
```python
# fill_in_the_gaps, fill_in_the_gaps_short_answers
REQUIRED: index, type, prompt, answer_key
OPTIONAL: max_words (default: 3, range: 1-10)
ANSWER_FORMAT: string (single) or list (multiple)
```

#### Multiple Choice Types  
```python
# multiple_choice_one_answer_*, multiple_choice_more_than_one_answer_*
REQUIRED: index, type, prompt, answer_key, options
OPTIONAL: max_choices (for "more than one" types)
OPTIONS_FORMAT: [{"value": "A", "text": "Option text"}, ...]
ANSWER_FORMAT: "A" (single) or ["A", "B"] (multiple)
```

#### TRUE/FALSE/NOT GIVEN
```python
# identifying_information_true_false_not_given
REQUIRED: index, type, prompt, answer_key, options
OPTIONS_FORMAT: [
  {"value": "TRUE", "text": "TRUE"},
  {"value": "FALSE", "text": "FALSE"}, 
  {"value": "NOT GIVEN", "text": "NOT GIVEN"}
]
ANSWER_FORMAT: "TRUE" | "FALSE" | "NOT GIVEN"
```

#### Matching Types
```python
# matching_headings
REQUIRED: index, type, prompt, answer_key, headings
HEADINGS_FORMAT: [{"value": "i", "text": "Heading text"}, ...]
ANSWER_FORMAT: "i" | "ii" | "iii" | etc.

# matching_features  
REQUIRED: index, type, prompt, answer_key, features
FEATURES_FORMAT: [{"value": "A", "text": "Feature text"}, ...]
ANSWER_FORMAT: "A" | "B" | "C" | etc.

# matching_sentence_endings
REQUIRED: index, type, prompt, answer_key, endings
ENDINGS_FORMAT: [{"value": "A", "text": "Ending text"}, ...]
ANSWER_FORMAT: "A" | "B" | "C" | etc.
```

#### Summary Completion Types
```python
# summary_completion_selecting_from_list
REQUIRED: index, type, prompt, answer_key, word_list
WORD_LIST_FORMAT: ["word1", "word2", "word3", ...]
ANSWER_FORMAT: "word1" (from list)

# summary_completion_selecting_words_from_text
REQUIRED: index, type, prompt, answer_key  
OPTIONAL: max_words (default: 3)
ANSWER_FORMAT: "text from passage"
```

#### Completion Types (Sentence, Table, Note, Form, Flowchart)
```python
# sentence_completion_*, table_completion_*, note_completion, form_completion, flowchart_completion_*
REQUIRED: index, type, prompt, answer_key
OPTIONAL: max_words (default: 3, range: 1-10)
OPTIONAL: table_data (for table types), form_fields (for form), image_url (for flowchart/map)
ANSWER_FORMAT: string or list (depending on question structure)
```

#### Map/Image Types
```python
# labelling_on_a_map, flowchart_completion_listening
REQUIRED: index, type, prompt, answer_key
OPTIONAL: image_url (map/flowchart image)
ANSWER_FORMAT: string (location/label name)
```

#### Writing Types
```python  
# writing_part_1
REQUIRED: index, type, prompt, min_words (150+)
OPTIONAL: chart_image, instructions, task_number
ANSWER_KEY: null (no auto-grading)

# writing_part_2
REQUIRED: index, type, prompt, min_words (250+)
OPTIONAL: instructions, task_number
ANSWER_KEY: null (no auto-grading)
```

---

## Auto-Grading Logic

### Grading Methods by Type

#### Exact Match (Case-Insensitive)
```python
# Used for: fill_in_the_gaps, sentence_completion_*, note_completion
def grade_exact_match(student_answer, correct_answer):
    return student_answer.lower().strip() == correct_answer.lower().strip()
```

#### Multiple Choice Exact Match
```python
# Used for: multiple_choice_*, true_false_not_given, matching_*
def grade_multiple_choice(student_answer, correct_answer):
    return student_answer == correct_answer  # Case-sensitive for option values
```

#### List Matching
```python
# Used for: fill_in_the_gaps_short_answers, multiple_choice_more_than_one_answer_*
def grade_list_match(student_answers, correct_answers):
    return set(student_answers) == set(correct_answers)
```

#### Word Limit Validation  
```python
# Used for: summary_completion_*, sentence_completion_*
def validate_word_limit(answer, max_words):
    word_count = len(answer.split())
    return word_count <= max_words
```

#### No Auto-Grading
```python
# Used for: writing_part_1, writing_part_2
# These require manual grading by admin
# System stores answers but doesn't calculate scores
```

---

## Legacy Type Support

### Comprehensive Legacy Mapping
```python
LEGACY_TYPE_MAPPING = {
    # TRUE/FALSE/NOT GIVEN variations
    "true_false_not_given": "identifying_information_true_false_not_given",
    "yes_no_not_given": "identifying_information_true_false_not_given", 
    "tfng": "identifying_information_true_false_not_given",
    "ynng": "identifying_information_true_false_not_given",
    
    # Reading completion variations
    "short_answer_reading": "sentence_completion_reading",
    "sentence_completion_wordlist": "summary_completion_selecting_from_list",
    "summary_completion": "summary_completion_selecting_from_list",
    "table_completion": "table_completion_reading",
    "note_completion_reading": "note_completion",
    "flowchart_completion": "flowchart_completion_selecting_words_from_text",
    
    # Reading matching variations
    "matching_headings_reading": "matching_headings",
    "matching_features_reading": "matching_features", 
    "matching_sentence_endings_reading": "matching_sentence_endings",
    
    # Listening variations
    "short_answer": "fill_in_the_gaps_short_answers",
    "multiple_choice_listening": "multiple_choice_one_answer_listening",
    "sentence_completion": "sentence_completion_listening",
    "map_labeling": "labelling_on_a_map",
    "diagram_labeling": "labelling_on_a_map"  # Maps to same component
}
```

### Legacy Normalization Process
```python
@validator('type', pre=True)
def normalize_question_type(cls, v):
    """Convert legacy type names to QTI standard names"""
    if v in LEGACY_TYPE_MAPPING:
        return LEGACY_TYPE_MAPPING[v]
    return v
```

---

## Error Handling

### Validation Error Types

#### 1. Invalid Question Type
```json
{
  "error": "Invalid question type: 'true_false'",
  "suggestion": "Did you mean: 'identifying_information_true_false_not_given'?",
  "help": "See documentation for complete list of valid types"
}
```

#### 2. Missing Required Fields
```json
{
  "error": "Field 'answer_key' is required for type 'sentence_completion_reading'", 
  "field": "sections.0.questions.2.answer_key",
  "type": "sentence_completion_reading"
}
```

#### 3. Invalid Field Values
```json
{
  "error": "Field 'max_words' must be between 1 and 10",
  "field": "sections.0.questions.5.max_words",
  "value": 15,
  "valid_range": "1-10"
}
```

#### 4. Format Validation Errors
```json
{
  "error": "Field 'options' must be array of objects with 'value' and 'text'",
  "field": "sections.0.questions.8.options", 
  "received": ["A", "B", "C"],
  "expected": [{"value": "A", "text": "..."}, ...]
}
```

### Auto-Normalization Features

#### Options Format Auto-Fix
```python
# Input: ["A", "B", "C"] (string array)
# Auto-converted to: [{"value": "A", "text": "A"}, {"value": "B", "text": "B"}, ...]

@validator('options', pre=True)
def normalize_options(cls, v):
    if isinstance(v, list) and v and isinstance(v[0], str):
        return [{"value": opt, "text": opt} for opt in v]
    return v
```

#### Word List Merging
```python
# Handles both 'word_list' and legacy 'wordlist' field names
@validator('word_list')
def merge_wordlist_fields(cls, v, values):
    if v is None and 'wordlist' in values:
        return values['wordlist']
    return v
```

---

## Validation Endpoints

### 1. Validate Import (Preview)
```bash
POST /api/tracks/validate-detailed
```
**Purpose:** Validate JSON without creating anything  
**Returns:** Validation status, statistics, warnings, normalized data

### 2. Import from AI
```bash
POST /api/tracks/import-from-ai  
```
**Purpose:** Validate and create track/exam from JSON  
**Returns:** Created IDs, statistics, success confirmation

### Usage Example
```bash
# Validate before import
curl -X POST http://localhost:8001/api/tracks/validate-detailed \
  -H "Content-Type: application/json" \
  -d @your_test.json

# Import if validation passes
curl -X POST http://localhost:8001/api/tracks/import-from-ai \
  -H "Content-Type: application/json" \  
  -d @your_test.json
```

---

## Summary

### ✅ Backend Validation Strengths
- **Complete type coverage:** All 24 QTI types supported
- **Legacy compatibility:** 15+ legacy type mappings
- **Smart normalization:** Auto-fixes common format issues
- **Detailed validation:** Field-by-field validation with helpful errors
- **Preview capability:** Validate without creating via `/validate-detailed`
- **Comprehensive grading:** Type-appropriate grading logic for all question types

### 🔧 Validation Features
- **Type normalization:** Automatic legacy → QTI conversion
- **Field validation:** Required/optional field checking per type
- **Format auto-fix:** Options, word lists, answer keys auto-normalized
- **Answer key validation:** Ensures present for gradable types
- **Sequential indexing:** Validates question numbering
- **Cross-validation:** Checks field consistency

### 📊 Status: ✅ 100% Complete
The backend validation system is comprehensive and production-ready, supporting all current and future question import needs with robust error handling and auto-normalization capabilities.