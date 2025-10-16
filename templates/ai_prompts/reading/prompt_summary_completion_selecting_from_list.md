# Summary Completion Selecting from List - Conversion Prompt

## Recognition
When you see these indicators in the PDF:
- "Complete the summary using words from the box below"
- "Choose from the list A-K"
- Word bank provided
- Summary paragraph with numbered blanks

Use type: `summary_completion_selecting_from_list`

## Required Fields
- **index** (integer) - Question number
- **type** (string) - Must be "summary_completion_selecting_from_list"
- **prompt** (string) - Summary sentence with blank
- **answer_key** (string) - Correct word from list
- **word_list** (array) - List of words to choose from

## JSON Template
```json
{
  "index": 1,
  "type": "summary_completion_selecting_from_list",
  "prompt": "The research revealed that (1) _____ was a major factor.",
  "answer_key": "pollution",
  "word_list": ["pollution", "climate", "population", "technology", "economy"]
}
```

## Real Examples

### Example 1: Summary with Word Box
**PDF Input:**
```
Questions 36-40
Complete the summary below.
Choose your answers from the box below and write them in boxes 36-40.

Word Box:
A. climate
B. pollution
C. technology
D. economy
E. population
F. resources
G. energy
H. agriculture

The study examined the impact of (36) _____ on marine ecosystems. 
Researchers discovered that (37) _____ plays a significant role.
The effects on (38) _____ were particularly severe.
New (39) _____ could help address these issues.
Future (40) _____ growth may worsen the situation.

Answers: 36. B  37. A  38. F  39. C  40. E
```

**JSON Output:**
```json
[
  {
    "index": 36,
    "type": "summary_completion_selecting_from_list",
    "prompt": "The study examined the impact of _____ on marine ecosystems.",
    "answer_key": "pollution",
    "word_list": ["climate", "pollution", "technology", "economy", "population", "resources", "energy", "agriculture"]
  },
  {
    "index": 37,
    "type": "summary_completion_selecting_from_list",
    "prompt": "Researchers discovered that _____ plays a significant role.",
    "answer_key": "climate",
    "word_list": ["climate", "pollution", "technology", "economy", "population", "resources", "energy", "agriculture"]
  }
]
```

## Common Mistakes to Avoid

### Mistake 1: Using Letter Instead of Word
❌ **Wrong:** `"answer_key": "B"`
✅ **Correct:** `"answer_key": "pollution"` (the actual word, not the letter)

### Mistake 2: Not Including Full Word List
❌ **Wrong:** Only including words that are answers
✅ **Correct:** Include ALL words from box A-H (or however many)

### Mistake 3: word_list as Objects
❌ **Wrong:** `"word_list": [{"value": "A", "text": "climate"}]`
✅ **Correct:** `"word_list": ["climate", "pollution", ...]` (simple string array)
