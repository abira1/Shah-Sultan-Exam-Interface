# Identifying Information TRUE/FALSE/NOT GIVEN - Conversion Prompt

## Recognition
When you see these indicators in the PDF:
- "Do the following statements agree with the information in the text?"
- "Write TRUE, FALSE, or NOT GIVEN"
- "Write YES, NO, or NOT GIVEN" (also uses this type)
- Statement verification questions

Use type: `identifying_information_true_false_not_given`

## Required Fields
- **index** (integer) - Question number
- **type** (string) - Must be "identifying_information_true_false_not_given"
- **prompt** (string) - Statement to verify
- **answer_key** (string) - "TRUE", "FALSE", or "NOT GIVEN"
- **options** (array) - Always the same three options

## JSON Template
```json
{
  "index": 1,
  "type": "identifying_information_true_false_not_given",
  "prompt": "The company was founded in 1990.",
  "answer_key": "TRUE",
  "options": [
    {"value": "TRUE", "text": "TRUE"},
    {"value": "FALSE", "text": "FALSE"},
    {"value": "NOT GIVEN", "text": "NOT GIVEN"}
  ]
}
```

## Real Examples

### Example 1: TRUE Statement
**PDF Input:**
```
Questions 1-5
Do the following statements agree with the information in Reading Passage 1?
Write:
TRUE if the statement agrees with the information
FALSE if the statement contradicts the information  
NOT GIVEN if there is no information on this

1. The research was conducted over five years.
2. All participants were volunteers.

Answers: 1. TRUE  2. FALSE
```

**JSON Output:**
```json
[
  {
    "index": 1,
    "type": "identifying_information_true_false_not_given",
    "prompt": "The research was conducted over five years.",
    "answer_key": "TRUE",
    "options": [
      {"value": "TRUE", "text": "TRUE"},
      {"value": "FALSE", "text": "FALSE"},
      {"value": "NOT GIVEN", "text": "NOT GIVEN"}
    ]
  },
  {
    "index": 2,
    "type": "identifying_information_true_false_not_given",
    "prompt": "All participants were volunteers.",
    "answer_key": "FALSE",
    "options": [
      {"value": "TRUE", "text": "TRUE"},
      {"value": "FALSE", "text": "FALSE"},
      {"value": "NOT GIVEN", "text": "NOT GIVEN"}
    ]
  }
]
```

### Example 2: YES/NO/NOT GIVEN Variant
**PDF Input:**
```
Questions 8-11
Do the following statements agree with the views of the writer?
Write:
YES if the statement agrees with the views of the writer
NO if the statement contradicts the views of the writer
NOT GIVEN if it is impossible to say what the writer thinks

8. Climate change is the most pressing issue.

Answer: YES
```

**JSON Output:**
```json
{
  "index": 8,
  "type": "identifying_information_true_false_not_given",
  "prompt": "Climate change is the most pressing issue.",
  "answer_key": "TRUE",
  "options": [
    {"value": "TRUE", "text": "TRUE"},
    {"value": "FALSE", "text": "FALSE"},
    {"value": "NOT GIVEN", "text": "NOT GIVEN"}
  ]
}
```

**Note:** Convert YES to TRUE, NO to FALSE in answer_key.

## Common Mistakes to Avoid

### Mistake 1: Using Short Type Name
❌ **Wrong:** `"type": "true_false_not_given"`
✅ **Correct:** `"type": "identifying_information_true_false_not_given"`

### Mistake 2: Lowercase Answers
❌ **Wrong:** `"answer_key": "true"`
✅ **Correct:** `"answer_key": "TRUE"`

### Mistake 3: Not Converting YES/NO
❌ **Wrong:** `"answer_key": "YES"` (when system expects TRUE/FALSE)
✅ **Correct:** `"answer_key": "TRUE"` (convert YES→TRUE, NO→FALSE)

### Mistake 4: Options as Strings
❌ **Wrong:** `"options": ["TRUE", "FALSE", "NOT GIVEN"]`
✅ **Correct:** `"options": [{"value": "TRUE", "text": "TRUE"}, ...]`
