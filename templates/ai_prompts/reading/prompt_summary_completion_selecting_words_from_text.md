# Summary Completion Selecting Words from Text - Conversion Prompt

## Recognition
When you see these indicators in the PDF:
- "Complete the summary using words from the passage"
- "Write NO MORE THAN TWO/THREE WORDS from the text"
- Summary paragraph with blanks
- NO word box provided (words come from passage)

Use type: `summary_completion_selecting_words_from_text`

## Required Fields
- **index** (integer) - Question number
- **type** (string) - Must be "summary_completion_selecting_words_from_text"
- **prompt** (string) - Summary sentence with blank
- **answer_key** (string) - Exact words from passage

## Optional Fields
- **max_words** (integer) - Maximum words allowed

## JSON Template
```json
{
  "index": 1,
  "type": "summary_completion_selecting_words_from_text",
  "prompt": "The research focused on _____.",
  "answer_key": "climate change",
  "max_words": 2
}
```

## Real Examples

### Example 1: Passage Summary
**PDF Input:**
```
Questions 19-23
Complete the summary below.
Choose NO MORE THAN TWO WORDS from the passage for each answer.

The ancient civilization developed (19) _____ to irrigate their crops.
Their society was organized around (20) _____ which controlled trade.
The population reached approximately (21) _____ at its peak.
Their decline was caused by (22) _____ and political instability.
Archaeologists discovered (23) _____ that provided valuable insights.

Answers: 19. irrigation systems  20. religious temples  21. 50,000 people  
22. climate change  23. ancient artifacts
```

**JSON Output:**
```json
[
  {
    "index": 19,
    "type": "summary_completion_selecting_words_from_text",
    "prompt": "The ancient civilization developed _____ to irrigate their crops.",
    "answer_key": "irrigation systems",
    "max_words": 2
  },
  {
    "index": 20,
    "type": "summary_completion_selecting_words_from_text",
    "prompt": "Their society was organized around _____ which controlled trade.",
    "answer_key": "religious temples",
    "max_words": 2
  },
  {
    "index": 21,
    "type": "summary_completion_selecting_words_from_text",
    "prompt": "The population reached approximately _____ at its peak.",
    "answer_key": "50,000 people",
    "max_words": 2
  }
]
```

## Common Mistakes to Avoid

### Mistake 1: Confusing with "Selecting from List"
❌ **Wrong:** Using `summary_completion_selecting_from_list` when no word box
✅ **Correct:** Use `summary_completion_selecting_words_from_text` when words come from passage

### Mistake 2: Paraphrasing
❌ **Wrong:** Using different words or synonyms
✅ **Correct:** Use exact words from the passage

### Mistake 3: Exceeding Word Limit
❌ **Wrong:** Answer has 3 words when max_words is 2
✅ **Correct:** Answer must be within word limit

### Mistake 4: Including word_list Field
❌ **Wrong:** Adding `"word_list": [...]` (not needed for this type)
✅ **Correct:** No word_list field (words come from passage, not a list)
