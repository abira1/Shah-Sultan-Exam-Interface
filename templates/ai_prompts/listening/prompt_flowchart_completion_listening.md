# Flowchart Completion Listening - Conversion Prompt

## Recognition
When you see these indicators in the PDF:
- "Complete the flowchart below"
- Diagram showing a process or sequence
- Arrows connecting boxes/stages
- Listening to describe a process
- Usually Section 2 or 3

Use type: `flowchart_completion_listening`

## Required Fields
- **index** (integer) - Question number
- **type** (string) - Must be "flowchart_completion_listening"
- **prompt** (string) - Description of flowchart stage
- **answer_key** (string) - Correct answer

## Optional Fields
- **max_words** (integer) - Maximum words allowed
- **flowchart_image** (string) - URL to flowchart image
- **stage** (string) - Stage/box label in flowchart

## JSON Template
```json
{
  "index": 1,
  "type": "flowchart_completion_listening",
  "prompt": "Stage 1: _____",
  "answer_key": "registration",
  "max_words": 2,
  "stage": "Stage 1"
}
```

## Real Examples

### Example 1: Process Description
**PDF Input:**
```
Questions 15-18
Complete the flowchart showing the application process.

15. First step: Submit _____
16. Second step: Attend _____
17. Third step: Complete _____
18. Final step: Receive _____

Answers: 15. application form  16. interview  17. assessment  18. confirmation email
```

**JSON Output:**
```json
[
  {
    "index": 15,
    "type": "flowchart_completion_listening",
    "prompt": "First step: Submit _____",
    "answer_key": "application form",
    "max_words": 2,
    "stage": "First step"
  },
  {
    "index": 16,
    "type": "flowchart_completion_listening",
    "prompt": "Second step: Attend _____",
    "answer_key": "interview",
    "max_words": 1,
    "stage": "Second step"
  }
]
```

## Common Mistakes to Avoid

### Mistake 1: Confusing with Reading Type
❌ **Wrong:** `flowchart_completion_selecting_words_from_text` (this is for reading)
✅ **Correct:** `flowchart_completion_listening` (for listening)

### Mistake 2: Not Including Stage Context
❌ **Wrong:** `"prompt": "_____"` (too vague)
✅ **Correct:** `"prompt": "Stage 1: _____"` (includes context)
