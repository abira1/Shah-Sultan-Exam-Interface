# Table Completion Listening - Conversion Prompt

## Recognition
When you see these indicators in the PDF:
- "Complete the table below"
- Grid/table structure with headers
- Multiple rows and columns
- Fill in missing cells
- Usually Section 2 or 3

Use type: `table_completion_listening`

## Required Fields
- **index** (integer) - Question number
- **type** (string) - Must be "table_completion_listening"
- **prompt** (string) - Row/column context
- **answer_key** (string) - Correct answer

## Optional Fields
- **max_words** (integer) - Maximum words allowed
- **row** (string) - Row identifier
- **column** (string) - Column identifier

## JSON Template
```json
{
  "index": 1,
  "type": "table_completion_listening",
  "prompt": "Course: Engineering - Duration: _____",
  "answer_key": "3 years",
  "max_words": 2,
  "row": "Engineering",
  "column": "Duration"
}
```

## Real Examples

### Example 1: Course Information Table
**PDF Input:**
```
Questions 6-10
Complete the table showing course information.

| Course      | Duration | Start Date | Fee    |
|-------------|----------|------------|--------|
| Engineering | (6)      | September  | $8,000 |
| Medicine    | 5 years  | (7)        | (8)    |
| Law         | (9)      | October    | (10)   |

Answers: 6. 4 years  7. January  8. $12,000  9. 3 years  10. $7,500
```

**JSON Output:**
```json
[
  {
    "index": 6,
    "type": "table_completion_listening",
    "prompt": "Course: Engineering - Duration: _____",
    "answer_key": "4 years",
    "max_words": 2,
    "row": "Engineering",
    "column": "Duration"
  },
  {
    "index": 7,
    "type": "table_completion_listening",
    "prompt": "Course: Medicine - Start Date: _____",
    "answer_key": "January",
    "max_words": 1,
    "row": "Medicine",
    "column": "Start Date"
  },
  {
    "index": 8,
    "type": "table_completion_listening",
    "prompt": "Course: Medicine - Fee: _____",
    "answer_key": "$12,000",
    "max_words": 1,
    "row": "Medicine",
    "column": "Fee"
  }
]
```

## Common Mistakes to Avoid

### Mistake 1: Not Including Row/Column Context
❌ **Wrong:** `"prompt": "_____"`
✅ **Correct:** `"prompt": "Course: Engineering - Duration: _____"`

### Mistake 2: Confusing with Reading Type
❌ **Wrong:** Using `table_completion_reading`
✅ **Correct:** Use `table_completion_listening` for listening tests
