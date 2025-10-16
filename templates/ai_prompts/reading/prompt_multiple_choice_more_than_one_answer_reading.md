# Multiple Choice More Than One Answer Reading - Conversion Prompt

## Recognition
When you see these indicators in the PDF:
- "Choose TWO/THREE letters"
- "Which TWO/THREE..."
- Multiple correct answers required from reading passage
- Options A-G or A-H

Use type: `multiple_choice_more_than_one_answer_reading`

## Required Fields
- **index** (integer) - Question number
- **type** (string) - Must be "multiple_choice_more_than_one_answer_reading"
- **prompt** (string) - Question text
- **answer_key** (array) - Array of correct letters
- **options** (array) - List of all options
- **max_choices** (integer) - Number of answers to choose (2 or 3)

## JSON Template
```json
{
  "index": 1,
  "type": "multiple_choice_more_than_one_answer_reading",
  "prompt": "Which TWO challenges are mentioned in the passage?",
  "answer_key": ["B", "E"],
  "max_choices": 2,
  "options": [
    {"value": "A", "text": "Limited funding"},
    {"value": "B", "text": "Technical difficulties"},
    {"value": "C", "text": "Staff shortages"},
    {"value": "D", "text": "Time constraints"},
    {"value": "E", "text": "Resource limitations"}
  ]
}
```

## Real Examples

### Example 1: Choose TWO
**PDF Input:**
```
Questions 24-25
Which TWO factors contributed to the decline?
Choose TWO letters, A-E.

A. Economic recession
B. Natural disasters
C. Political instability
D. Climate change
E. Population growth

24-25. _____

Answers: A, D
```

**JSON Output:**
```json
{
  "index": 24,
  "type": "multiple_choice_more_than_one_answer_reading",
  "prompt": "Which TWO factors contributed to the decline?",
  "answer_key": ["A", "D"],
  "max_choices": 2,
  "options": [
    {"value": "A", "text": "Economic recession"},
    {"value": "B", "text": "Natural disasters"},
    {"value": "C", "text": "Political instability"},
    {"value": "D", "text": "Climate change"},
    {"value": "E", "text": "Population growth"}
  ]
}
```

## Common Mistakes to Avoid

### Mistake 1: String Instead of Array for answer_key
❌ **Wrong:** `"answer_key": "A, D"`
✅ **Correct:** `"answer_key": ["A", "D"]`

### Mistake 2: Wrong Type
❌ **Wrong:** Using `multiple_choice_one_answer_reading`
✅ **Correct:** Use `multiple_choice_more_than_one_answer_reading`

### Mistake 3: Separate Questions
❌ **Wrong:** Creating questions 24 and 25 separately
✅ **Correct:** One question (index 24) with array of 2 answers
