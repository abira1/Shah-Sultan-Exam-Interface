# Matching Headings - Conversion Prompt

## Recognition
When you see these indicators in the PDF:
- "Choose the correct heading for each paragraph"
- "Choose from the list of headings below"
- Roman numerals (i, ii, iii, iv, etc.)
- Match to paragraphs A, B, C, etc.

Use type: `matching_headings`

## Required Fields
- **index** (integer) - Question number
- **type** (string) - Must be "matching_headings"
- **prompt** (string) - Paragraph identifier (e.g., "Paragraph A")
- **answer_key** (string) - Correct heading (roman numeral)
- **headings** (array) - List of all available headings

## JSON Template
```json
{
  "index": 1,
  "type": "matching_headings",
  "prompt": "Paragraph A",
  "answer_key": "iii",
  "headings": [
    {"value": "i", "text": "Early developments"},
    {"value": "ii", "text": "Modern applications"},
    {"value": "iii", "text": "Future prospects"}
  ]
}
```

## Real Examples

### Example 1: Standard Matching Headings
**PDF Input:**
```
Questions 14-18
The reading passage has five paragraphs, A-E.
Choose the correct heading for each paragraph from the list of headings below.

List of Headings:
i. The origins of the practice
ii. Economic benefits
iii. Environmental concerns
iv. Government regulations
v. Public opinion
vi. Future developments
vii. International comparisons

14. Paragraph A
15. Paragraph B
16. Paragraph C
17. Paragraph D
18. Paragraph E

Answers: 14. i  15. ii  16. v  17. iv  18. vi
```

**JSON Output:**
```json
[
  {
    "index": 14,
    "type": "matching_headings",
    "prompt": "Paragraph A",
    "answer_key": "i",
    "headings": [
      {"value": "i", "text": "The origins of the practice"},
      {"value": "ii", "text": "Economic benefits"},
      {"value": "iii", "text": "Environmental concerns"},
      {"value": "iv", "text": "Government regulations"},
      {"value": "v", "text": "Public opinion"},
      {"value": "vi", "text": "Future developments"},
      {"value": "vii", "text": "International comparisons"}
    ]
  },
  {
    "index": 15,
    "type": "matching_headings",
    "prompt": "Paragraph B",
    "answer_key": "ii",
    "headings": [
      {"value": "i", "text": "The origins of the practice"},
      {"value": "ii", "text": "Economic benefits"},
      {"value": "iii", "text": "Environmental concerns"},
      {"value": "iv", "text": "Government regulations"},
      {"value": "v", "text": "Public opinion"},
      {"value": "vi", "text": "Future developments"},
      {"value": "vii", "text": "International comparisons"}
    ]
  }
]
```

## Common Mistakes to Avoid

### Mistake 1: Using Numbers Instead of Roman Numerals
❌ **Wrong:** `"answer_key": "1"`
✅ **Correct:** `"answer_key": "i"`

### Mistake 2: Uppercase Roman Numerals
❌ **Wrong:** `"value": "I"` or `"value": "III"`
✅ **Correct:** `"value": "i"` or `"value": "iii"` (lowercase)

### Mistake 3: Not Including All Headings
❌ **Wrong:** Only including headings that are used
✅ **Correct:** Include ALL headings from the list (i through vii or however many)

### Mistake 4: Using "options" Instead of "headings"
❌ **Wrong:** `"options": [...]`
✅ **Correct:** `"headings": [...]`
