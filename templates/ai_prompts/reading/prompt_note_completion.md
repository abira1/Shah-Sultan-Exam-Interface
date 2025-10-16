# Note Completion - Conversion Prompt

## Recognition
When you see these indicators in the PDF:
- "Complete the notes below"
- "Write NO MORE THAN TWO/THREE WORDS from the passage"
- Notes format (bullet points, indented structure)
- Summary or outline to complete

Use type: `note_completion`

## Required Fields
- **index** (integer) - Question number
- **type** (string) - Must be "note_completion"
- **prompt** (string) - Note context with blank
- **answer_key** (string) - Words from passage

## Optional Fields
- **max_words** (integer) - Maximum words allowed

## JSON Template
```json
{
  "index": 1,
  "type": "note_completion",
  "prompt": "Main topic: _____",
  "answer_key": "climate change",
  "max_words": 2
}
```

## Real Examples

### Example 1: Structured Notes
**PDF Input:**
```
Questions 32-35
Complete the notes below.
Choose NO MORE THAN TWO WORDS from the passage for each answer.

Research Project Notes:
- Topic: (32) _____
- Duration: (33) _____
- Location: (34) _____  
- Participants: (35) _____

Answers: 32. urban development  33. three years  34. coastal regions  35. local communities
```

**JSON Output:**
```json
[
  {
    "index": 32,
    "type": "note_completion",
    "prompt": "Topic: _____",
    "answer_key": "urban development",
    "max_words": 2
  },
  {
    "index": 33,
    "type": "note_completion",
    "prompt": "Duration: _____",
    "answer_key": "three years",
    "max_words": 2
  },
  {
    "index": 34,
    "type": "note_completion",
    "prompt": "Location: _____",
    "answer_key": "coastal regions",
    "max_words": 2
  }
]
```

## Common Mistakes to Avoid

### Mistake 1: Answer Not From Passage
❌ **Wrong:** Paraphrasing with different words
✅ **Correct:** Use exact words from passage

### Mistake 2: Exceeding Word Limit
❌ **Wrong:** `"answer_key": "the three year period"` (4 words when max is 2)
✅ **Correct:** `"answer_key": "three years"` (2 words)
