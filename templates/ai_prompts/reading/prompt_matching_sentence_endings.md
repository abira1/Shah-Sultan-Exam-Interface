# Matching Sentence Endings - Conversion Prompt

## Recognition
When you see these indicators in the PDF:
- "Complete each sentence with the correct ending A-H below"
- Sentence starters that need matching endings
- Choose from list of endings
- Usually 5-7 questions

Use type: `matching_sentence_endings`

## Required Fields
- **index** (integer) - Question number
- **type** (string) - Must be "matching_sentence_endings"
- **prompt** (string) - Sentence starter
- **answer_key** (string) - Correct ending letter
- **endings** (array) - List of all possible endings

## JSON Template
```json
{
  "index": 1,
  "type": "matching_sentence_endings",
  "prompt": "The research showed that",
  "answer_key": "D",
  "endings": [
    {"value": "A", "text": "climate change is accelerating"},
    {"value": "B", "text": "more data is needed"},
    {"value": "C", "text": "the results were inconclusive"},
    {"value": "D", "text": "pollution levels are rising"}
  ]
}
```

## Real Examples

### Example 1: Standard Sentence Endings
**PDF Input:**
```
Questions 9-13
Complete each sentence with the correct ending, A-H, below.

9. Early settlers discovered that
10. Scientists believe that
11. The government announced that
12. Research indicates that
13. Experts suggest that

List of Endings:
A. funding will increase next year
B. the climate was more favorable
C. new technologies are needed
D. pollution affects marine life
E. regulations should be stricter
F. the data supports the theory
G. further study is necessary
H. conservation efforts are working

Answers: 9. B  10. F  11. A  12. D  13. C
```

**JSON Output:**
```json
[
  {
    "index": 9,
    "type": "matching_sentence_endings",
    "prompt": "Early settlers discovered that",
    "answer_key": "B",
    "endings": [
      {"value": "A", "text": "funding will increase next year"},
      {"value": "B", "text": "the climate was more favorable"},
      {"value": "C", "text": "new technologies are needed"},
      {"value": "D", "text": "pollution affects marine life"},
      {"value": "E", "text": "regulations should be stricter"},
      {"value": "F", "text": "the data supports the theory"},
      {"value": "G", "text": "further study is necessary"},
      {"value": "H", "text": "conservation efforts are working"}
    ]
  },
  {
    "index": 10,
    "type": "matching_sentence_endings",
    "prompt": "Scientists believe that",
    "answer_key": "F",
    "endings": [
      {"value": "A", "text": "funding will increase next year"},
      {"value": "B", "text": "the climate was more favorable"},
      {"value": "C", "text": "new technologies are needed"},
      {"value": "D", "text": "pollution affects marine life"},
      {"value": "E", "text": "regulations should be stricter"},
      {"value": "F", "text": "the data supports the theory"},
      {"value": "G", "text": "further study is necessary"},
      {"value": "H", "text": "conservation efforts are working"}
    ]
  }
]
```

## Common Mistakes to Avoid

### Mistake 1: Using "options" Instead of "endings"
❌ **Wrong:** `"options": [...]`
✅ **Correct:** `"endings": [...]`

### Mistake 2: Including Sentence Starter in Endings
❌ **Wrong:** Ending text includes the sentence starter
✅ **Correct:** Only the ending portion in the endings array

### Mistake 3: Not Including All Endings
❌ **Wrong:** Only including endings that are used as answers
✅ **Correct:** Include ALL endings from list A-H (or however many provided)
