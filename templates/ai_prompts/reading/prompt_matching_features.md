# Matching Features - Conversion Prompt

## Recognition
When you see these indicators in the PDF:
- "Match each statement with the correct person/researcher/place"
- "Choose from the list A-F"
- Matching items to categories/people/places
- Some letters may be used more than once

Use type: `matching_features`

## Required Fields
- **index** (integer) - Question number
- **type** (string) - Must be "matching_features"
- **prompt** (string) - Statement to match
- **answer_key** (string) - Correct letter
- **features** (array) - List of people/places/categories to match

## JSON Template
```json
{
  "index": 1,
  "type": "matching_features",
  "prompt": "Developed a new theory of evolution",
  "answer_key": "B",
  "features": [
    {"value": "A", "text": "Charles Darwin"},
    {"value": "B", "text": "Alfred Wallace"},
    {"value": "C", "text": "Gregor Mendel"}
  ]
}
```

## Real Examples

### Example 1: Match Researchers to Discoveries
**PDF Input:**
```
Questions 18-22
Match each discovery with the correct researcher.
Choose from the list A-E below.
NB: You may use any letter more than once.

List of Researchers:
A. Marie Curie
B. Albert Einstein
C. Isaac Newton
D. Nikola Tesla
E. Thomas Edison

18. Discovered radioactivity
19. Developed theory of relativity
20. Formulated laws of motion
21. Invented alternating current
22. Created the light bulb

Answers: 18. A  19. B  20. C  21. D  22. E
```

**JSON Output:**
```json
[
  {
    "index": 18,
    "type": "matching_features",
    "prompt": "Discovered radioactivity",
    "answer_key": "A",
    "features": [
      {"value": "A", "text": "Marie Curie"},
      {"value": "B", "text": "Albert Einstein"},
      {"value": "C", "text": "Isaac Newton"},
      {"value": "D", "text": "Nikola Tesla"},
      {"value": "E", "text": "Thomas Edison"}
    ]
  },
  {
    "index": 19,
    "type": "matching_features",
    "prompt": "Developed theory of relativity",
    "answer_key": "B",
    "features": [
      {"value": "A", "text": "Marie Curie"},
      {"value": "B", "text": "Albert Einstein"},
      {"value": "C", "text": "Isaac Newton"},
      {"value": "D", "text": "Nikola Tesla"},
      {"value": "E", "text": "Thomas Edison"}
    ]
  }
]
```

## Common Mistakes to Avoid

### Mistake 1: Using Wrong Field Name
❌ **Wrong:** `"options"` instead of `"features"`
✅ **Correct:** `"features"` for this question type

### Mistake 2: Not Including All Features
❌ **Wrong:** Only including the features that are answers
✅ **Correct:** Include ALL features from the list A-E (or A-F, etc.)
