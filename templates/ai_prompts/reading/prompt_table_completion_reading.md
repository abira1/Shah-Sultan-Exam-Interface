# Table Completion Reading - Conversion Prompt

## Recognition
When you see these indicators in the PDF:
- "Complete the table below"
- "Write NO MORE THAN TWO/THREE WORDS from the passage"
- Table/grid structure with headers
- Fill in missing cells with words from text

Use type: `table_completion_reading`

## Required Fields
- **index** (integer) - Question number
- **type** (string) - Must be "table_completion_reading"
- **prompt** (string) - Row/column context
- **answer_key** (string) - Words from passage

## Optional Fields
- **max_words** (integer) - Maximum words allowed
- **row** (string) - Row identifier
- **column** (string) - Column identifier

## JSON Template
```json
{
  "index": 1,
  "type": "table_completion_reading",
  "prompt": "Species: Tigers - Habitat: _____",
  "answer_key": "tropical forests",
  "max_words": 2,
  "row": "Tigers",
  "column": "Habitat"
}
```

## Real Examples

### Example 1: Species Information Table
**PDF Input:**
```
Questions 8-12
Complete the table below.
Choose NO MORE THAN THREE WORDS from the passage for each answer.

| Species  | Habitat         | Diet            | Status       |
|----------|-----------------|-----------------|-------------|
| Tigers   | (8) _____       | carnivorous     | endangered   |
| Pandas   | bamboo forests  | (9) _____       | (10) _____   |
| Eagles   | (11) _____      | small mammals   | (12) _____   |

Answers: 8. tropical forests  9. bamboo shoots  10. vulnerable  
11. mountain regions  12. least concern
```

**JSON Output:**
```json
[
  {
    "index": 8,
    "type": "table_completion_reading",
    "prompt": "Species: Tigers - Habitat: _____",
    "answer_key": "tropical forests",
    "max_words": 3,
    "row": "Tigers",
    "column": "Habitat"
  },
  {
    "index": 9,
    "type": "table_completion_reading",
    "prompt": "Species: Pandas - Diet: _____",
    "answer_key": "bamboo shoots",
    "max_words": 3,
    "row": "Pandas",
    "column": "Diet"
  },
  {
    "index": 10,
    "type": "table_completion_reading",
    "prompt": "Species: Pandas - Status: _____",
    "answer_key": "vulnerable",
    "max_words": 3,
    "row": "Pandas",
    "column": "Status"
  }
]
```

## Common Mistakes to Avoid

### Mistake 1: Not Including Context
❌ **Wrong:** `"prompt": "_____"`
✅ **Correct:** `"prompt": "Species: Tigers - Habitat: _____"`

### Mistake 2: Using Listening Type
❌ **Wrong:** `table_completion_listening`
✅ **Correct:** `table_completion_reading` for reading passages

### Mistake 3: Answer Not From Passage
❌ **Wrong:** Using inference or paraphrasing
✅ **Correct:** Use exact words from the passage
