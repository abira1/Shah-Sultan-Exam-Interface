# 🎯 COMPLETE PRODUCTION-READY PLAN: 24 QTI Question Types System

**Document Version:** 1.0  
**Created:** January 2025  
**Status:** Ready for Execution  
**Total Estimated Time:** 23-30 hours (3-4 days)

---

## 📋 EXECUTIVE SUMMARY

### System Overview
This plan creates a complete IELTS question management system where:
1. **DeepSeek AI** reads IELTS question PDFs
2. **Generates perfect JSON** using provided prompts
3. **Backend validates & imports** all questions automatically  
4. **Frontend renders** using existing QTI components
5. **Students take tests** with identical IELTS interface

### Scope
- **24 QTI Question Types:** 10 Listening + 12 Reading + 2 Writing
- **AI Integration:** DeepSeek prompt templates for PDF conversion
- **Complete Validation:** Backend accepts all format variations
- **Full Documentation:** User guides, API reference, templates
- **Production Ready:** Tested, validated, deployable

---

## 🗺️ PHASE OVERVIEW

| Phase | Name | Time | Priority | Status |
|-------|------|------|----------|--------|
| **Phase 1** | System Audit & Mapping | 2-3 hours | Critical | ⏳ Pending |
| **Phase 2** | AI-Ready JSON Templates | 3-4 hours | Critical | ⏳ Pending |
| **Phase 3** | DeepSeek AI Prompts | 2 hours | Critical | ⏳ Pending |
| **Phase 4** | Backend Validation Fix | 3-4 hours | Critical | ⏳ Pending |
| **Phase 5** | Frontend Integration | 4-5 hours | High | ⏳ Pending |
| **Phase 6** | Documentation | 3-4 hours | High | ⏳ Pending |
| **Phase 7** | Testing & Validation | 4-5 hours | High | ⏳ Pending |
| **Phase 8** | Production Deployment | 2 hours | Medium | ⏳ Pending |

---

# 📍 PHASE 1: SYSTEM AUDIT & MAPPING

**Duration:** 2-3 hours  
**Priority:** Critical  
**Dependencies:** None

## Objectives
- Map all 24 QTI question types through the entire system
- Identify backend ↔ frontend ↔ component mappings
- Verify all components exist and work
- Document gaps and mismatches

## Tasks

### Task 1.1: Create Master Question Type Reference Table

**Action:** Create comprehensive mapping document

**Deliverable:** `/app/docs/QUESTION_TYPE_MASTER_REFERENCE.md`

**Content Structure:**
```markdown
| # | Question Type Name | Category | Backend Type | QTI Component | File Path | Status | Notes |
|---|-------------------|----------|--------------|---------------|-----------|--------|-------|
| 1 | Fill in the Gaps | Listening | fill_in_the_gaps | FillInTheGaps | /qti/listening/FillInTheGaps.jsx | ✅ Working | Short answer blanks |
| 2 | Fill in Gaps Short | Listening | fill_in_the_gaps_short_answers | FillInTheGapsShortAnswers | /qti/listening/FillInTheGapsShortAnswers.jsx | ✅ Working | Multiple blanks |
| ... | ... | ... | ... | ... | ... | ... | ... |
```

**Table Columns:**
1. **#** - Sequential number (1-24)
2. **Question Type Name** - Human-readable name
3. **Category** - Listening/Reading/Writing
4. **Backend Type** - Exact string used in backend validation
5. **QTI Component** - React component name
6. **File Path** - Location of component file
7. **Status** - ✅ Working / ⚠️ Issues / ❌ Missing
8. **Notes** - Additional information

### Task 1.2: Verify QTI Component Coverage

**Action:** Check all component files exist and are properly integrated

**Listening Components (10):**
```bash
# Check existence
ls -la /app/frontend/src/components/qti/listening/

Expected files:
- FillInTheGaps.jsx
- FillInTheGapsShortAnswers.jsx
- FlowchartCompletionListening.jsx
- FormCompletion.jsx
- LabellingOnAMap.jsx
- MatchingListening.jsx
- MultipleChoiceMoreThanOneAnswerListening.jsx
- MultipleChoiceOneAnswerListening.jsx
- SentenceCompletionListening.jsx
- TableCompletionListening.jsx
```

**Reading Components (12):** ✅ Already verified in previous task
```bash
ls -la /app/frontend/src/components/qti/reading/

Expected files:
- FlowchartCompletionSelectingWordsFromText.jsx
- IdentifyingInformationTrueFalseNotGiven.jsx
- MatchingFeatures.jsx
- MatchingHeadings.jsx
- MatchingSentenceEndings.jsx
- MultipleChoiceMoreThanOneAnswerReading.jsx
- MultipleChoiceOneAnswerReading.jsx
- NoteCompletion.jsx
- SentenceCompletionReading.jsx
- SummaryCompletionSelectingFromList.jsx
- SummaryCompletionSelectingWordsFromText.jsx
- TableCompletionReading.jsx
```

**Writing Components (2):** ✅ Already verified in previous task
```bash
ls -la /app/frontend/src/components/qti/writing/

Expected files:
- WritingPart1.jsx
- WritingPart2.jsx
```

**Deliverable:** Component inventory report with missing files list

### Task 1.3: Analyze Backend Question Validation

**Action:** Review and document backend validation logic

**Files to Check:**
1. `/app/backend/ai_import_service.py` - AI import validation
2. `/app/backend/server.py` - Question creation endpoints
3. `/app/backend/models/` - Database models (if separate)

**Document:**
- Accepted type names (current list)
- Required fields per type
- Optional fields per type
- Validation rules
- Auto-grading logic

**Deliverable:** `/app/docs/BACKEND_VALIDATION_REFERENCE.md`

### Task 1.4: Analyze Frontend Rendering Flow

**Action:** Review how questions are rendered in test interfaces

**Files to Check:**
1. `/app/frontend/src/components/ListeningTest.jsx`
2. `/app/frontend/src/components/ReadingTest.jsx` 
3. `/app/frontend/src/components/WritingTest.jsx`

**Check:**
- `renderQuestion()` or `renderQuestionComponent()` switch statements
- Which types are integrated vs missing
- Import statements for QTI components
- Handler functions (onAnswerChange, onFocus)

**Deliverable:** Frontend integration status report

### Task 1.5: Check Admin Question Creation UI

**Action:** Review admin panel question creation interface

**Files to Check:**
1. `/app/frontend/src/components/admin/QuestionManager.jsx`
2. `/app/frontend/src/components/admin/TestManagement.jsx`

**Document:**
- Current question creation flow
- Type selection mechanism
- Payload structure generation
- Validation before save

**Deliverable:** Admin UI capabilities report

## Phase 1 Success Criteria
- ✅ Master reference table complete with all 24 types
- ✅ All component files verified (exist or marked as missing)
- ✅ Backend validation documented
- ✅ Frontend rendering flow mapped
- ✅ Admin UI capabilities assessed
- ✅ Gaps and issues list created

## Phase 1 Outputs
1. `QUESTION_TYPE_MASTER_REFERENCE.md`
2. `BACKEND_VALIDATION_REFERENCE.md`
3. `COMPONENT_INVENTORY_REPORT.md`
4. `FRONTEND_INTEGRATION_STATUS.md`
5. `ADMIN_UI_CAPABILITIES_REPORT.md`
6. `GAPS_AND_ISSUES.md`

---

# 📍 PHASE 2: AI-READY JSON TEMPLATES

**Duration:** 3-4 hours  
**Priority:** Critical  
**Dependencies:** Phase 1 complete

## Objectives
- Create validated JSON templates for all 24 question types
- Ensure templates work with DeepSeek AI output
- Provide complete test examples
- Include inline documentation

## Tasks

### Task 2.1: Design Standard JSON Structure

**Action:** Define the universal JSON format for test imports

**Standard Structure:**
```json
{
  "test_type": "listening|reading|writing",
  "title": "Test Title (3-200 characters)",
  "description": "Test Description (10-1000 characters)",
  "duration_seconds": 3600,
  "audio_url": "https://..." (required for listening, null otherwise),
  "sections": [
    {
      "index": 1,
      "title": "Section 1: Title",
      "instructions": "Questions 1-10",
      "passage_text": "Full passage text" (required for reading, null otherwise),
      "questions": [
        {
          "index": 1,
          "type": "question_type_name",
          "prompt": "Question text",
          "answer_key": "correct_answer",
          "// ... type-specific fields"
        }
      ]
    }
  ]
}
```

**Validation Rules:**
- `test_type`: Must be "listening", "reading", or "writing"
- `duration_seconds`: 60-7200 (1 min - 2 hours)
- `sections`: 1-4 sections
- `questions`: Sequential indices, no duplicates
- `audio_url`: Required for listening, must be valid URL
- `passage_text`: Required for reading, 100+ characters

**Deliverable:** `/app/docs/JSON_STRUCTURE_STANDARD.md`

### Task 2.2: Create Individual Question Templates

**Action:** Create 24 separate JSON files, one per question type

**Directory Structure:**
```
/app/templates/question_types/
├── README.md
├── listening/
│   ├── 01_fill_in_the_gaps.json
│   ├── 02_fill_in_the_gaps_short_answers.json
│   ├── 03_flowchart_completion_listening.json
│   ├── 04_form_completion.json
│   ├── 05_labelling_on_a_map.json
│   ├── 06_matching_listening.json
│   ├── 07_multiple_choice_more_than_one_answer_listening.json
│   ├── 08_multiple_choice_one_answer_listening.json
│   ├── 09_sentence_completion_listening.json
│   └── 10_table_completion_listening.json
├── reading/
│   ├── 01_flowchart_completion_selecting_words_from_text.json
│   ├── 02_identifying_information_true_false_not_given.json
│   ├── 03_matching_features.json
│   ├── 04_matching_headings.json
│   ├── 05_matching_sentence_endings.json
│   ├── 06_multiple_choice_more_than_one_answer_reading.json
│   ├── 07_multiple_choice_one_answer_reading.json
│   ├── 08_note_completion.json
│   ├── 09_sentence_completion_reading.json
│   ├── 10_summary_completion_selecting_from_list.json
│   ├── 11_summary_completion_selecting_words_from_text.json
│   └── 12_table_completion_reading.json
├── writing/
│   ├── 01_writing_part_1.json
│   └── 02_writing_part_2.json
└── complete_tests/
    ├── sample_listening_test_40q.json
    ├── sample_reading_test_40q.json
    └── sample_writing_test_2tasks.json
```

**Template Format Standard:**

Each template includes:
1. **Metadata Comments** - Description and use case
2. **Required Fields** - Must be present
3. **Optional Fields** - Can be null
4. **Field Descriptions** - What each field does
5. **Valid Values** - Accepted values/formats
6. **Working Example** - Real data that passes validation

**Example Template Structure:**
```json
{
  "_comment_type": "Question Type: Fill in the Gaps",
  "_comment_description": "Students fill in missing words in sentences. Used for listening for specific information.",
  "_comment_use_case": "Listening Section 1, factual information questions",
  
  "_required_fields": [
    "index", "type", "prompt", "answer_key"
  ],
  
  "_optional_fields": [
    "max_words", "instructions"
  ],
  
  "index": 1,
  "type": "fill_in_the_gaps",
  "prompt": "The student will study _____ at university.",
  "answer_key": "engineering",
  "max_words": 1,
  
  "_field_descriptions": {
    "index": "Question number (sequential, unique per test)",
    "type": "Exact type name - must be 'fill_in_the_gaps'",
    "prompt": "Question text with ___ for blank space",
    "answer_key": "Correct answer (case-insensitive matching)",
    "max_words": "Maximum words allowed (default: 3, range: 1-5)"
  },
  
  "_validation_rules": {
    "answer_key": "String, no special chars except hyphen/apostrophe",
    "max_words": "Integer 1-5",
    "prompt": "Must contain at least one ___"
  },
  
  "_grading": {
    "method": "case_insensitive_exact_match",
    "accepts_variations": ["engineering", "Engineering", "ENGINEERING"],
    "rejects": ["engineer", "engineerings", "engine"]
  }
}
```

**Deliverable:** 24 validated JSON template files

### Task 2.3: Create Complete Test Examples

**Action:** Create 3 full test JSON files with multiple question types

**Complete Listening Test (40 questions):**
```json
{
  "test_type": "listening",
  "title": "IELTS Listening Practice Test - Complete Example",
  "description": "Complete listening test with all 10 question types demonstrated",
  "duration_seconds": 2004,
  "audio_url": "https://audio.jukehost.co.uk/example",
  "sections": [
    {
      "index": 1,
      "title": "Section 1: Social Needs",
      "instructions": "Questions 1-10",
      "questions": [
        {"index": 1, "type": "fill_in_the_gaps", ...},
        {"index": 2, "type": "fill_in_the_gaps_short_answers", ...},
        {"index": 3, "type": "form_completion", ...}
      ]
    },
    {
      "index": 2,
      "title": "Section 2: Campus Facilities",
      "instructions": "Questions 11-20",
      "questions": [
        {"index": 11, "type": "labelling_on_a_map", ...},
        {"index": 12, "type": "multiple_choice_one_answer_listening", ...}
      ]
    }
  ]
}
```

**Complete Reading Test (40 questions):**
```json
{
  "test_type": "reading",
  "title": "IELTS Reading Practice Test - Complete Example",
  "description": "Complete reading test with all 12 question types demonstrated",
  "duration_seconds": 3600,
  "audio_url": null,
  "sections": [
    {
      "index": 1,
      "title": "Passage 1: Ancient Societies",
      "instructions": "Questions 1-13",
      "passage_text": "A\nAlthough humans have established many types...",
      "questions": [
        {"index": 1, "type": "identifying_information_true_false_not_given", ...},
        {"index": 8, "type": "sentence_completion_reading", ...}
      ]
    }
  ]
}
```

**Complete Writing Test (2 tasks):**
```json
{
  "test_type": "writing",
  "title": "IELTS Writing Practice Test - Complete Example",
  "description": "Complete writing test with both tasks",
  "duration_seconds": 3600,
  "audio_url": null,
  "sections": [
    {
      "index": 1,
      "title": "Writing Task 1",
      "instructions": "Spend about 20 minutes on this task",
      "questions": [
        {
          "index": 1,
          "type": "writing_part_1",
          "prompt": "The chart shows milk export figures from Italy, Russia and Poland from 2008 to 2012.",
          "chart_image": "https://example.com/chart.png",
          "min_words": 150,
          "answer_key": null
        }
      ]
    },
    {
      "index": 2,
      "title": "Writing Task 2",
      "instructions": "Spend about 40 minutes on this task",
      "questions": [
        {
          "index": 2,
          "type": "writing_part_2",
          "prompt": "Some people believe that international media should be controlled...",
          "min_words": 250,
          "answer_key": null
        }
      ]
    }
  ]
}
```

**Deliverable:** 3 complete test JSON files

### Task 2.4: Create Template README

**Action:** Write comprehensive README for template usage

**Content:**
```markdown
# Question Type Templates - Usage Guide

## Quick Start

1. Choose template for your question type from `listening/`, `reading/`, or `writing/`
2. Copy template content
3. Replace example values with your actual question data
4. Validate using `/api/tracks/validate-detailed` endpoint
5. Import using `/api/tracks/import-from-ai` endpoint

## Template Categories

### Listening (10 types)
- `01_fill_in_the_gaps.json` - Single blank, short answer
- `02_fill_in_the_gaps_short_answers.json` - Multiple blanks
- ...

### Reading (12 types)
- `01_flowchart_completion_selecting_words_from_text.json` - Flowchart with word limit
- `02_identifying_information_true_false_not_given.json` - TRUE/FALSE/NOT GIVEN
- ...

### Writing (2 types)
- `01_writing_part_1.json` - Chart/graph description
- `02_writing_part_2.json` - Essay writing

## Field Reference

[Complete field documentation]

## Validation Rules

[Complete validation rules]

## Common Issues

[Troubleshooting guide]
```

**Deliverable:** `/app/templates/question_types/README.md`

## Phase 2 Success Criteria
- ✅ 24 individual question templates created
- ✅ All templates validated against backend schema
- ✅ 3 complete test examples created
- ✅ Templates include comprehensive documentation
- ✅ README.md with usage instructions

## Phase 2 Outputs
1. 24 individual question template JSON files
2. 3 complete test example JSON files
3. `JSON_STRUCTURE_STANDARD.md`
4. `templates/question_types/README.md`

---

# 📍 PHASE 3: DEEPSEEK AI PROMPTS

**Duration:** 2 hours  
**Priority:** Critical  
**Dependencies:** Phase 2 complete

## Objectives
- Create AI prompts that generate perfect JSON from PDF text
- One master prompt + 24 type-specific prompts
- Include examples and validation rules
- Test with sample IELTS questions

## Tasks

### Task 3.1: Create Master Prompt Template

**Action:** Design universal prompt for DeepSeek AI

**File:** `/app/templates/ai_prompts/MASTER_PROMPT.md`

**Structure:**
```markdown
# IELTS Question Converter - Master Prompt

## Your Role
You are an expert IELTS exam question converter. Your task is to convert IELTS questions from PDF text into structured JSON format that can be imported into our test creation system.

## Critical Rules

### 1. Question Type Recognition
Use EXACT type names from this list:

**LISTENING TYPES (10):**
- `fill_in_the_gaps` - Single blank, short answer
- `fill_in_the_gaps_short_answers` - Multiple blanks in passage
- `flowchart_completion_listening` - Complete flowchart from audio
- `form_completion` - Fill in form fields
- `labelling_on_a_map` - Label locations on map
- `matching_listening` - Match items from audio
- `multiple_choice_more_than_one_answer_listening` - Choose 2-3 answers
- `multiple_choice_one_answer_listening` - Choose 1 answer
- `sentence_completion_listening` - Complete sentences
- `table_completion_listening` - Fill in table cells

**READING TYPES (12):**
- `flowchart_completion_selecting_words_from_text` - Complete flowchart with words from passage
- `identifying_information_true_false_not_given` - TRUE/FALSE/NOT GIVEN questions
- `matching_features` - Match features to descriptions
- `matching_headings` - Match paragraph headings
- `matching_sentence_endings` - Complete sentences by matching
- `multiple_choice_more_than_one_answer_reading` - Choose 2-3 answers
- `multiple_choice_one_answer_reading` - Choose 1 answer
- `note_completion` - Complete notes/summary
- `sentence_completion_reading` - Complete sentences from passage
- `summary_completion_selecting_from_list` - Complete summary from word list
- `summary_completion_selecting_words_from_text` - Complete summary from passage
- `table_completion_reading` - Fill in table from passage

**WRITING TYPES (2):**
- `writing_part_1` - Chart/graph/diagram description (150+ words)
- `writing_part_2` - Essay writing (250+ words)

### 2. Type Recognition Patterns

| If PDF says... | Use type... |
|---------------|-------------|
| "Write NO MORE THAN ONE/TWO/THREE WORD(S)" | `sentence_completion_reading` or `fill_in_the_gaps` |
| "TRUE, FALSE, or NOT GIVEN" | `identifying_information_true_false_not_given` |
| "YES, NO, or NOT GIVEN" | `identifying_information_true_false_not_given` |
| "Choose the correct letter A-H" for headings | `matching_headings` |
| "Complete the summary using words from the box" | `summary_completion_selecting_from_list` |
| "Complete the summary using words from the text" | `summary_completion_selecting_words_from_text` |
| "Choose TWO/THREE letters" | `multiple_choice_more_than_one_answer_reading/listening` |
| "Label the diagram/map/plan" | `labelling_on_a_map` (listening) or `note_completion` (reading) |
| "Complete the form/table" | `form_completion` or `table_completion_reading` |
| "Match each statement with correct person/place" | `matching_features` |
| "Complete sentences by choosing correct ending" | `matching_sentence_endings` |

### 3. JSON Structure
Always follow this exact structure:

```json
{
  "test_type": "listening|reading|writing",
  "title": "Test Title",
  "description": "Brief description",
  "duration_seconds": 3600,
  "audio_url": "https://..." (only for listening),
  "sections": [
    {
      "index": 1,
      "title": "Section 1: Title from PDF",
      "instructions": "Questions 1-10" (exactly as written in PDF),
      "passage_text": "..." (only for reading, full paragraph text),
      "questions": [
        {
          "index": 1,
          "type": "exact_type_name_from_list_above",
          "prompt": "Question text",
          "answer_key": "correct answer",
          "options": [...] (if applicable),
          "... other fields based on type"
        }
      ]
    }
  ]
}
```

### 4. Options Format
For multiple choice and TRUE/FALSE/NOT GIVEN questions:

```json
"options": [
  {"value": "A", "text": "First option text"},
  {"value": "B", "text": "Second option text"},
  {"value": "C", "text": "Third option text"}
]
```

For TRUE/FALSE/NOT GIVEN specifically:
```json
"options": [
  {"value": "TRUE", "text": "TRUE"},
  {"value": "FALSE", "text": "FALSE"},
  {"value": "NOT GIVEN", "text": "NOT GIVEN"}
]
```

### 5. Word Lists
When question has a word bank (like "Choose from: A-History, B-Science..."):

```json
"word_list": ["History", "Science", "Mathematics", "Art", "Geography"]
```

### 6. Headings Format
For matching headings questions:

```json
"headings": [
  {"value": "i", "text": "The early stages"},
  {"value": "ii", "text": "Modern developments"},
  {"value": "iii", "text": "Future prospects"}
]
```

### 7. Answer Keys
- For short answer: `"answer_key": "engineering"`
- For multiple choice: `"answer_key": "B"`
- For TRUE/FALSE/NOT GIVEN: `"answer_key": "TRUE"`
- For multiple answer: `"answer_key": ["B", "D"]`
- For matching: `"answer_key": "iii"`
- For writing: `"answer_key": null`

### 8. Sequential Indexing
Question indices MUST be sequential starting from 1:
- Section 1: Questions 1-10
- Section 2: Questions 11-20
- Section 3: Questions 21-30
- Section 4: Questions 31-40

### 9. Passage Text (Reading Only)
Include the COMPLETE passage text with paragraph markers:
```json
"passage_text": "A\nFirst paragraph text here.\n\nB\nSecond paragraph text here.\n\nC\nThird paragraph..."
```

## Examples

### Example 1: TRUE/FALSE/NOT GIVEN
**PDF Input:**
```
Questions 1-5
Do the following statements agree with the information in the text?
Write:
TRUE if the statement agrees with the information
FALSE if the statement contradicts the information
NOT GIVEN if there is no information on this

1. The company was founded in 1990.
2. All employees receive training.
```

**JSON Output:**
```json
{
  "index": 1,
  "type": "identifying_information_true_false_not_given",
  "prompt": "The company was founded in 1990.",
  "answer_key": "TRUE",
  "options": [
    {"value": "TRUE", "text": "TRUE"},
    {"value": "FALSE", "text": "FALSE"},
    {"value": "NOT GIVEN", "text": "NOT GIVEN"}
  ]
}
```

### Example 2: Sentence Completion
**PDF Input:**
```
Questions 6-10
Complete the sentences below.
Write NO MORE THAN TWO WORDS from the passage for each answer.

6. The building was constructed using _____.
```

**JSON Output:**
```json
{
  "index": 6,
  "type": "sentence_completion_reading",
  "prompt": "The building was constructed using _____.",
  "answer_key": "local materials",
  "max_words": 2
}
```

### Example 3: Matching Headings
**PDF Input:**
```
Questions 14-19
The reading passage has six paragraphs, A-F.
Choose the correct heading for each paragraph from the list of headings below.

List of Headings:
i. Early development
ii. Modern applications
iii. Future possibilities

14. Paragraph A
```

**JSON Output:**
```json
{
  "index": 14,
  "type": "matching_headings",
  "prompt": "Paragraph A",
  "answer_key": "i",
  "headings": [
    {"value": "i", "text": "Early development"},
    {"value": "ii", "text": "Modern applications"},
    {"value": "iii", "text": "Future possibilities"}
  ]
}
```

## Validation Checklist
Before outputting JSON, verify:
- [ ] test_type is "listening", "reading", or "writing"
- [ ] All question types match exact names from the list
- [ ] Question indices are sequential with no gaps
- [ ] answer_key present for all except writing
- [ ] options format is array of objects with value and text
- [ ] passage_text included for reading tests
- [ ] audio_url included for listening tests
- [ ] No missing commas or brackets
- [ ] Valid JSON syntax

## Now Convert

Paste your IELTS question text below, and I'll convert it to perfect JSON:

[USER PASTES QUESTION TEXT HERE]
```

**Deliverable:** `/app/templates/ai_prompts/MASTER_PROMPT.md`

### Task 3.2: Create Type-Specific Prompts

**Action:** Create 24 focused prompts for each question type

**Directory Structure:**
```
/app/templates/ai_prompts/
├── MASTER_PROMPT.md
├── listening/
│   ├── prompt_fill_in_the_gaps.md
│   ├── prompt_fill_in_the_gaps_short_answers.md
│   ├── prompt_flowchart_completion_listening.md
│   ├── prompt_form_completion.md
│   ├── prompt_labelling_on_a_map.md
│   ├── prompt_matching_listening.md
│   ├── prompt_multiple_choice_more_than_one_answer_listening.md
│   ├── prompt_multiple_choice_one_answer_listening.md
│   ├── prompt_sentence_completion_listening.md
│   └── prompt_table_completion_listening.md
├── reading/
│   ├── prompt_flowchart_completion_selecting_words_from_text.md
│   ├── prompt_identifying_information_true_false_not_given.md
│   ├── prompt_matching_features.md
│   ├── prompt_matching_headings.md
│   ├── prompt_matching_sentence_endings.md
│   ├── prompt_multiple_choice_more_than_one_answer_reading.md
│   ├── prompt_multiple_choice_one_answer_reading.md
│   ├── prompt_note_completion.md
│   ├── prompt_sentence_completion_reading.md
│   ├── prompt_summary_completion_selecting_from_list.md
│   ├── prompt_summary_completion_selecting_words_from_text.md
│   └── prompt_table_completion_reading.md
└── writing/
    ├── prompt_writing_part_1.md
    └── prompt_writing_part_2.md
```

**Type-Specific Prompt Structure:**
```markdown
# [Question Type Name] - Conversion Prompt

## Recognition
When you see these indicators in the PDF:
- "keyword phrase 1"
- "keyword phrase 2"
- "keyword phrase 3"

Use type: `exact_type_name`

## Required Fields
- field1 (description)
- field2 (description)

## Optional Fields
- field3 (description)

## JSON Template
```json
{
  "index": 1,
  "type": "exact_type_name",
  ...
}
```

## Real Examples
[3-5 real IELTS examples with conversions]

## Common Mistakes to Avoid
- Mistake 1 and how to fix
- Mistake 2 and how to fix
```

**Deliverable:** 24 type-specific prompt files

### Task 3.3: Create DeepSeek Quick Reference

**Action:** Create cheat sheet for quick lookups

**File:** `/app/templates/ai_prompts/DEEPSEEK_CHEATSHEET.md`

**Content:**
```markdown
# DeepSeek Quick Reference

## Type Selection Matrix

| PDF Indicator | Question Type | Category |
|--------------|---------------|----------|
| "NO MORE THAN ONE WORD" | `sentence_completion_reading` or `fill_in_the_gaps` | Reading/Listening |
| "TRUE/FALSE/NOT GIVEN" | `identifying_information_true_false_not_given` | Reading |
| "Choose correct heading" | `matching_headings` | Reading |
| "Match features" | `matching_features` | Reading |
| "Complete sentence endings" | `matching_sentence_endings` | Reading |
| "Complete from word list" | `summary_completion_selecting_from_list` | Reading |
| "Complete from passage" | `summary_completion_selecting_words_from_text` | Reading |
| "Choose TWO letters" | `multiple_choice_more_than_one_answer_*` | Reading/Listening |
| "Choose ONE letter A-D" | `multiple_choice_one_answer_*` | Reading/Listening |
| "Label the map" | `labelling_on_a_map` | Listening |
| "Complete the form" | `form_completion` | Listening |
| "Complete the table" | `table_completion_*` | Reading/Listening |
| "Complete flowchart" | `flowchart_completion_*` | Reading/Listening |
| "Complete notes" | `note_completion` | Reading |
| "At least 150 words" | `writing_part_1` | Writing |
| "At least 250 words" | `writing_part_2` | Writing |

## Field Requirements by Type

### All Question Types
```json
{
  "index": 1,          // Required: Sequential number
  "type": "...",       // Required: Exact type name
  "prompt": "...",     // Required: Question text
  "answer_key": "..."  // Required (except writing)
}
```

### Multiple Choice Types
```json
{
  "options": [         // Required
    {"value": "A", "text": "..."},
    {"value": "B", "text": "..."}
  ],
  "max_choices": 2     // Optional: for "more than one answer" types
}
```

### Matching Types
```json
{
  "headings": [...],   // For matching_headings
  "features": [...],   // For matching_features
  "endings": [...]     // For matching_sentence_endings
}
```

### Word Limit Types
```json
{
  "max_words": 2       // For completion questions
}
```

### Writing Types
```json
{
  "min_words": 150,           // Required
  "chart_image": "https://",  // Optional (Part 1)
  "instructions": "...",      // Optional
  "answer_key": null          // Always null
}
```

## Common Conversions

### PDF → JSON Examples

**Example 1: Basic Conversion**
```
PDF: "1. The building was constructed in _____."
Answer: 1990

JSON:
{
  "index": 1,
  "type": "sentence_completion_reading",
  "prompt": "The building was constructed in _____.",
  "answer_key": "1990",
  "max_words": 1
}
```

**Example 2: Multiple Choice**
```
PDF: "2. What is the main purpose?
A. To inform
B. To entertain
C. To persuade"
Answer: A

JSON:
{
  "index": 2,
  "type": "multiple_choice_one_answer_reading",
  "prompt": "What is the main purpose?",
  "answer_key": "A",
  "options": [
    {"value": "A", "text": "To inform"},
    {"value": "B", "text": "To entertain"},
    {"value": "C", "text": "To persuade"}
  ]
}
```

**Example 3: TRUE/FALSE/NOT GIVEN**
```
PDF: "3. The author supports the theory."
Answer: TRUE

JSON:
{
  "index": 3,
  "type": "identifying_information_true_false_not_given",
  "prompt": "The author supports the theory.",
  "answer_key": "TRUE",
  "options": [
    {"value": "TRUE", "text": "TRUE"},
    {"value": "FALSE", "text": "FALSE"},
    {"value": "NOT GIVEN", "text": "NOT GIVEN"}
  ]
}
```

## Troubleshooting

### Issue: Type name not recognized
**Error:** "Invalid question type: 'true_false'"
**Fix:** Use full name: `identifying_information_true_false_not_given`

### Issue: Options format wrong
**Error:** "Input should be a valid dictionary"
**Fix:** Use `[{"value": "A", "text": "..."}, ...]` not `["A", "B", "C"]`

### Issue: Missing answer_key
**Error:** "answer_key is required"
**Fix:** Add answer_key for all except `writing_part_1` and `writing_part_2`

### Issue: Sequential indices
**Error:** "Duplicate question indices"
**Fix:** Questions must be 1, 2, 3, 4... with no gaps or duplicates

## Quick Check Before Submit

✅ test_type is "listening", "reading", or "writing"  
✅ All types match exact names from master list  
✅ Questions numbered 1, 2, 3... sequentially  
✅ answer_key present (except writing)  
✅ options as array of objects  
✅ Valid JSON (no missing commas/brackets)  
✅ passage_text included (reading only)  
✅ audio_url included (listening only)
```

**Deliverable:** `/app/templates/ai_prompts/DEEPSEEK_CHEATSHEET.md`

### Task 3.4: Test Prompts with Sample Questions

**Action:** Validate prompts work with real IELTS questions

**Test Cases:**
1. Take 5 real IELTS questions (different types)
2. Use master prompt with DeepSeek
3. Verify generated JSON validates
4. Document any issues
5. Refine prompts based on results

**Deliverable:** Test results document

## Phase 3 Success Criteria
- ✅ Master prompt created and tested
- ✅ 24 type-specific prompts created
- ✅ Quick reference cheat sheet complete
- ✅ Prompts validated with real questions
- ✅ All prompts produce valid JSON

## Phase 3 Outputs
1. `MASTER_PROMPT.md`
2. 24 type-specific prompt files
3. `DEEPSEEK_CHEATSHEET.md`
4. `PROMPT_TEST_RESULTS.md`

---

# 📍 PHASE 4: BACKEND VALIDATION FIX

**Duration:** 3-4 hours  
**Priority:** Critical  
**Dependencies:** Phases 1-3 complete

## Objectives
- Accept all possible type name variations
- Auto-normalize input formats
- Provide clear error messages
- Add validation preview endpoint

## Tasks

### Task 4.1: Expand Legacy Type Mapping

**Action:** Create comprehensive type name mapping

**File:** `/app/backend/ai_import_service.py`

**Add Complete Mapping:**
```python
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
```

**Deliverable:** Comprehensive type mapping

### Task 4.2: Implement Smart Auto-Normalization

**Action:** Add validators to auto-fix common format issues

**Add Validators:**

```python
class QuestionImport(BaseModel):
    """Individual question import with auto-normalization"""
    index: int
    type: str
    prompt: str
    answer_key: Optional[Any] = None
    options: Optional[Any] = None
    wordlist: Optional[List[str]] = None
    word_list: Optional[List[str]] = None
    # ... other fields
    
    @validator('type', pre=True)
    def normalize_question_type(cls, v):
        """Convert legacy type names to QTI standard names"""
        if not v:
            raise ValueError("Question type is required")
        
        v_lower = v.lower().strip().replace(' ', '_').replace('-', '_')
        
        # Check direct match first
        if v_lower in LEGACY_TYPE_MAPPING:
            return LEGACY_TYPE_MAPPING[v_lower]
        
        # Check if already valid
        valid_types = {
            "fill_in_the_gaps", "fill_in_the_gaps_short_answers",
            "flowchart_completion_listening", "form_completion",
            "labelling_on_a_map", "matching_listening",
            "multiple_choice_more_than_one_answer_listening",
            "multiple_choice_one_answer_listening",
            "sentence_completion_listening", "table_completion_listening",
            "flowchart_completion_selecting_words_from_text",
            "identifying_information_true_false_not_given",
            "matching_features", "matching_headings",
            "matching_sentence_endings",
            "multiple_choice_more_than_one_answer_reading",
            "multiple_choice_one_answer_reading", "note_completion",
            "sentence_completion_reading",
            "summary_completion_selecting_from_list",
            "summary_completion_selecting_words_from_text",
            "table_completion_reading", "writing_part_1", "writing_part_2"
        }
        
        if v_lower in valid_types:
            return v_lower
        
        raise ValueError(
            f"Invalid question type: '{v}'. "
            f"Please use one of: {', '.join(sorted(valid_types))}. "
            f"See documentation for complete list."
        )
    
    @validator('options', pre=True)
    def normalize_options(cls, v):
        """Auto-convert any option format to standard dict array"""
        if v is None:
            return None
        
        # Already correct format
        if isinstance(v, list) and v and isinstance(v[0], dict):
            return v
        
        # String array → Dict array
        if isinstance(v, list) and v and isinstance(v[0], str):
            return [{"value": opt, "text": opt} for opt in v]
        
        # Single string → Dict array
        if isinstance(v, str):
            return [{"value": v, "text": v}]
        
        return v
    
    @validator('word_list')
    def merge_wordlist_fields(cls, v, values):
        """Merge legacy 'wordlist' field into 'word_list'"""
        # If word_list is None but wordlist exists, use wordlist
        if v is None and 'wordlist' in values and values['wordlist']:
            return values['wordlist']
        return v
    
    @validator('answer_key')
    def validate_answer_key_presence(cls, v, values):
        """Ensure answer_key present for non-writing types"""
        q_type = values.get('type')
        
        # Writing types don't need answer keys
        if q_type in ['writing_part_1', 'writing_part_2']:
            return None
        
        if not v:
            raise ValueError(
                f"answer_key is required for question type '{q_type}'. "
                f"Only writing questions can have null answer_key."
            )
        
        return v
    
    @validator('prompt')
    def validate_prompt(cls, v):
        """Ensure prompt is not empty"""
        if not v or not v.strip():
            raise ValueError("Question prompt cannot be empty")
        return v.strip()
```

**Deliverable:** Smart validation system

### Task 4.3: Add Validation Preview Endpoint

**Action:** Create endpoint to validate without creating

**Add Endpoint:**

```python
@router.post("/api/tracks/validate-detailed")
async def validate_import_detailed(request: AIImportRequest):
    """
    Validate import without creating anything
    Shows what will be created and any auto-corrections
    """
    try:
        # Validation happens automatically through Pydantic
        # If we get here, validation passed
        
        # Collect statistics
        total_questions = sum(len(section.questions) for section in request.sections)
        questions_by_type = {}
        
        for section in request.sections:
            for question in section.questions:
                q_type = question.type
                questions_by_type[q_type] = questions_by_type.get(q_type, 0) + 1
        
        # Check for potential issues (warnings, not errors)
        warnings = []
        
        # Check audio URL for listening
        if request.test_type == "listening" and not request.audio_url:
            warnings.append("Listening test should have audio_url")
        
        # Check passage text for reading
        for section in request.sections:
            if request.test_type == "reading" and not section.passage_text:
                warnings.append(f"Section {section.index}: Reading section should have passage_text")
        
        # Check question count
        if request.test_type in ["listening", "reading"] and total_questions != 40:
            warnings.append(f"Expected 40 questions for {request.test_type}, got {total_questions}")
        
        if request.test_type == "writing" and total_questions != 2:
            warnings.append(f"Expected 2 tasks for writing, got {total_questions}")
        
        return {
            "valid": True,
            "message": "Import validation successful",
            "statistics": {
                "test_type": request.test_type,
                "title": request.title,
                "total_sections": len(request.sections),
                "total_questions": total_questions,
                "duration_minutes": request.duration_seconds // 60,
                "questions_by_type": questions_by_type
            },
            "warnings": warnings if warnings else None,
            "preview": {
                "exam_id": "will_be_generated_on_import",
                "will_create": {
                    "exam": 1,
                    "sections": len(request.sections),
                    "questions": total_questions
                }
            },
            "normalized_data": request.dict()  # Show final processed data
        }
        
    except ValidationError as e:
        # Return detailed validation errors
        return {
            "valid": False,
            "errors": [
                {
                    "field": ".".join(str(x) for x in error["loc"]),
                    "message": error["msg"],
                    "type": error["type"],
                    "input": error.get("input")
                }
                for error in e.errors()
            ],
            "help": "See /app/docs/AI_IMPORT_GUIDE.md for examples"
        }
```

**Deliverable:** Validation preview endpoint

### Task 4.4: Improve Error Messages

**Action:** Add helpful error messages with suggestions

**Update Validators:**

```python
@validator('type')
def validate_question_type_with_suggestions(cls, v):
    """Provide helpful suggestions for invalid types"""
    valid_types = {...}  # list of valid types
    
    if v not in valid_types:
        # Find similar types (fuzzy match)
        from difflib import get_close_matches
        suggestions = get_close_matches(v, valid_types, n=3, cutoff=0.6)
        
        error_msg = f"Invalid question type: '{v}'."
        
        if suggestions:
            error_msg += f" Did you mean: {', '.join(suggestions)}?"
        else:
            error_msg += f" Valid types: {', '.join(sorted(valid_types))}."
        
        error_msg += " See /app/docs/QUESTION_TYPE_REFERENCE.md for details."
        
        raise ValueError(error_msg)
    
    return v
```

**Deliverable:** Better error messages

## Phase 4 Success Criteria
- ✅ 50+ legacy type name variations supported
- ✅ Auto-normalization for options, wordlist, etc.
- ✅ Validation preview endpoint working
- ✅ Clear error messages with suggestions
- ✅ User's original JSON validates and imports

## Phase 4 Outputs
1. Updated `ai_import_service.py` with complete mapping
2. New validation preview endpoint
3. Improved error messages
4. Test report showing successful import

---

# 📍 PHASE 5: FRONTEND INTEGRATION

**Duration:** 4-5 hours  
**Priority:** High  
**Dependencies:** Phases 1-4 complete

## Objectives
- Complete QTI component integration in all test interfaces
- Create question type preview test
- Verify all 24 types render correctly
- Test student interaction flows

## Tasks

### Task 5.1: Complete ListeningTest.jsx Integration

**Action:** Integrate all 10 listening QTI components

**File:** `/app/frontend/src/components/ListeningTest.jsx`

**Check Imports:**
```javascript
// QTI Listening Components
import FillInTheGaps from './qti/listening/FillInTheGaps';
import FillInTheGapsShortAnswers from './qti/listening/FillInTheGapsShortAnswers';
import FlowchartCompletionListening from './qti/listening/FlowchartCompletionListening';
import FormCompletion from './qti/listening/FormCompletion';
import LabellingOnAMap from './qti/listening/LabellingOnAMap';
import MatchingListening from './qti/listening/MatchingListening';
import MultipleChoiceMoreThanOneAnswerListening from './qti/listening/MultipleChoiceMoreThanOneAnswerListening';
import MultipleChoiceOneAnswerListening from './qti/listening/MultipleChoiceOneAnswerListening';
import SentenceCompletionListening from './qti/listening/SentenceCompletionListening';
import TableCompletionListening from './qti/listening/TableCompletionListening';
```

**Update Switch Statement:**
```javascript
const renderQuestionComponent = (question) => {
  const answer = answers[question.index] || '';
  const onChange = (value) => handleAnswerChange(question.index, value);
  const onFocus = () => setCurrentQuestionIndex(question.index);
  
  switch (question.type) {
    // Listening Types
    case 'fill_in_the_gaps':
      return <FillInTheGaps question={question} answer={answer} onAnswerChange={handleAnswerChange} onFocus={onFocus} />;
    
    case 'fill_in_the_gaps_short_answers':
      return <FillInTheGapsShortAnswers question={question} answer={answer} onAnswerChange={handleAnswerChange} onFocus={onFocus} />;
    
    case 'flowchart_completion_listening':
      return <FlowchartCompletionListening question={question} answer={answer} onAnswerChange={handleAnswerChange} onFocus={onFocus} />;
    
    case 'form_completion':
      return <FormCompletion question={question} answer={answer} onAnswerChange={handleAnswerChange} onFocus={onFocus} />;
    
    case 'labelling_on_a_map':
      return <LabellingOnAMap question={question} answer={answer} onAnswerChange={handleAnswerChange} onFocus={onFocus} />;
    
    case 'matching_listening':
      return <MatchingListening question={question} answer={answer} onAnswerChange={handleAnswerChange} onFocus={onFocus} />;
    
    case 'multiple_choice_more_than_one_answer_listening':
      return <MultipleChoiceMoreThanOneAnswerListening question={question} answer={answer} onAnswerChange={handleAnswerChange} onFocus={onFocus} />;
    
    case 'multiple_choice_one_answer_listening':
      return <MultipleChoiceOneAnswerListening question={question} answer={answer} onAnswerChange={handleAnswerChange} onFocus={onFocus} />;
    
    case 'sentence_completion_listening':
      return <SentenceCompletionListening question={question} answer={answer} onAnswerChange={handleAnswerChange} onFocus={onFocus} />;
    
    case 'table_completion_listening':
      return <TableCompletionListening question={question} answer={answer} onAnswerChange={handleAnswerChange} onFocus={onFocus} />;
    
    // Legacy types for backward compatibility
    case 'short_answer':
    case 'multiple_choice':
    case 'map_labeling':
    case 'diagram_labeling':
      // Handle legacy types with existing components
      return renderLegacyQuestion(question);
    
    default:
      return (
        <div className="mb-4 p-4 border border-yellow-400 bg-yellow-50 rounded">
          <p className="text-sm text-gray-700">
            <span className="font-semibold">Question {question.index}:</span> Unsupported question type "{question.type}"
          </p>
        </div>
      );
  }
};
```

**Deliverable:** Complete listening integration

### Task 5.2: Verify ReadingTest.jsx Integration

**Action:** Confirm all 12 reading components integrated

**File:** `/app/frontend/src/components/ReadingTest.jsx`

**Status:** ✅ Already done in previous task (Phase 3 continuation)

**Verify:**
- All 12 imports present
- All 12 cases in switch statement
- Props correctly passed (question, answer, onAnswerChange, onFocus)
- Legacy types still supported

**Deliverable:** Verification report

### Task 5.3: Verify WritingTest.jsx Integration

**Action:** Confirm both writing components integrated

**File:** `/app/frontend/src/components/WritingTest.jsx`

**Status:** ✅ Already done in previous task (Phase 3 continuation)

**Verify:**
- WritingPart1 and WritingPart2 imported
- renderQuestionComponent function exists
- Conditional rendering works (QTI vs legacy)
- Props correctly passed

**Deliverable:** Verification report

### Task 5.4: Create Question Type Preview Test

**Action:** Create special test with ONE example of each type

**Create JSON:**
```json
{
  "test_type": "reading",
  "title": "Question Type Preview - All 24 QTI Types",
  "description": "Demo test showing all question types with sample data",
  "duration_seconds": 7200,
  "audio_url": "https://audio.jukehost.co.uk/sample",
  "sections": [
    {
      "index": 1,
      "title": "LISTENING TYPES (10)",
      "instructions": "Questions 1-10: Preview of all listening question types",
      "questions": [
        {
          "index": 1,
          "type": "fill_in_the_gaps",
          "prompt": "The student will study _____ at university.",
          "answer_key": "engineering",
          "max_words": 1
        },
        {
          "index": 2,
          "type": "fill_in_the_gaps_short_answers",
          "prompt": "Complete the notes below.\n\nName: _____\nAge: _____\nCity: _____",
          "answer_key": ["John", "25", "London"],
          "max_words": 2
        },
        // ... all 10 listening types
      ]
    },
    {
      "index": 2,
      "title": "READING TYPES (12)",
      "instructions": "Questions 11-22: Preview of all reading question types",
      "passage_text": "A\nThis is a sample passage for reading questions...",
      "questions": [
        {
          "index": 11,
          "type": "identifying_information_true_false_not_given",
          "prompt": "The passage discusses environmental issues.",
          "answer_key": "TRUE",
          "options": [
            {"value": "TRUE", "text": "TRUE"},
            {"value": "FALSE", "text": "FALSE"},
            {"value": "NOT GIVEN", "text": "NOT GIVEN"}
          ]
        },
        // ... all 12 reading types
      ]
    },
    {
      "index": 3,
      "title": "WRITING TYPES (2)",
      "instructions": "Tasks 23-24: Preview of writing tasks",
      "questions": [
        {
          "index": 23,
          "type": "writing_part_1",
          "prompt": "The chart shows milk export figures...",
          "chart_image": "https://example.com/chart.png",
          "min_words": 150,
          "answer_key": null
        },
        {
          "index": 24,
          "type": "writing_part_2",
          "prompt": "Some people believe that...",
          "min_words": 250,
          "answer_key": null
        }
      ]
    }
  ]
}
```

**Import Script:**
```bash
curl -X POST http://localhost:8001/api/tracks/import-from-ai \
  -H "Content-Type: application/json" \
  -d @/app/templates/question_types/complete_tests/question_type_preview_test.json
```

**Deliverable:** Question type preview test

### Task 5.5: Visual Testing

**Action:** Take the preview test and verify each type renders

**Test Each Component:**
1. Navigate to exam
2. For each question type:
   - ✅ Component renders without errors
   - ✅ Question text displays correctly
   - ✅ Input fields/controls appear
   - ✅ Can enter answer
   - ✅ Answer saves correctly
   - ✅ Navigation works
   - ✅ Styling matches existing design

**Document Issues:**
- Screenshot each question type
- Note any rendering issues
- Note any interaction problems
- Note any styling inconsistencies

**Deliverable:** Visual test report with screenshots

### Task 5.6: Create Missing Components

**Action:** If any components are missing, create them

**For Each Missing Component:**

1. **Check if truly missing**
   ```bash
   ls /app/frontend/src/components/qti/[category]/ComponentName.jsx
   ```

2. **If missing, create from template:**
   ```javascript
   import React from 'react';
   
   /**
    * [Question Type Name] - [Category]
    * [Description of question type]
    * QTI Source: /app/Question type/[Category]/[Type Folder]/
    */
   const ComponentName = ({ question, answer, onAnswerChange, onFocus }) => {
     const questionNum = question.index;
     const { prompt, /* other fields */ } = question.payload;
   
     return (
       <div 
         className="mb-4" 
         data-question-index={questionNum}
         onClick={() => onFocus && onFocus(questionNum)}
       >
         <div className="flex items-start gap-2">
           <span className="font-semibold min-w-[3rem]">{questionNum}.</span>
           <div className="flex-1">
             <p className="text-gray-700 mb-2">{prompt}</p>
             {/* Component-specific UI */}
           </div>
         </div>
       </div>
     );
   };
   
   export default ComponentName;
   ```

3. **Test component individually**

**Deliverable:** Any new components created

## Phase 5 Success Criteria
- ✅ All 24 QTI components integrated
- ✅ All test interfaces (Listening, Reading, Writing) updated
- ✅ Question type preview test created and working
- ✅ Visual test completed with screenshots
- ✅ All components render correctly
- ✅ Student interactions work properly

## Phase 5 Outputs
1. Updated test component files
2. Question type preview test JSON
3. Visual test report with 24 screenshots
4. Any new components created
5. Integration status document

---

# 📍 PHASE 6: COMPREHENSIVE DOCUMENTATION

**Duration:** 3-4 hours  
**Priority:** High  
**Dependencies:** Phases 1-5 complete

## Objectives
- Create complete reference guide for all 24 types
- Write AI import guide for DeepSeek users
- Create admin user manual
- Document API endpoints

## Tasks

### Task 6.1: Question Type Reference Guide

**Action:** Create comprehensive reference for all types

**File:** `/app/docs/QUESTION_TYPE_REFERENCE.md`

**Structure:**
```markdown
# Complete IELTS Question Type Reference

## Table of Contents
1. [Overview](#overview)
2. [Listening Types (10)](#listening-types)
3. [Reading Types (12)](#reading-types)
4. [Writing Types (2)](#writing-types)
5. [Quick Reference Table](#quick-reference-table)

---

## Overview

This document provides complete specifications for all 24 QTI-compliant IELTS question types supported by the system.

### Type Categories
- **Listening:** 10 types for audio-based questions
- **Reading:** 12 types for passage-based questions
- **Writing:** 2 types for essay writing tasks

### Document Conventions
- **Type Name:** Exact string to use in JSON
- **Required Fields:** Must be present in JSON
- **Optional Fields:** Can be null or omitted
- **Grading:** How answers are evaluated

---

## Listening Types

### 1.1 Fill in the Gaps

**Description:** Students listen and fill in missing words in sentences or short passages.

**Type Name:** `fill_in_the_gaps`

**Use Case:** Listening for specific information, factual details

**UI Component:** FillInTheGaps.jsx

**Required Fields:**
```json
{
  "index": 1,
  "type": "fill_in_the_gaps",
  "prompt": "Question text with _____ blank",
  "answer_key": "correct answer"
}
```

**Optional Fields:**
```json
{
  "max_words": 1,          // Default: 3
  "instructions": "..."     // Additional instructions
}
```

**Grading Rules:**
- Case-insensitive exact match
- Accepts minor spelling variations
- Punctuation ignored
- Extra spaces trimmed

**JSON Example:**
```json
{
  "index": 1,
  "type": "fill_in_the_gaps",
  "prompt": "The student will study _____ at university.",
  "answer_key": "engineering",
  "max_words": 1
}
```

**Visual Preview:**
```
1. The student will study _____ at university.

[Text input field]

Note: Write NO MORE THAN ONE WORD
```

**Common Mistakes:**
- ❌ Using "fill_gaps" instead of "fill_in_the_gaps"
- ❌ Forgetting answer_key
- ❌ Not including blank (___) in prompt

**DeepSeek Recognition:**
When PDF says: "Write NO MORE THAN ONE/TWO WORD(S) for each answer"

---

[Repeat for all 24 types with same structure]

---

## Quick Reference Table

| # | Type Name | Category | Answer Format | Auto-Graded |
|---|-----------|----------|---------------|-------------|
| 1 | fill_in_the_gaps | Listening | String | Yes |
| 2 | fill_in_the_gaps_short_answers | Listening | Array | Yes |
| ... | ... | ... | ... | ... |
| 24 | writing_part_2 | Writing | Long text | No |
```

**Deliverable:** Complete reference guide (50+ pages)

### Task 6.2: AI Import Guide

**Action:** Write step-by-step guide for DeepSeek users

**File:** `/app/docs/AI_IMPORT_GUIDE.md`

**Content:**
```markdown
# AI Import Guide - DeepSeek Integration

## Quick Start (5 minutes)

1. **Prepare your IELTS questions**
   - Get PDF or text of IELTS questions
   - Copy the text

2. **Open DeepSeek**
   - Go to DeepSeek AI chat
   - Paste master prompt from `/app/templates/ai_prompts/MASTER_PROMPT.md`

3. **Paste questions**
   - Add your IELTS question text after the prompt
   - DeepSeek generates JSON

4. **Validate**
   ```bash
   curl -X POST /api/tracks/validate-detailed \
     -H "Content-Type: application/json" \
     -d @generated.json
   ```

5. **Import**
   ```bash
   curl -X POST /api/tracks/import-from-ai \
     -H "Content-Type: application/json" \
     -d @generated.json
   ```

6. **Verify**
   - Check admin panel
   - Take test as student

---

## Detailed Process

### Step 1: Extract Question Text from PDF

#### Option A: Copy-Paste
1. Open PDF in browser or PDF reader
2. Select all text (Ctrl+A / Cmd+A)
3. Copy (Ctrl+C / Cmd+C)
4. Paste into text editor
5. Clean up formatting:
   - Remove page numbers
   - Remove headers/footers
   - Keep question numbers
   - Keep all answer choices

#### Option B: OCR Tools
If PDF is scanned image:
1. Use Adobe Acrobat OCR
2. Use Google Drive (upload → open with Google Docs)
3. Use online OCR services

**Example Clean Text:**
```
Questions 1-5

Do the following statements agree with the information in the passage?

Write:
TRUE if the statement agrees
FALSE if contradicts
NOT GIVEN if no information

1. The company was founded in 1990.
2. All employees receive training.
```

---

### Step 2: Use DeepSeek to Generate JSON

#### 2.1 Open DeepSeek
- Go to https://chat.deepseek.com/ (or your DeepSeek interface)
- Start new conversation

#### 2.2 Load Master Prompt
- Open `/app/templates/ai_prompts/MASTER_PROMPT.md`
- Copy entire content
- Paste into DeepSeek

#### 2.3 Add Your Questions
After the master prompt, add:
```
Now convert these questions:

[PASTE YOUR QUESTIONS HERE]
```

#### 2.4 Review Output
DeepSeek will generate JSON like:
```json
{
  "test_type": "reading",
  "title": "...",
  ...
}
```

#### 2.5 Copy JSON
- Select all JSON output
- Copy to clipboard
- Save as `.json` file

---

### Step 3: Validate Before Import

**Why Validate?**
- Catch errors early
- See what will be created
- Get warnings about potential issues

**Validation Command:**
```bash
curl -X POST http://localhost:8001/api/tracks/validate-detailed \
  -H "Content-Type: application/json" \
  -d @your_test.json
```

**Success Response:**
```json
{
  "valid": true,
  "statistics": {
    "total_questions": 40,
    "by_type": {
      "identifying_information_true_false_not_given": 7,
      "sentence_completion_reading": 13
    }
  },
  "warnings": null
}
```

**Error Response:**
```json
{
  "valid": false,
  "errors": [
    {
      "field": "sections.0.questions.0.type",
      "message": "Invalid question type: 'true_false'",
      "help": "Did you mean: identifying_information_true_false_not_given?"
    }
  ]
}
```

---

### Step 4: Import Test

**Import Command:**
```bash
curl -X POST http://localhost:8001/api/tracks/import-from-ai \
  -H "Content-Type: application/json" \
  -d @your_test.json
```

**Success Response:**
```json
{
  "success": true,
  "track_id": "abc123...",
  "exam_id": "your-test-slug",
  "message": "Track and exam created successfully",
  "statistics": {
    "created": {
      "exam": 1,
      "sections": 3,
      "questions": 40
    }
  }
}
```

---

### Step 5: Verify in Admin Panel

1. **Login to Admin**
   - Go to `/admin/login`
   - Use admin credentials

2. **Check Test Management**
   - Go to "Test Management"
   - Find your imported test
   - Verify question count

3. **Check Questions**
   - Click test name
   - Review each question
   - Verify types and content

4. **Publish Test**
   - Click "Publish" button
   - Test becomes visible to students

---

## Troubleshooting

### Issue 1: Type Name Not Recognized

**Error Message:**
```
Invalid question type: 'true_false'
```

**Cause:** Using shortened/incorrect type name

**Solution:**
Use full name: `identifying_information_true_false_not_given`

See `/app/docs/QUESTION_TYPE_REFERENCE.md` for all valid names.

---

### Issue 2: Options Format Wrong

**Error Message:**
```
Input should be a valid dictionary
```

**Cause:** Options as string array instead of dict array

**Wrong:**
```json
"options": ["A", "B", "C"]
```

**Correct:**
```json
"options": [
  {"value": "A", "text": "First option"},
  {"value": "B", "text": "Second option"}
]
```

**Auto-Fix:** Backend should auto-convert this, but best to use correct format.

---

[20+ more troubleshooting scenarios]

---

## Best Practices

### 1. Question Ordering
- Always start from 1
- No gaps (1, 2, 3... not 1, 3, 5)
- Sequential across sections

### 2. Answer Keys
- Required for all except writing
- Case doesn't matter ("Engineering" = "engineering")
- Use exact format for multiple choice ("A", not "a" or "Option A")

### 3. Passage Text
- Include full text with paragraph markers
- Use "A\n", "B\n" for paragraph labels
- Keep original formatting

### 4. Test Types
- Listening: Requires audio_url
- Reading: Requires passage_text per section
- Writing: 2 tasks, no audio/passage

---

## Advanced Usage

### Batch Import Multiple Tests
```bash
for file in tests/*.json; do
  echo "Importing $file..."
  curl -X POST /api/tracks/import-from-ai -d @"$file"
done
```

### Update Existing Test
1. Export as JSON
2. Modify
3. Delete old
4. Import new

### Validate Multiple Files
```bash
for file in tests/*.json; do
  echo "Validating $file..."
  curl -X POST /api/tracks/validate-detailed -d @"$file" | jq '.valid'
done
```
```

**Deliverable:** AI import guide (30+ pages)

### Task 6.3: Admin User Manual

**Action:** Write manual for admin users

**File:** `/app/docs/ADMIN_MANUAL.md`

**Content:**
```markdown
# Admin User Manual

## Getting Started

### Login
1. Go to `/admin/login`
2. Enter admin credentials
3. Click "Login"

### Dashboard Overview
- Test Management: Create and manage tests
- Question Management: Add/edit questions
- Student Management: View students and submissions
- Submissions: Review and grade submissions

---

## Creating Tests

### Method 1: AI Import (Recommended)

**When to Use:**
- You have IELTS questions in PDF
- Creating complete tests (40 questions)
- Need consistent formatting

**Steps:**
1. See `/app/docs/AI_IMPORT_GUIDE.md`
2. Use DeepSeek to generate JSON
3. Import via API or admin UI

**Advantages:**
- Fast (5-10 minutes for full test)
- Accurate type detection
- Validated format

---

### Method 2: Manual Creation

**When to Use:**
- Creating custom questions
- Small number of questions
- Need complete control

**Steps:**
1. Go to "Test Management"
2. Click "Create Test"
3. Fill in:
   - Test title
   - Description
   - Duration (minutes)
   - Test type (Listening/Reading/Writing)
4. Click "Create"
5. Add sections and questions

---

## Managing Questions

### Adding Questions

1. **Select Test**
   - Go to Test Management
   - Click test name

2. **Choose Section**
   - Click section (1, 2, 3, or 4)
   - Click "Add Question"

3. **Select Question Type**
   - Choose from dropdown
   - See type descriptions

4. **Fill Question Form**
   Fields vary by type:
   
   **Common Fields:**
   - Question number (auto-assigned)
   - Question text/prompt
   - Correct answer
   
   **Type-Specific Fields:**
   - Options (multiple choice)
   - Word limit (completion questions)
   - Images (map/diagram questions)
   - etc.

5. **Save Question**
   - Review fields
   - Click "Save"

### Editing Questions

1. Find question in list
2. Click "Edit" icon
3. Modify fields
4. Click "Update"

### Deleting Questions

⚠️ **Warning:** This permanently deletes the question

1. Find question
2. Click "Delete" icon
3. Confirm deletion

**Note:** Remaining questions automatically re-index

---

## Question Type Guide

### Listening Types (10)

#### 1. Fill in the Gaps
**Use For:** Single blank, short answer
**Example:** "The student will study _____ at university."
**Fields:**
- Question text (with _____)
- Answer key
- Max words (default: 3)

[... descriptions for all 24 types ...]

---

## Publishing Tests

### Before Publishing Checklist
- ✅ All questions added
- ✅ Correct answers verified
- ✅ Question count correct (40 for L/R, 2 for W)
- ✅ Audio uploaded (for listening)
- ✅ Passages included (for reading)

### Publishing Steps
1. Go to Test Management
2. Find test
3. Click "Publish"
4. Test becomes visible to students

### Unpublishing
- Click "Unpublish"
- Test hidden from students
- Existing submissions retained

---

## Managing Submissions

### Viewing Submissions

1. Go to "Submissions"
2. See all student submissions
3. Filter by:
   - Test
   - Student
   - Date range
   - Score range

### Reviewing Answers

1. Click submission row
2. See student answers
3. Compare with correct answers
4. Color-coded:
   - Green = Correct
   - Red = Incorrect
   - Gray = Not answered

### Manual Grading (Writing)

**For Writing Tests:**
1. Open submission
2. Read student's essay
3. Enter score (0-100)
4. Add comments (optional)
5. Click "Save Score"

### Publishing Results

**Option 1: Publish Individual**
- Open submission
- Click "Publish Result"
- Student sees score

**Option 2: Bulk Publish**
- Select multiple submissions
- Click "Publish Selected"
- All selected results published

### Exporting Data

**Export Submissions:**
- Click "Export CSV"
- Downloads spreadsheet with:
  - Student names
  - Scores
  - Dates
  - Answers

---

## Student Management

### Viewing Students

1. Go to "Student Management"
2. See all registered students
3. Info shown:
   - Name
   - Email
   - Institution
   - Submission count
   - Join date

### Student Actions

**View Submissions:**
- Click student name
- See all their submissions

**Delete Student:**
- Click "Delete" icon
- Confirm deletion
- ⚠️ All submissions deleted too

---

## Best Practices

### Test Creation
1. Start with AI import if possible
2. Verify all questions after import
3. Test yourself before publishing
4. Keep answer keys secure

### Question Quality
1. Clear, unambiguous prompts
2. Correct answer keys
3. Appropriate difficulty
4. Realistic IELTS format

### Grading
1. Review auto-graded results
2. Check for edge cases
3. Manual grade writing promptly
4. Publish results within 24-48 hours

### Student Communication
1. Announce new tests
2. Set clear deadlines
3. Provide feedback
4. Respond to queries

---

## Troubleshooting

[Common admin issues and solutions]
```

**Deliverable:** Admin manual (25+ pages)

### Task 6.4: API Documentation

**Action:** Document all endpoints

**File:** `/app/docs/API_REFERENCE.md`

**Content:**
```markdown
# API Reference

## Base URL
```
http://localhost:8001/api
```

## Authentication
Most admin endpoints require authentication via session cookie.

---

## AI Import Endpoints

### Validate Import
Validate JSON without creating anything

**Endpoint:** `POST /api/tracks/validate-detailed`

**Request Body:**
```json
{
  "test_type": "reading",
  "title": "...",
  "sections": [...]
}
```

**Response (Success):**
```json
{
  "valid": true,
  "statistics": {...},
  "warnings": null,
  "normalized_data": {...}
}
```

**Response (Error):**
```json
{
  "valid": false,
  "errors": [
    {
      "field": "sections.0.questions.0.type",
      "message": "Invalid type",
      "help": "..."
    }
  ]
}
```

---

### Import Test
Create test from JSON

**Endpoint:** `POST /api/tracks/import-from-ai`

**Request Body:** Same as validate

**Response:**
```json
{
  "success": true,
  "track_id": "...",
  "exam_id": "...",
  "statistics": {...}
}
```

---

[Document all endpoints: exams, questions, submissions, etc.]
```

**Deliverable:** API reference (20+ pages)

## Phase 6 Success Criteria
- ✅ Question type reference complete (all 24 types)
- ✅ AI import guide complete with examples
- ✅ Admin manual complete with screenshots
- ✅ API documentation complete
- ✅ All docs reviewed and tested

## Phase 6 Outputs
1. `QUESTION_TYPE_REFERENCE.md` (50+ pages)
2. `AI_IMPORT_GUIDE.md` (30+ pages)
3. `ADMIN_MANUAL.md` (25+ pages)
4. `API_REFERENCE.md` (20+ pages)
5. Total: 125+ pages of documentation

---

# 📍 PHASE 7: TESTING & VALIDATION

**Duration:** 4-5 hours  
**Priority:** High  
**Dependencies:** Phases 1-6 complete

## Objectives
- Test all 24 question types end-to-end
- Validate import with real IELTS questions
- Test student experience
- Test admin workflows

## Tasks

### Task 7.1: Backend API Testing

**Action:** Test all import scenarios

**Test Cases:**

1. **Individual Type Import (24 tests)**
   ```bash
   # Test each question type individually
   for type in templates/question_types/listening/*.json; do
     echo "Testing $type..."
     curl -X POST /api/tracks/validate-detailed -d @"$type"
   done
   
   for type in templates/question_types/reading/*.json; do
     curl -X POST /api/tracks/validate-detailed -d @"$type"
   done
   
   for type in templates/question_types/writing/*.json; do
     curl -X POST /api/tracks/validate-detailed -d @"$type"
   done
   ```

2. **Complete Test Import (3 tests)**
   ```bash
   # Import complete test samples
   curl -X POST /api/tracks/import-from-ai \
     -d @templates/question_types/complete_tests/sample_listening_test_40q.json
   
   curl -X POST /api/tracks/import-from-ai \
     -d @templates/question_types/complete_tests/sample_reading_test_40q.json
   
   curl -X POST /api/tracks/import-from-ai \
     -d @templates/question_types/complete_tests/sample_writing_test_2tasks.json
   ```

3. **User's Original JSON**
   ```bash
   # Test the JSON provided in the initial request
   curl -X POST /api/tracks/import-from-ai \
     -d @user_provided_reading_test.json
   ```

4. **Error Handling Tests**
   - Invalid type names
   - Missing required fields
   - Malformed JSON
   - Wrong question counts
   - Duplicate indices

**Deliverable:** Backend test report

### Task 7.2: Frontend Rendering Testing

**Action:** Verify all question types display correctly

**Test Process:**

1. **Take Question Type Preview Test**
   - Login as student
   - Start "Question Type Preview" test
   - For each of 24 questions:
     - Screenshot the rendered question
     - Test interaction (click, type, select)
     - Verify answer saves
     - Check navigation

2. **Component Validation Checklist**
   For each question type:
   - [ ] Component renders without errors
   - [ ] Question number displays (1, 2, 3...)
   - [ ] Question text/prompt shows correctly
   - [ ] Input controls appear (text field, radio, checkbox, dropdown)
   - [ ] Placeholder text appropriate
   - [ ] Can enter/select answer
   - [ ] Answer persists when navigating away and back
   - [ ] Validation works (word limits, required fields)
   - [ ] Styling consistent with design
   - [ ] Responsive on mobile
   - [ ] Accessibility (keyboard navigation, screen readers)

3. **Create Test Evidence**
   ```
   /test_evidence/
   ├── listening/
   │   ├── 01_fill_in_the_gaps.png
   │   ├── 02_fill_in_the_gaps_short_answers.png
   │   └── ...
   ├── reading/
   │   ├── 01_flowchart_completion.png
   │   ├── 02_true_false_not_given.png
   │   └── ...
   └── writing/
       ├── 01_writing_part_1.png
       └── 02_writing_part_2.png
   ```

**Deliverable:** Frontend test report with 24 screenshots

### Task 7.3: Auto-Grading Testing

**Action:** Verify grading logic for each type

**Test Cases:**

1. **Create Test Submission**
   ```javascript
   const testSubmission = {
     exam_id: "question-type-preview-test",
     answers: {
       1: "engineering",           // Correct
       2: "ENGINEERING",           // Correct (case insensitive)
       3: "Engineer",              // Incorrect (different word)
       4: "A",                     // Multiple choice correct
       5: "B",                     // Multiple choice incorrect
       6: "TRUE",                  // TRUE/FALSE correct
       7: "NOT GIVEN",             // T/F incorrect
       // ... test all variations
     }
   };
   ```

2. **Submit and Check Score**
   ```bash
   curl -X POST /api/submissions \
     -d @test_submission.json
   
   # Get submission
   curl /api/submissions/{submission_id}
   
   # Verify score calculation
   ```

3. **Edge Cases**
   - Extra spaces in answers
   - Different capitalization
   - Punctuation in answers
   - Partial matches
   - Multiple answer questions
   - Writing (should not be auto-graded)

**Grading Matrix:**

| Type | Grading Method | Case Sensitive | Accepts Variations |
|------|---------------|----------------|--------------------|
| fill_in_the_gaps | exact_match | No | Yes (minor spelling) |
| identifying_information_true_false_not_given | exact_match | No | No |
| sentence_completion_reading | exact_match | No | Yes (minor spelling) |
| multiple_choice_* | exact_match | Yes | No |
| matching_* | exact_match | Yes | No |
| writing_* | manual | N/A | N/A |

**Deliverable:** Auto-grading test report

### Task 7.4: End-to-End User Flow Testing

**Action:** Complete student journey

**Test Scenarios:**

**Scenario 1: Complete Listening Test**
1. Student registers
2. Student logs in
3. Student sees available tests
4. Student starts listening test
5. Audio plays
6. Student answers all 40 questions
7. Student submits
8. Student sees confirmation
9. Admin reviews submission
10. Admin publishes result
11. Student sees score in dashboard

**Scenario 2: Complete Reading Test**
1-11. Same as above but with reading test

**Scenario 3: Complete Writing Test**
1. Student starts writing test
2. Completes Task 1 (150+ words)
3. Completes Task 2 (250+ words)
4. Submits
5. Admin manually grades
6. Admin publishes score
7. Student sees score

**Scenario 4: AI Import to Student Submission**
1. Admin generates JSON with DeepSeek
2. Admin validates JSON
3. Admin imports test
4. Test appears in admin panel
5. Admin publishes test
6. Student sees new test
7. Student completes test
8. Admin reviews
9. Admin publishes results
10. Student sees score

**Deliverable:** E2E test report with flow diagrams

### Task 7.5: Performance Testing

**Action:** Test system under load

**Tests:**

1. **Import Performance**
   - Import 10 tests simultaneously
   - Measure time per test
   - Check for errors

2. **Rendering Performance**
   - Load test with 40 questions
   - Measure page load time
   - Check rendering speed

3. **Submission Performance**
   - Submit 100 tests
   - Measure response time
   - Check database performance

**Deliverable:** Performance test report

### Task 7.6: Cross-Browser Testing

**Action:** Test on multiple browsers

**Browsers:**
- Chrome (latest)
- Firefox (latest)
- Safari (latest)
- Edge (latest)
- Mobile Safari (iOS)
- Mobile Chrome (Android)

**Test:**
- Test rendering
- Test interactions
- Test submissions

**Deliverable:** Browser compatibility report

## Phase 7 Success Criteria
- ✅ All 24 types tested individually
- ✅ Complete tests imported successfully
- ✅ Frontend renders all types correctly
- ✅ Auto-grading works correctly
- ✅ E2E flows completed successfully
- ✅ Performance acceptable
- ✅ Cross-browser compatible

## Phase 7 Outputs
1. Backend test report
2. Frontend test report with screenshots
3. Auto-grading test report
4. E2E test report
5. Performance test report
6. Browser compatibility report
7. Consolidated test summary

---

# 📍 PHASE 8: PRODUCTION DEPLOYMENT

**Duration:** 2 hours  
**Priority:** Medium  
**Dependencies:** All phases complete

## Objectives
- Package all deliverables
- Create deployment checklist
- Document system for future maintainers
- Create handoff materials

## Tasks

### Task 8.1: Create Release Package

**Action:** Organize all deliverables

**Directory Structure:**
```
/app/releases/qti_question_system_v1.0/
├── README.md
├── CHANGELOG.md
├── DEPLOYMENT_GUIDE.md
├── templates/
│   ├── question_types/         # 24 JSON templates
│   ├── complete_tests/          # 3 sample tests
│   └── README.md
├── ai_prompts/
│   ├── MASTER_PROMPT.md
│   ├── DEEPSEEK_CHEATSHEET.md
│   ├── listening/               # 10 prompts
│   ├── reading/                 # 12 prompts
│   └── writing/                 # 2 prompts
├── docs/
│   ├── QUESTION_TYPE_REFERENCE.md
│   ├── AI_IMPORT_GUIDE.md
│   ├── ADMIN_MANUAL.md
│   ├── API_REFERENCE.md
│   └── TROUBLESHOOTING.md
├── tests/
│   ├── backend_tests/
│   ├── frontend_tests/
│   └── test_evidence/           # Screenshots
└── scripts/
    ├── validate_all_templates.sh
    ├── import_all_samples.sh
    └── check_integration.sh
```

**Deliverable:** Organized release package

### Task 8.2: Create Master README

**Action:** Write comprehensive README for the system

**File:** `/app/releases/qti_question_system_v1.0/README.md`

**Content:**
```markdown
# IELTS QTI Question System v1.0

Complete question management system supporting all 24 QTI question types.

## What's Included

- ✅ 24 validated JSON templates
- ✅ 3 complete sample tests (Listening, Reading, Writing)
- ✅ DeepSeek AI prompts for automatic conversion
- ✅ Complete documentation (125+ pages)
- ✅ Backend validation with auto-normalization
- ✅ Frontend components for all types
- ✅ Admin management interface
- ✅ Comprehensive test suite

## Quick Links

- [Getting Started](#getting-started)
- [Question Type Reference](docs/QUESTION_TYPE_REFERENCE.md)
- [AI Import Guide](docs/AI_IMPORT_GUIDE.md)
- [Admin Manual](docs/ADMIN_MANUAL.md)
- [API Reference](docs/API_REFERENCE.md)

## Getting Started

### For DeepSeek Users (AI Import)

1. **Get Question Text**
   - Extract from PDF
   - Copy question text

2. **Generate JSON**
   - Use prompt from `ai_prompts/MASTER_PROMPT.md`
   - Paste into DeepSeek
   - Copy generated JSON

3. **Validate**
   ```bash
   curl -X POST /api/tracks/validate-detailed -d @test.json
   ```

4. **Import**
   ```bash
   curl -X POST /api/tracks/import-from-ai -d @test.json
   ```

5. **Publish**
   - Login to admin
   - Find test
   - Click "Publish"

### For Manual Creation

See [Admin Manual](docs/ADMIN_MANUAL.md)

## System Architecture

```
┌─────────────────┐
│   DeepSeek AI   │ → Generates JSON from PDF
└────────┬────────┘
         │
         ↓
┌─────────────────┐
│  Validation API │ → Validates & normalizes
└────────┬────────┘
         │
         ↓
┌─────────────────┐
│   Import API    │ → Creates exam in DB
└────────┬────────┘
         │
         ↓
┌─────────────────┐
│  Admin Panel    │ → Manage & publish
└────────┬────────┘
         │
         ↓
┌─────────────────┐
│ Student Portal  │ → Take test
└─────────────────┘
```

## Question Types Supported

### Listening (10)
1. Fill in the Gaps
2. Fill in the Gaps (Short Answers)
3. Flowchart Completion
4. Form Completion
5. Labelling on a Map
6. Matching
7. Multiple Choice (More than One)
8. Multiple Choice (One Answer)
9. Sentence Completion
10. Table Completion

### Reading (12)
1. Flowchart Completion (Selecting Words)
2. Identifying Information (TRUE/FALSE/NOT GIVEN)
3. Matching Features
4. Matching Headings
5. Matching Sentence Endings
6. Multiple Choice (More than One)
7. Multiple Choice (One Answer)
8. Note Completion
9. Sentence Completion
10. Summary Completion (Selecting from List)
11. Summary Completion (Selecting Words from Text)
12. Table Completion

### Writing (2)
1. Writing Part 1 (Chart/Graph Description)
2. Writing Part 2 (Essay)

## File Organization

- `templates/` - Copy-paste ready JSON templates
- `ai_prompts/` - DeepSeek conversion prompts
- `docs/` - Complete documentation
- `tests/` - Test data and evidence
- `scripts/` - Utility scripts

## Troubleshooting

See [docs/TROUBLESHOOTING.md](docs/TROUBLESHOOTING.md)

## Support

- Documentation: `/docs/`
- Examples: `/templates/`
- Test Data: `/tests/`

## Version History

See [CHANGELOG.md](CHANGELOG.md)
```

**Deliverable:** Master README

### Task 8.3: Create Changelog

**Action:** Document all changes

**File:** `/app/releases/qti_question_system_v1.0/CHANGELOG.md`

**Content:**
```markdown
# Changelog

## v1.0.0 - 2025-01-XX

### Added
- Complete support for 24 QTI question types
- AI import system with DeepSeek integration
- 24 validated JSON templates
- 3 complete sample tests
- Master prompt for AI conversion
- 24 type-specific prompts
- Comprehensive documentation (125+ pages)
- Backend validation with auto-normalization
- Frontend QTI component integration
- Question type preview test
- Validation preview endpoint

### Changed
- Updated backend to accept legacy type names
- Enhanced error messages with suggestions
- Improved auto-grading logic
- Redesigned admin question creation UI

### Fixed
- Type name validation issues
- Options format handling
- Duplicate default clause in ListeningTest
- Component integration gaps

### Documentation
- Question Type Reference (50 pages)
- AI Import Guide (30 pages)
- Admin Manual (25 pages)
- API Reference (20 pages)
- DeepSeek Quick Reference

### Testing
- Backend API tests (24 types)
- Frontend rendering tests (24 screenshots)
- Auto-grading tests
- E2E flow tests
- Performance tests
- Cross-browser tests

### Known Issues
- None

### Breaking Changes
- None (backward compatible)
```

**Deliverable:** Changelog

### Task 8.4: Create Deployment Guide

**Action:** Write deployment instructions

**File:** `/app/releases/qti_question_system_v1.0/DEPLOYMENT_GUIDE.md`

**Content:**
```markdown
# Deployment Guide

## Prerequisites

- Node.js 16+
- Python 3.9+
- MongoDB 4.4+
- Yarn package manager

## Installation

### 1. Backend Setup

```bash
cd /app/backend
pip install -r requirements.txt
```

### 2. Frontend Setup

```bash
cd /app/frontend
yarn install
```

### 3. Environment Variables

Already configured in:
- `/app/backend/.env`
- `/app/frontend/.env`

### 4. Services

```bash
# Start all services
sudo supervisorctl start all

# Check status
sudo supervisorctl status
```

## Verification

### 1. Backend Health Check

```bash
curl http://localhost:8001/api/
```

Expected: `{"status": "ok"}`

### 2. Frontend Access

Open: `http://localhost:3000`

Expected: Homepage loads

### 3. Import Sample Test

```bash
curl -X POST http://localhost:8001/api/tracks/import-from-ai \
  -H "Content-Type: application/json" \
  -d @/app/releases/qti_question_system_v1.0/templates/complete_tests/sample_reading_test_40q.json
```

Expected: Success message

### 4. Admin Login

1. Go to `/admin/login`
2. Login with admin credentials
3. Verify test appears

## Configuration

### Add New Admin

Edit `/app/backend/middleware/auth.py`:
```python
ADMIN_EMAILS = [
    "admin@example.com",
    "your_email@example.com"  # Add here
]
```

### Change Test Duration Limits

Edit `/app/backend/ai_import_service.py`:
```python
duration_seconds: int = Field(..., ge=60, le=7200)
# Change 7200 to desired max seconds
```

### Add New Question Type

1. Create component in `/app/frontend/src/components/qti/[category]/`
2. Add to backend validation in `/app/backend/ai_import_service.py`
3. Add to test interface switch statement
4. Create template in `/app/templates/question_types/`
5. Add to documentation

## Maintenance

### Database Backup

```bash
mongodump --out /backup/$(date +%Y%m%d)
```

### Clear Logs

```bash
find /var/log/supervisor -type f -name "*.log" -mtime +7 -delete
```

### Update Dependencies

```bash
# Backend
cd /app/backend
pip install --upgrade -r requirements.txt

# Frontend
cd /app/frontend
yarn upgrade
```

## Monitoring

### Check Service Status

```bash
sudo supervisorctl status
```

### View Logs

```bash
# Backend
tail -f /var/log/supervisor/backend.out.log

# Frontend
tail -f /var/log/supervisor/frontend.out.log
```

### Monitor Performance

```bash
# Check resource usage
htop

# Check database
mongo
> show dbs
> use ielts_db
> db.stats()
```

## Troubleshooting

See [docs/TROUBLESHOOTING.md](docs/TROUBLESHOOTING.md)
```

**Deliverable:** Deployment guide

### Task 8.5: Create Handoff Document

**Action:** Document for future maintainers

**File:** `/app/releases/qti_question_system_v1.0/MAINTAINER_GUIDE.md`

**Content:**
```markdown
# Maintainer Guide

## System Overview

This system manages IELTS exam questions with support for 24 question types across 3 categories (Listening, Reading, Writing).

## Key Components

### Backend (`/app/backend/`)
- `server.py` - Main FastAPI application
- `ai_import_service.py` - Import validation and creation
- `auth_service.py` - Authentication
- `init_*_test.py` - Test initialization scripts

### Frontend (`/app/frontend/`)
- `src/components/ListeningTest.jsx` - Listening test interface
- `src/components/ReadingTest.jsx` - Reading test interface
- `src/components/WritingTest.jsx` - Writing test interface
- `src/components/qti/` - Question type components (24 total)

### Templates (`/app/templates/`)
- `question_types/` - JSON templates for each type
- `ai_prompts/` - DeepSeek conversion prompts

### Documentation (`/app/docs/`)
- Complete guides and references

## Common Tasks

### Adding New Question Type

[Step-by-step instructions]

### Modifying Existing Type

[Step-by-step instructions]

### Updating Validation Rules

[Step-by-step instructions]

### Changing Grading Logic

[Step-by-step instructions]

## Code Structure

### Backend Validation Flow

```
Request → Pydantic Model → Validators → Normalizers → Database
```

### Frontend Rendering Flow

```
Load Exam → Parse Questions → renderQuestionComponent → QTI Component → Display
```

## Important Files

| File | Purpose | Edit When |
|------|---------|-----------|
| `ai_import_service.py` | Import validation | Adding types, changing validation |
| `ReadingTest.jsx` | Reading UI | Adding reading components |
| `ListeningTest.jsx` | Listening UI | Adding listening components |
| `QUESTION_TYPE_REFERENCE.md` | Type docs | Documenting types |

## Testing

### Run Backend Tests
```bash
pytest /app/backend/tests/
```

### Run Frontend Tests
```bash
cd /app/frontend
yarn test
```

### Manual Testing
1. Import sample tests
2. Take test as student
3. Review in admin
4. Check grading

## Deployment

### Production Checklist
- [ ] All tests passing
- [ ] Documentation updated
- [ ] Database backed up
- [ ] Environment variables set
- [ ] Services configured
- [ ] Logs monitored

### Rollback Procedure
1. Stop services
2. Restore database backup
3. Checkout previous git commit
4. Restart services

## Contact

For questions or issues, contact:
- Technical Lead: [name@email.com]
- Documentation: See `/app/docs/`
```

**Deliverable:** Maintainer guide

### Task 8.6: Final Verification

**Action:** Complete final checklist

**Checklist:**
- [ ] All 24 templates created and validated
- [ ] All 24 prompts created
- [ ] All documentation complete
- [ ] Backend accepts all type variations
- [ ] Frontend renders all types
- [ ] Tests passing
- [ ] Sample tests import successfully
- [ ] User's original JSON imports successfully
- [ ] Release package organized
- [ ] README complete
- [ ] Changelog complete
- [ ] Deployment guide complete
- [ ] Maintainer guide complete

**Deliverable:** Final verification report

## Phase 8 Success Criteria
- ✅ Release package complete and organized
- ✅ All documentation finalized
- ✅ Deployment guide tested
- ✅ Final checklist 100% complete
- ✅ System production-ready

## Phase 8 Outputs
1. Complete release package
2. Master README
3. Changelog
4. Deployment guide
5. Maintainer guide
6. Final verification report

---

# 🎯 EXECUTION INSTRUCTIONS

## How to Use This Plan

### For You (User)
**Command format:**
```
"Please start Phase [number]"
or
"Please start Phase [number], Task [number]"
```

**Examples:**
- "Please start Phase 1" - Executes all of Phase 1
- "Please start Phase 2, Task 2.1" - Executes just Task 2.1
- "Please continue Phase 3" - Continues from where you left off
- "Please skip to Phase 4" - Jumps to Phase 4

### For Agent (Next Agent)
When user says "Please start Phase X":

1. **Read this document section for Phase X**
2. **Follow tasks sequentially**
3. **Create deliverables as specified**
4. **Update phase status in this document**
5. **Report completion with summary**

### Phase Status Tracking

Update this table as phases complete:

| Phase | Status | Started | Completed | Notes |
|-------|--------|---------|-----------|-------|
| 1 | ⏳ Pending | - | - | - |
| 2 | ⏳ Pending | - | - | - |
| 3 | ⏳ Pending | - | - | - |
| 4 | ⏳ Pending | - | - | - |
| 5 | ⏳ Pending | - | - | - |
| 6 | ⏳ Pending | - | - | - |
| 7 | ⏳ Pending | - | - | - |
| 8 | ⏳ Pending | - | - | - |

---

# 📊 SUCCESS METRICS

## Completion Criteria

### System Complete When:
- ✅ All 24 question types have templates
- ✅ All 24 types render correctly in frontend
- ✅ Backend accepts all format variations
- ✅ DeepSeek can generate valid JSON
- ✅ User's original JSON imports successfully
- ✅ Complete documentation exists
- ✅ All tests passing

### Production Ready When:
- ✅ 100+ real questions imported
- ✅ 10+ complete tests created
- ✅ 100+ students can take tests
- ✅ Auto-grading working
- ✅ Admin can manage everything
- ✅ No critical bugs

---

# 🚀 NEXT STEPS

**You said you want to start execution.**

Please confirm:
1. Start with Phase 1?
2. Or specific phase you want first?
3. Any modifications to the plan?

**When ready, simply say:**
- "Please start Phase 1" - I'll begin immediately
- "Please start Phase X" - I'll jump to that phase
- "Modify the plan first" - We'll discuss changes

I'm ready to execute! 🎯