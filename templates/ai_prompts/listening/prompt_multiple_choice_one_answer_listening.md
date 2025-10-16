# Multiple Choice One Answer Listening - Conversion Prompt

## Recognition
When you see these indicators in the PDF:
- "Choose the correct letter A, B, or C"
- Single correct answer
- 3-4 options provided
- Usually Section 2, 3, or 4

Use type: `multiple_choice_one_answer_listening`

## Required Fields
- **index** (integer) - Question number
- **type** (string) - Must be "multiple_choice_one_answer_listening"
- **prompt** (string) - Question text
- **answer_key** (string) - Correct letter (A, B, C, or D)
- **options** (array) - List of all options

## JSON Template
```json
{
  "index": 1,
  "type": "multiple_choice_one_answer_listening",
  "prompt": "What is the main purpose of the lecture?",
  "answer_key": "B",
  "options": [
    {"value": "A", "text": "To inform about new policies"},
    {"value": "B", "text": "To explain research findings"},
    {"value": "C", "text": "To introduce a new course"}
  ]
}
```

## Real Examples

### Example 1: Three Options
**PDF Input:**
```
Question 15:
What does the speaker recommend?

A. Joining a study group
B. Reading additional materials
C. Attending extra tutorials

Answer: A
```

**JSON Output:**
```json
{
  "index": 15,
  "type": "multiple_choice_one_answer_listening",
  "prompt": "What does the speaker recommend?",
  "answer_key": "A",
  "options": [
    {"value": "A", "text": "Joining a study group"},
    {"value": "B", "text": "Reading additional materials"},
    {"value": "C", "text": "Attending extra tutorials"}
  ]
}
```

### Example 2: Four Options
**PDF Input:**
```
Question 28:
According to the speaker, what is the main advantage of the new system?

A. It saves time
B. It reduces costs
C. It improves accuracy
D. It increases flexibility

Answer: C
```

**JSON Output:**
```json
{
  "index": 28,
  "type": "multiple_choice_one_answer_listening",
  "prompt": "According to the speaker, what is the main advantage of the new system?",
  "answer_key": "C",
  "options": [
    {"value": "A", "text": "It saves time"},
    {"value": "B", "text": "It reduces costs"},
    {"value": "C", "text": "It improves accuracy"},
    {"value": "D", "text": "It increases flexibility"}
  ]
}
```

## Common Mistakes to Avoid

### Mistake 1: Array Instead of String for answer_key
❌ **Wrong:** `"answer_key": ["B"]`
✅ **Correct:** `"answer_key": "B"`

### Mistake 2: Including Answer in Option Text
❌ **Wrong:** `{"value": "A", "text": "A. Joining a study group"}`
✅ **Correct:** `{"value": "A", "text": "Joining a study group"}`

### Mistake 3: Using Multiple Answer Type
❌ **Wrong:** Using `multiple_choice_more_than_one_answer_listening`
✅ **Correct:** Use `multiple_choice_one_answer_listening` for single answer
