# Multiple Choice More Than One Answer Listening - Conversion Prompt

## Recognition
When you see these indicators in the PDF:
- "Choose TWO/THREE letters"
- "Which TWO/THREE..."
- Multiple correct answers required
- Options A-G or A-H
- Usually Section 3 or 4

Use type: `multiple_choice_more_than_one_answer_listening`

## Required Fields
- **index** (integer) - Question number
- **type** (string) - Must be "multiple_choice_more_than_one_answer_listening"
- **prompt** (string) - Question text
- **answer_key** (array) - Array of correct letters
- **options** (array) - List of all options
- **max_choices** (integer) - Number of answers to choose (2 or 3)

## JSON Template
```json
{
  "index": 1,
  "type": "multiple_choice_more_than_one_answer_listening",
  "prompt": "Which TWO problems are mentioned?",
  "answer_key": ["B", "D"],
  "max_choices": 2,
  "options": [
    {"value": "A", "text": "Cost issues"},
    {"value": "B", "text": "Time constraints"},
    {"value": "C", "text": "Staff shortage"},
    {"value": "D", "text": "Equipment failure"},
    {"value": "E", "text": "Weather conditions"}
  ]
}
```

## Real Examples

### Example 1: Choose TWO
**PDF Input:**
```
Questions 23-24
Which TWO factors affected the project?

A. Budget cuts
B. Weather delays
C. Staff changes
D. Material shortages
E. Design modifications

23-24. _____

Answers: B, D
```

**JSON Output:**
```json
{
  "index": 23,
  "type": "multiple_choice_more_than_one_answer_listening",
  "prompt": "Which TWO factors affected the project?",
  "answer_key": ["B", "D"],
  "max_choices": 2,
  "options": [
    {"value": "A", "text": "Budget cuts"},
    {"value": "B", "text": "Weather delays"},
    {"value": "C", "text": "Staff changes"},
    {"value": "D", "text": "Material shortages"},
    {"value": "E", "text": "Design modifications"}
  ]
}
```

### Example 2: Choose THREE
**PDF Input:**
```
Questions 25-27
Which THREE benefits are mentioned?

A. Cost savings
B. Improved efficiency
C. Better quality
D. Faster delivery
E. Increased capacity
F. Reduced waste
G. Enhanced safety

25-27. _____

Answers: A, C, F
```

**JSON Output:**
```json
{
  "index": 25,
  "type": "multiple_choice_more_than_one_answer_listening",
  "prompt": "Which THREE benefits are mentioned?",
  "answer_key": ["A", "C", "F"],
  "max_choices": 3,
  "options": [
    {"value": "A", "text": "Cost savings"},
    {"value": "B", "text": "Improved efficiency"},
    {"value": "C", "text": "Better quality"},
    {"value": "D", "text": "Faster delivery"},
    {"value": "E", "text": "Increased capacity"},
    {"value": "F", "text": "Reduced waste"},
    {"value": "G", "text": "Enhanced safety"}
  ]
}
```

## Common Mistakes to Avoid

### Mistake 1: Single String Instead of Array
❌ **Wrong:** `"answer_key": "B, D"`
✅ **Correct:** `"answer_key": ["B", "D"]`

### Mistake 2: Using Single Choice Type
❌ **Wrong:** Using `multiple_choice_one_answer_listening`
✅ **Correct:** Use `multiple_choice_more_than_one_answer_listening`

### Mistake 3: Wrong max_choices
❌ **Wrong:** `"max_choices": 2` when question says "Choose THREE"
✅ **Correct:** `"max_choices": 3` (must match question)

### Mistake 4: Separate Questions for Each Answer
❌ **Wrong:** Creating index 23, 24, 25 as separate questions
✅ **Correct:** One question (index 23) with array of 3 answers
