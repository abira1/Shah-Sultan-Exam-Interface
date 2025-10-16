# Matching Listening - Conversion Prompt

## Recognition
When you see these indicators in the PDF:
- "Match the items/people/places"
- "Choose from the list A-H"
- Two lists to match
- Usually Section 2 or 3

Use type: `matching_listening`

## Required Fields
- **index** (integer) - Question number
- **type** (string) - Must be "matching_listening"
- **prompt** (string) - Item to match
- **answer_key** (string) - Correct letter
- **options** (array) - List of possible matches

## Optional Fields
- **match_type** (string) - Type of matching (people, features, dates, etc.)

## JSON Template
```json
{
  "index": 1,
  "type": "matching_listening",
  "prompt": "John",
  "answer_key": "C",
  "options": [
    {"value": "A", "text": "Engineer"},
    {"value": "B", "text": "Teacher"},
    {"value": "C", "text": "Doctor"}
  ]
}
```

## Real Examples

### Example 1: Match People to Professions
**PDF Input:**
```
Questions 16-20
Match each person to their profession.
Choose from list A-H.

A. Engineer
B. Teacher  
C. Doctor
D. Lawyer
E. Architect

16. Sarah
17. Michael
18. Emma
19. David
20. Lisa

Answers: 16. C  17. A  18. B  19. E  20. D
```

**JSON Output:**
```json
[
  {
    "index": 16,
    "type": "matching_listening",
    "prompt": "Sarah",
    "answer_key": "C",
    "options": [
      {"value": "A", "text": "Engineer"},
      {"value": "B", "text": "Teacher"},
      {"value": "C", "text": "Doctor"},
      {"value": "D", "text": "Lawyer"},
      {"value": "E", "text": "Architect"}
    ]
  },
  {
    "index": 17,
    "type": "matching_listening",
    "prompt": "Michael",
    "answer_key": "A",
    "options": [
      {"value": "A", "text": "Engineer"},
      {"value": "B", "text": "Teacher"},
      {"value": "C", "text": "Doctor"},
      {"value": "D", "text": "Lawyer"},
      {"value": "E", "text": "Architect"}
    ]
  }
]
```

## Common Mistakes to Avoid

### Mistake 1: Not Including All Options
❌ **Wrong:** Only including the correct option
✅ **Correct:** Include ALL options from the list A-H

### Mistake 2: Options as String Array
❌ **Wrong:** `"options": ["Engineer", "Teacher"]`
✅ **Correct:** `"options": [{"value": "A", "text": "Engineer"}, ...]`
