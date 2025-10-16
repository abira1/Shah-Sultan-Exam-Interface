# Question Type Templates - Usage Guide

**Phase 2 - AI-Ready JSON Templates**  
**Created:** January 2025  
**Purpose:** Complete template library for all 24 QTI question types

---

## Table of Contents
1. [Quick Start](#quick-start)
2. [Template Categories](#template-categories)
3. [Field Reference](#field-reference)
4. [Validation Rules](#validation-rules)
5. [Common Issues](#common-issues)
6. [Advanced Usage](#advanced-usage)

---

## Quick Start

### For AI Tools (DeepSeek, ChatGPT, etc.)
1. Choose template for your question type from `listening/`, `reading/`, or `writing/`
2. Copy template content as base structure  
3. Replace example values with your actual question data
4. Ensure all required fields are filled
5. Test with validation endpoint before importing

### For Manual Creation
1. Browse templates to understand question type structure
2. Use complete test examples as reference for full tests
3. Validate JSON syntax and required fields
4. Import using `/api/tracks/import-from-ai` endpoint

### Validation & Import Workflow
```bash
# 1. Validate your JSON
curl -X POST /api/tracks/validate-detailed \
  -H "Content-Type: application/json" \
  -d @your_test.json

# 2. Import if validation passes  
curl -X POST /api/tracks/import-from-ai \
  -H "Content-Type: application/json" \
  -d @your_test.json
```

---

## Template Categories

### 📻 Listening (10 types)

| File | Question Type | Use Case |
|------|--------------|----------|
| `01_fill_in_the_gaps.json` | Single blank, short answer | Section 1, factual information |
| `02_fill_in_the_gaps_short_answers.json` | Multiple blanks in passage | Section 1, form completion |
| `03_flowchart_completion_listening.json` | Complete flowchart from audio | Section 2/4, processes |
| `04_form_completion.json` | Fill in form fields | Section 1, personal information |
| `05_labelling_on_a_map.json` | Label locations on map | Section 2, directions |
| `06_matching_listening.json` | Match items from audio | Section 2/3, opinions/features |
| `07_multiple_choice_more_than_one_answer_listening.json` | Choose 2+ answers | Section 2/3/4, features |
| `08_multiple_choice_one_answer_listening.json` | Choose 1 answer | All sections, various topics |
| `09_sentence_completion_listening.json` | Complete sentences from audio | Section 1/3/4, specific info |
| `10_table_completion_listening.json` | Fill in table cells | Section 2/4, organized info |

### 📚 Reading (12 types)

| File | Question Type | Use Case |
|------|--------------|----------|
| `01_flowchart_completion_selecting_words_from_text.json` | Complete flowchart with passage words | All passages, processes |
| `02_identifying_information_true_false_not_given.json` | TRUE/FALSE/NOT GIVEN | All passages, factual accuracy |
| `03_matching_features.json` | Match features to descriptions | Passage 2/3, people/places |
| `04_matching_headings.json` | Match paragraph headings | All passages, main ideas |
| `05_matching_sentence_endings.json` | Complete sentences by matching | Passage 2/3, sentence completion |
| `06_multiple_choice_more_than_one_answer_reading.json` | Choose 2+ answers | Passage 2/3, multiple features |
| `07_multiple_choice_one_answer_reading.json` | Choose 1 answer | All passages, various topics |
| `08_note_completion.json` | Complete notes/summary | All passages, key information |
| `09_sentence_completion_reading.json` | Complete sentences from passage | All passages, specific details |
| `10_summary_completion_selecting_from_list.json` | Complete summary from word list | Passage 2/3, guided completion |
| `11_summary_completion_selecting_words_from_text.json` | Complete summary from passage | All passages, free completion |
| `12_table_completion_reading.json` | Fill in table from passage | All passages, organized data |

### ✍️ Writing (2 types)

| File | Question Type | Use Case |
|------|--------------|----------|
| `01_writing_part_1.json` | Chart/diagram description (150+ words) | Task 1, visual information |
| `02_writing_part_2.json` | Essay writing (250+ words) | Task 2, argumentation |

### 🧪 Complete Test Examples

| File | Description | Questions |
|------|-------------|-----------|
| `sample_listening_test_40q.json` | Full listening test with all 10 types | 40 questions |
| `sample_reading_test_40q.json` | Full reading test with all 12 types | 40 questions |
| `sample_writing_test_2tasks.json` | Complete writing test | 2 tasks |

---

## Field Reference

### Universal Fields (Required for ALL question types)
```json
{
  "index": 1,                    // Question number (sequential 1-40)
  "type": "question_type_name",  // Exact QTI type name
  "prompt": "Question text",     // Question/instruction text
  "answer_key": "answer"        // Correct answer (null for writing)
}
```

### Test Structure Fields
```json
{
  "test_type": "listening|reading|writing",  // Test category
  "title": "Test Title",                     // 3-200 characters
  "description": "Test description",        // 10-1000 characters  
  "duration_seconds": 3600,                 // 60-7200 seconds
  "audio_url": "https://...",               // Required for listening only
  "sections": [...]                         // 1-4 sections
}
```

### Section Structure Fields
```json
{
  "index": 1,                              // Section number (1-4)
  "title": "Section 1: Title",             // Section title
  "instructions": "Questions 1-10",        // Section instructions
  "passage_text": "Full passage...",      // Required for reading only
  "questions": [...]                       // Array of questions
}
```

### Type-Specific Optional Fields

#### Word Limits
```json
{
  "max_words": 3,        // Maximum words allowed (1-10)
  "min_words": 150       // Minimum words required (writing only)
}
```

#### Multiple Choice & Matching
```json
{
  "options": [           // Multiple choice options
    {"value": "A", "text": "Option text"},
    {"value": "B", "text": "Option text"}
  ],
  "headings": [          // For matching headings
    {"value": "i", "text": "Heading text"}
  ],
  "features": [          // For matching features
    {"value": "A", "text": "Feature text"}  
  ],
  "endings": [           // For sentence endings
    {"value": "A", "text": "Ending text"}
  ],
  "max_choices": 2       // For multiple answer questions
}
```

#### Word Banks & Lists
```json
{
  "word_list": ["word1", "word2", "word3"]  // For summary completion
}
```

#### Images & Media
```json
{
  "image_url": "https://...",     // Question image (maps, diagrams)
  "chart_image": "https://..."    // Chart for writing Task 1
}
```

#### Writing Specifics
```json
{
  "task_number": 1,               // Writing task number (1 or 2)
  "instructions": "Spend 20 minutes..."  // Additional instructions
}
```

---

## Validation Rules

### Question Type Validation
- **Must use exact type names** from the 24 QTI types
- **Case sensitive:** `fill_in_the_gaps` not `Fill_In_The_Gaps`
- **No abbreviations:** Use full type names

### Answer Key Requirements
```javascript
// Required for ALL except writing
"answer_key": "string" || ["array"] || null

// Format by type:
"fill_in_the_gaps": "engineering"                    // String
"multiple_choice_one_answer_*": "B"                  // Single letter
"multiple_choice_more_than_one_answer_*": ["B","D"]  // Array of letters  
"identifying_information_true_false_not_given": "TRUE"  // TRUE/FALSE/NOT GIVEN
"writing_part_1": null                               // Always null
"writing_part_2": null                               // Always null
```

### Sequential Question Indexing
- **Must start at 1:** First question is index 1, not 0
- **No gaps:** 1, 2, 3, 4... (not 1, 3, 5...)
- **No duplicates:** Each index used once only
- **Cross-section:** Continue numbering across sections

### Test Type Specific Rules

#### Listening Tests
```json
{
  "test_type": "listening",
  "audio_url": "https://...",    // Required
  "duration_seconds": 2004,      // Typical: ~33 minutes
  "sections": 4                  // Typically 4 sections
}
```

#### Reading Tests  
```json
{
  "test_type": "reading",
  "audio_url": null,             // Must be null
  "duration_seconds": 3600,      // Typically 60 minutes
  "passage_text": "..."         // Required in each section
}
```

#### Writing Tests
```json
{
  "test_type": "writing", 
  "audio_url": null,             // Must be null
  "duration_seconds": 3600,      // Typically 60 minutes
  "sections": 2,                 // Always 2 sections
  "min_words": 150/250          // Task 1: 150, Task 2: 250
}
```

---

## Common Issues

### ❌ Issue 1: Invalid Question Type
**Error:** `Invalid question type: 'true_false'`
**Fix:** Use full name: `identifying_information_true_false_not_given`
**Prevention:** Copy exact type names from templates

### ❌ Issue 2: Wrong Options Format
**Error:** `Input should be a valid dictionary`
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

### ❌ Issue 3: Missing Answer Key
**Error:** `answer_key is required`
**Fix:** Add answer_key for all except `writing_part_1` and `writing_part_2`
```json
{
  "type": "sentence_completion_reading",
  "answer_key": "required for this type"
}
```

### ❌ Issue 4: Sequential Index Gaps
**Error:** `Duplicate question indices`
**Wrong:** Questions numbered 1, 3, 5, 7...
**Correct:** Questions numbered 1, 2, 3, 4...

### ❌ Issue 5: Audio URL for Non-Listening
**Error:** `audio_url should be null for reading/writing`
**Fix:**
```json
{
  "test_type": "reading",
  "audio_url": null     // Must be null for non-listening
}
```

### ❌ Issue 6: Missing Passage Text
**Error:** `passage_text required for reading sections`
**Fix:**
```json
{
  "test_type": "reading",
  "sections": [
    {
      "passage_text": "Full passage text here..."  // Required
    }
  ]
}
```

---

## Advanced Usage

### Batch Import Multiple Tests
```bash
for file in tests/*.json; do
  echo "Importing $file..."
  curl -X POST /api/tracks/import-from-ai \
    -H "Content-Type: application/json" \
    -d @"$file"
done
```

### Validate Multiple Files
```bash
for file in tests/*.json; do
  echo "Validating $file..."
  curl -X POST /api/tracks/validate-detailed \
    -H "Content-Type: application/json" \
    -d @"$file" | jq '.valid'
done
```

### Template Customization
1. **Copy base template** for your question type
2. **Modify example content** with your questions
3. **Keep field structure** exactly as shown
4. **Validate before import** to catch errors early

### Creating Custom Complete Tests
1. **Start with complete test example** 
2. **Replace questions** with your content
3. **Maintain question indexing** (1, 2, 3...)
4. **Keep section structure** consistent
5. **Test each section** separately if needed

---

## Template File Structure

```
/app/templates/question_types/
├── README.md                    # This guide
├── listening/                   # 10 listening templates
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
├── reading/                     # 12 reading templates
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
├── writing/                     # 2 writing templates
│   ├── 01_writing_part_1.json
│   └── 02_writing_part_2.json
└── complete_tests/              # 3 complete examples
    ├── sample_listening_test_40q.json
    ├── sample_reading_test_40q.json
    └── sample_writing_test_2tasks.json
```

---

## Support & Resources

### Documentation
- **Backend Validation:** `/app/docs/BACKEND_VALIDATION_REFERENCE.md`
- **Frontend Components:** `/app/docs/COMPONENT_INVENTORY_REPORT.md`
- **JSON Structure:** `/app/docs/JSON_STRUCTURE_STANDARD.md`

### Validation Endpoints
- **Preview:** `POST /api/tracks/validate-detailed`
- **Import:** `POST /api/tracks/import-from-ai`
- **List Tracks:** `GET /api/tracks`

### Quick Reference
- **24 Question Types:** All supported with templates
- **Legacy Support:** Automatic conversion from old type names
- **Auto-Grading:** All types except writing are auto-graded
- **Manual Grading:** Writing tasks require admin review

This template library provides everything needed to create comprehensive IELTS tests with all 24 QTI question types. Each template includes detailed documentation, validation rules, and working examples to ensure successful imports.