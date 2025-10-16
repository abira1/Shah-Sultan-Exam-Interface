# Flowchart Completion Selecting Words from Text - Conversion Prompt

## Recognition
When you see these indicators in the PDF:
- "Complete the flowchart using words from the passage"
- "Write NO MORE THAN TWO/THREE WORDS from the text"
- Flowchart diagram with blanks
- Process or sequence description in passage

Use type: `flowchart_completion_selecting_words_from_text`

## Required Fields
- **index** (integer) - Question number
- **type** (string) - Must be "flowchart_completion_selecting_words_from_text"
- **prompt** (string) - Flowchart stage/box description
- **answer_key** (string) - Exact words from passage

## Optional Fields
- **max_words** (integer) - Maximum words allowed
- **stage** (string) - Stage identifier

## JSON Template
```json
{
  "index": 1,
  "type": "flowchart_completion_selecting_words_from_text",
  "prompt": "First stage: _____",
  "answer_key": "initial assessment",
  "max_words": 2
}
```

## Real Examples

### Example 1: Process Flowchart
**PDF Input:**
```
Questions 5-8
Complete the flowchart below.
Choose NO MORE THAN TWO WORDS from the passage for each answer.

5. Stage 1: _____
6. Stage 2: _____
7. Stage 3: _____
8. Final stage: _____

Answers: 5. data collection  6. initial analysis  7. peer review  8. publication
```

**JSON Output:**
```json
[
  {
    "index": 5,
    "type": "flowchart_completion_selecting_words_from_text",
    "prompt": "Stage 1: _____",
    "answer_key": "data collection",
    "max_words": 2,
    "stage": "Stage 1"
  },
  {
    "index": 6,
    "type": "flowchart_completion_selecting_words_from_text",
    "prompt": "Stage 2: _____",
    "answer_key": "initial analysis",
    "max_words": 2,
    "stage": "Stage 2"
  }
]
```

## Common Mistakes to Avoid

### Mistake 1: Using Listening Type
❌ **Wrong:** `flowchart_completion_listening`
✅ **Correct:** `flowchart_completion_selecting_words_from_text` (for reading)

### Mistake 2: Answer Not From Text
❌ **Wrong:** Paraphrasing or using different words
✅ **Correct:** Use exact words from passage
