# JSON Structure Standard - AI Import Templates

**Phase 2 - AI-Ready JSON Templates**  
**Created:** January 2025  
**Purpose:** Define universal JSON format for all 24 QTI question types

---

## Table of Contents
1. [Overview](#overview)
2. [Standard JSON Structure](#standard-json-structure)
3. [Field Specifications](#field-specifications)
4. [Validation Rules](#validation-rules)
5. [Question Type Categories](#question-type-categories)
6. [Examples by Test Type](#examples-by-test-type)

---

## Overview

This document defines the universal JSON format that DeepSeek AI and other tools should generate when converting IELTS questions from PDFs. The format is optimized for backend validation and supports all 24 QTI question types plus legacy compatibility.

### Design Principles
- **Universal Structure:** Same format for listening, reading, and writing
- **Type-Specific Flexibility:** Each question type can have custom payload fields
- **Validation-Ready:** Aligns with backend Pydantic models
- **AI-Friendly:** Clear, consistent patterns for AI generation
- **Future-Proof:** Extensible for new question types

---

## Standard JSON Structure

### Complete Template
```json
{
  "test_type": "listening|reading|writing",
  "title": "Test Title (3-200 characters)",
  "description": "Test Description (10-1000 characters)", 
  "duration_seconds": 3600,
  "audio_url": "https://..." || null,
  "sections": [
    {
      "index": 1,
      "title": "Section 1: Title",
      "instructions": "Questions 1-10",
      "passage_text": "Full passage text" || null,
      "questions": [
        {
          "index": 1,
          "type": "question_type_name",
          "prompt": "Question text",
          "answer_key": "correct_answer",
          "// ... type-specific fields below"
        }
      ]
    }
  ]
}
```

### Minimal Required Structure
```json
{
  "test_type": "reading",
  "title": "Test Title",
  "description": "Test description", 
  "duration_seconds": 3600,
  "sections": [
    {
      "index": 1,
      "title": "Section 1",
      "instructions": "Questions 1-13",
      "questions": [
        {
          "index": 1,
          "type": "sentence_completion_reading",
          "prompt": "Complete: The building was made of _____.",
          "answer_key": "stone"
        }
      ]
    }
  ]
}
```

---

## Field Specifications

### Root Level Fields

#### Required Fields
```json
{
  "test_type": "listening|reading|writing",    // Test category
  "title": "string (3-200 chars)",            // Test title
  "description": "string (10-1000 chars)",    // Test description
  "duration_seconds": "integer (60-7200)",    // Test duration
  "sections": "array (1-4 sections)"          // Test sections
}
```

#### Optional Fields
```json
{
  "audio_url": "string (valid URL)" || null   // Required for listening, null otherwise
}
```

### Section Level Fields

#### Required Fields
```json
{
  "index": "integer (1-4)",                   // Section number
  "title": "string (min 3 chars)",           // Section title
  "instructions": "string (min 5 chars)",    // Section instructions
  "questions": "array (1+ questions)"        // Questions in section
}
```

#### Optional Fields
```json
{
  "passage_text": "string (100+ chars)" || null  // Required for reading, null otherwise
}
```

### Question Level Fields

#### Universal Required Fields (All 24 Types)
```json
{
  "index": "integer (sequential 1-40)",      // Question number
  "type": "string (valid QTI type)",         // Question type name
  "prompt": "string (min 1 char)",           // Question text
  "answer_key": "any (except writing)" || null  // Correct answer
}
```

#### Type-Specific Optional Fields
```json
{
  // Word limits
  "max_words": "integer (1-10)",             // Max words allowed
  "min_words": "integer (50-500)",           // Min words required (writing)
  
  // Multiple choice
  "options": "array of objects",             // Choice options
  "max_choices": "integer (2-5)",            // Max selections
  
  // Matching questions
  "headings": "array of objects",            // Heading options
  "features": "array of objects",            // Feature options
  "endings": "array of objects",             // Sentence endings
  
  // Word banks
  "word_list": "array of strings",           // Available words
  
  // Images and media
  "image_url": "string (valid URL)",         // Question image
  "chart_image": "string (valid URL)",       // Chart for writing
  
  // Forms and structures
  "table_data": "object",                    // Table structure
  "form_fields": "array of objects",         // Form field definitions
  
  // Writing specifics
  "task_number": "integer (1-2)",           // Writing task number
  "instructions": "string"                   // Additional instructions
}
```

---

## Validation Rules

### Test Type Rules
```javascript
// Test type validation
test_type: {
  required: true,
  enum: ["listening", "reading", "writing"],
  description: "Must be one of the three valid test types"
}
```

### Duration Rules
```javascript
// Duration validation
duration_seconds: {
  required: true,
  minimum: 60,        // 1 minute minimum
  maximum: 7200,      // 2 hours maximum
  typical: {
    "listening": 2004,   // ~33 minutes (31:24 + 2 min review)
    "reading": 3600,     // 60 minutes
    "writing": 3600      // 60 minutes
  }
}
```

### Audio URL Rules
```javascript
// Audio URL validation
audio_url: {
  required_if: "test_type === 'listening'",
  format: "valid URL",
  null_if: "test_type !== 'listening'",
  examples: [
    "https://audio.jukehost.co.uk/...",
    "https://example.com/audio.mp3"
  ]
}
```

### Section Rules
```javascript
// Section validation
sections: {
  required: true,
  min_count: 1,
  max_count: 4,
  typical_counts: {
    "listening": 4,     // Sections 1-4
    "reading": 3,       // Passages 1-3  
    "writing": 2        // Tasks 1-2
  }
}
```

### Question Index Rules
```javascript
// Question indexing validation
question_indices: {
  required: "sequential starting from 1",
  no_gaps: true,
  no_duplicates: true,
  typical_ranges: {
    "listening": "1-40",    // 40 questions
    "reading": "1-40",      // 40 questions
    "writing": "1-2"        // 2 tasks
  }
}
```

### Answer Key Rules
```javascript
// Answer key validation by type
answer_key: {
  required_except: ["writing_part_1", "writing_part_2"],
  formats: {
    "string": ["fill_in_the_gaps", "sentence_completion_*"],
    "array": ["fill_in_the_gaps_short_answers", "multiple_choice_more_than_one_*"],
    "null": ["writing_part_1", "writing_part_2"]
  }
}
```

---

## Question Type Categories

### Listening Types (10)
```json
{
  "fill_in_the_gaps": {
    "answer_format": "string",
    "optional_fields": ["max_words"],
    "typical_use": "Single blank completion"
  },
  "fill_in_the_gaps_short_answers": {
    "answer_format": "array",
    "optional_fields": ["max_words"],
    "typical_use": "Multiple blanks in passage"
  },
  "flowchart_completion_listening": {
    "answer_format": "string|array",
    "optional_fields": ["image_url", "max_words"],
    "typical_use": "Complete flowchart from audio"
  },
  "form_completion": {
    "answer_format": "string|array",
    "optional_fields": ["form_fields", "max_words"],
    "typical_use": "Fill in form fields"
  },
  "labelling_on_a_map": {
    "answer_format": "string",
    "optional_fields": ["image_url"],
    "typical_use": "Label locations on map"
  },
  "matching_listening": {
    "answer_format": "string",
    "optional_fields": ["features", "options"],
    "typical_use": "Match items from audio"
  },
  "multiple_choice_more_than_one_answer_listening": {
    "answer_format": "array",
    "required_fields": ["options"],
    "optional_fields": ["max_choices"],
    "typical_use": "Choose 2+ answers"
  },
  "multiple_choice_one_answer_listening": {
    "answer_format": "string",
    "required_fields": ["options"],
    "typical_use": "Choose 1 answer"
  },
  "sentence_completion_listening": {
    "answer_format": "string",
    "optional_fields": ["max_words"],
    "typical_use": "Complete sentences from audio"
  },
  "table_completion_listening": {
    "answer_format": "string|array",
    "optional_fields": ["table_data", "max_words"],
    "typical_use": "Fill in table cells"
  }
}
```

### Reading Types (12)
```json
{
  "flowchart_completion_selecting_words_from_text": {
    "answer_format": "string",
    "optional_fields": ["image_url", "max_words"],
    "typical_use": "Complete flowchart with passage words"
  },
  "identifying_information_true_false_not_given": {
    "answer_format": "string",
    "required_fields": ["options"],
    "options_format": [
      {"value": "TRUE", "text": "TRUE"},
      {"value": "FALSE", "text": "FALSE"},
      {"value": "NOT GIVEN", "text": "NOT GIVEN"}
    ],
    "typical_use": "TRUE/FALSE/NOT GIVEN questions"
  },
  "matching_features": {
    "answer_format": "string",
    "required_fields": ["features"],
    "typical_use": "Match features to descriptions"
  },
  "matching_headings": {
    "answer_format": "string", 
    "required_fields": ["headings"],
    "headings_format": [
      {"value": "i", "text": "Heading text"},
      {"value": "ii", "text": "Heading text"}
    ],
    "typical_use": "Match paragraph headings"
  },
  "matching_sentence_endings": {
    "answer_format": "string",
    "required_fields": ["endings"],
    "typical_use": "Complete sentences by matching"
  },
  "multiple_choice_more_than_one_answer_reading": {
    "answer_format": "array",
    "required_fields": ["options"],
    "optional_fields": ["max_choices"],
    "typical_use": "Choose 2+ answers"
  },
  "multiple_choice_one_answer_reading": {
    "answer_format": "string",
    "required_fields": ["options"],
    "typical_use": "Choose 1 answer"
  },
  "note_completion": {
    "answer_format": "string",
    "optional_fields": ["max_words"],
    "typical_use": "Complete notes/summary"
  },
  "sentence_completion_reading": {
    "answer_format": "string",
    "optional_fields": ["max_words"],
    "typical_use": "Complete sentences from passage"
  },
  "summary_completion_selecting_from_list": {
    "answer_format": "string",
    "required_fields": ["word_list"],
    "typical_use": "Complete summary from word list"
  },
  "summary_completion_selecting_words_from_text": {
    "answer_format": "string",
    "optional_fields": ["max_words"],
    "typical_use": "Complete summary from passage"
  },
  "table_completion_reading": {
    "answer_format": "string",
    "optional_fields": ["table_data", "max_words"],
    "typical_use": "Fill in table from passage"
  }
}
```

### Writing Types (2)
```json
{
  "writing_part_1": {
    "answer_format": null,
    "required_fields": ["min_words"],
    "optional_fields": ["chart_image", "task_number", "instructions"],
    "min_words": 150,
    "typical_use": "Chart/diagram description"
  },
  "writing_part_2": {
    "answer_format": null,
    "required_fields": ["min_words"],
    "optional_fields": ["task_number", "instructions"],
    "min_words": 250,
    "typical_use": "Essay writing"
  }
}
```

---

## Examples by Test Type

### Listening Test Structure
```json
{
  "test_type": "listening",
  "title": "IELTS Listening Practice Test",
  "description": "Complete listening test with 40 questions",
  "duration_seconds": 2004,
  "audio_url": "https://audio.jukehost.co.uk/sample",
  "sections": [
    {
      "index": 1,
      "title": "Section 1: Social Needs",
      "instructions": "Questions 1-10",
      "questions": [
        {
          "index": 1,
          "type": "fill_in_the_gaps",
          "prompt": "The student will study _____ at university.",
          "answer_key": "engineering",
          "max_words": 1
        }
      ]
    },
    {
      "index": 2,
      "title": "Section 2: Campus Facilities", 
      "instructions": "Questions 11-20",
      "questions": [
        {
          "index": 11,
          "type": "labelling_on_a_map",
          "prompt": "Label the map below. Choose your answers from the box.",
          "answer_key": "Library",
          "image_url": "https://example.com/campus-map.png"
        }
      ]
    }
  ]
}
```

### Reading Test Structure
```json
{
  "test_type": "reading",
  "title": "IELTS Reading Practice Test",
  "description": "Complete reading test with 40 questions",
  "duration_seconds": 3600,
  "audio_url": null,
  "sections": [
    {
      "index": 1,
      "title": "Passage 1: Ancient Civilizations",
      "instructions": "Questions 1-13",
      "passage_text": "A\nAlthough humans have established many types of societies...",
      "questions": [
        {
          "index": 1,
          "type": "identifying_information_true_false_not_given",
          "prompt": "Ancient civilizations were more advanced than modern ones.",
          "answer_key": "FALSE",
          "options": [
            {"value": "TRUE", "text": "TRUE"},
            {"value": "FALSE", "text": "FALSE"},
            {"value": "NOT GIVEN", "text": "NOT GIVEN"}
          ]
        }
      ]
    }
  ]
}
```

### Writing Test Structure
```json
{
  "test_type": "writing",
  "title": "IELTS Writing Practice Test",
  "description": "Complete writing test with 2 tasks",
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
          "answer_key": null,
          "chart_image": "https://example.com/milk-chart.png",
          "min_words": 150,
          "task_number": 1,
          "instructions": "You should spend about 20 minutes on this task."
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
          "prompt": "Some people believe that international media should be controlled by governments. To what extent do you agree or disagree?",
          "answer_key": null,
          "min_words": 250,
          "task_number": 2,
          "instructions": "Give reasons for your answer and include any relevant examples from your own knowledge or experience."
        }
      ]
    }
  ]
}
```

---

## Validation Checklist

Before importing JSON, verify:

### Structure Validation
- [ ] `test_type` is "listening", "reading", or "writing"
- [ ] `title` and `description` are within character limits
- [ ] `duration_seconds` is reasonable (60-7200)
- [ ] `sections` array has 1-4 sections
- [ ] Each section has required fields (`index`, `title`, `instructions`, `questions`)

### Question Validation  
- [ ] All question `index` values are sequential (1, 2, 3...)
- [ ] All question `type` values match valid QTI type names
- [ ] All questions have `prompt` text
- [ ] Non-writing questions have `answer_key`
- [ ] Writing questions have `answer_key: null`

### Type-Specific Validation
- [ ] Multiple choice questions have `options` array
- [ ] Matching questions have appropriate arrays (`headings`, `features`, `endings`)
- [ ] Word limit questions have reasonable `max_words` (1-10)
- [ ] Writing questions have appropriate `min_words` (150+ for task 1, 250+ for task 2)

### Format Validation
- [ ] `options` are arrays of objects with `value` and `text` properties
- [ ] URLs are valid (audio_url, image_url, chart_image)
- [ ] No missing commas or brackets
- [ ] Valid JSON syntax

### Content Validation
- [ ] Listening tests have `audio_url`
- [ ] Reading sections have `passage_text`  
- [ ] Writing questions have null `audio_url` and `passage_text`
- [ ] Question prompts are meaningful and complete
- [ ] Answer keys match expected formats for each question type

This standard ensures consistent, valid JSON that will pass backend validation and render correctly in the frontend components.