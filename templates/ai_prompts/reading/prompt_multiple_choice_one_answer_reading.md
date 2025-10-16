# Multiple Choice One Answer Reading - Conversion Prompt

## Recognition
When you see these indicators in the PDF:
- "Choose the correct letter A, B, C, or D"
- Single correct answer from reading passage
- 3-4 options provided

Use type: `multiple_choice_one_answer_reading`

## Required Fields
- **index** (integer) - Question number
- **type** (string) - Must be "multiple_choice_one_answer_reading"
- **prompt** (string) - Question text
- **answer_key** (string) - Correct letter (A, B, C, or D)
- **options** (array) - List of all options

## JSON Template
```json
{
  "index": 1,
  "type": "multiple_choice_one_answer_reading",
  "prompt": "What is the main idea of the passage?",
  "answer_key": "B",
  "options": [
    {"value": "A", "text": "To describe a process"},
    {"value": "B", "text": "To analyze a problem"},
    {"value": "C", "text": "To compare solutions"},
    {"value": "D", "text": "To predict outcomes"}
  ]
}
```

## Real Examples

### Example 1: Main Idea Question
**PDF Input:**
```
Question 27:
What is the writer's main purpose in the third paragraph?

A. To provide historical context
B. To introduce a new argument
C. To give examples
D. To summarize previous points

Answer: B
```

**JSON Output:**
```json
{
  "index": 27,
  "type": "multiple_choice_one_answer_reading",
  "prompt": "What is the writer's main purpose in the third paragraph?",
  "answer_key": "B",
  "options": [
    {"value": "A", "text": "To provide historical context"},
    {"value": "B", "text": "To introduce a new argument"},
    {"value": "C", "text": "To give examples"},
    {"value": "D", "text": "To summarize previous points"}
  ]
}
```

## Common Mistakes to Avoid

### Mistake 1: Array Instead of String
❌ **Wrong:** `"answer_key": ["B"]`
✅ **Correct:** `"answer_key": "B"`

### Mistake 2: Using Multiple Answer Type
❌ **Wrong:** Using `multiple_choice_more_than_one_answer_reading`
✅ **Correct:** Use `multiple_choice_one_answer_reading` for single answer
