# Labelling on a Map - Conversion Prompt

## Recognition
When you see these indicators in the PDF:
- "Label the map/plan/diagram below"
- Map, floor plan, or layout diagram
- Locations marked with letters or numbers
- "Write the correct letter A-H"
- Usually Section 2

Use type: `labelling_on_a_map`

## Required Fields
- **index** (integer) - Question number
- **type** (string) - Must be "labelling_on_a_map"
- **prompt** (string) - Location description
- **answer_key** (string) - Correct letter (A-Z)

## Optional Fields
- **map_image** (string) - URL to map image
- **locations** (array) - List of available locations with letters

## JSON Template
```json
{
  "index": 1,
  "type": "labelling_on_a_map",
  "prompt": "Cafeteria",
  "answer_key": "C",
  "locations": [
    {"value": "A", "text": "Library"},
    {"value": "B", "text": "Gym"},
    {"value": "C", "text": "Cafeteria"}
  ]
}
```

## Real Examples

### Example 1: Campus Map
**PDF Input:**
```
Questions 11-15
Label the campus map below.
Write the correct letter A-J next to questions 11-15.

11. Main entrance
12. Library
13. Sports center
14. Administration building
15. Student accommodation

Answers: 11. D  12. F  13. A  14. H  15. B
```

**JSON Output:**
```json
[
  {
    "index": 11,
    "type": "labelling_on_a_map",
    "prompt": "Main entrance",
    "answer_key": "D"
  },
  {
    "index": 12,
    "type": "labelling_on_a_map",
    "prompt": "Library",
    "answer_key": "F"
  },
  {
    "index": 13,
    "type": "labelling_on_a_map",
    "prompt": "Sports center",
    "answer_key": "A"
  }
]
```

### Example 2: Floor Plan
**PDF Input:**
```
Questions 21-24
Label the floor plan.

21. Reception
22. Meeting room
23. Kitchen
24. Office

Answers: 21. E  22. C  23. G  24. B
```

**JSON Output:**
```json
[
  {
    "index": 21,
    "type": "labelling_on_a_map",
    "prompt": "Reception",
    "answer_key": "E"
  },
  {
    "index": 22,
    "type": "labelling_on_a_map",
    "prompt": "Meeting room",
    "answer_key": "C"
  }
]
```

## Common Mistakes to Avoid

### Mistake 1: Using Full Words Instead of Letters
❌ **Wrong:** `"answer_key": "Cafeteria"`
✅ **Correct:** `"answer_key": "C"`

### Mistake 2: Lowercase Letters
❌ **Wrong:** `"answer_key": "c"`
✅ **Correct:** `"answer_key": "C"` (always uppercase)

### Mistake 3: Including "Question" in Prompt
❌ **Wrong:** `"prompt": "11. Cafeteria"`
✅ **Correct:** `"prompt": "Cafeteria"`
