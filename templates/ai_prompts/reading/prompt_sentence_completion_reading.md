# Sentence Completion Reading - Conversion Prompt

## Recognition
When you see these indicators in the PDF:
- "Complete the sentences below"
- "Write NO MORE THAN TWO/THREE WORDS from the passage"
- Sentences with blanks to fill
- Words must come from the text

Use type: `sentence_completion_reading`

## Required Fields
- **index** (integer) - Question number
- **type** (string) - Must be "sentence_completion_reading"
- **prompt** (string) - Sentence with blank
- **answer_key** (string) - Exact words from passage

## Optional Fields
- **max_words** (integer) - Maximum words allowed

## JSON Template
```json
{
  "index": 1,
  "type": "sentence_completion_reading",
  "prompt": "The building was constructed using _____.",
  "answer_key": "local materials",
  "max_words": 2
}
```

## Real Examples

### Example 1: Standard Completion
**PDF Input:**
```
Questions 4-7
Complete the sentences below.
Choose NO MORE THAN THREE WORDS from the passage for each answer.

4. The researchers found evidence of _____.
5. The study was funded by _____.
6. Results were published in _____.
7. The main conclusion was that _____.

Answers: 4. ancient civilizations  5. the government  6. 2019  7. climate affects behavior
```

**JSON Output:**
```json
[
  {
    "index": 4,
    "type": "sentence_completion_reading",
    "prompt": "The researchers found evidence of _____.",
    "answer_key": "ancient civilizations",
    "max_words": 3
  },
  {
    "index": 5,
    "type": "sentence_completion_reading",
    "prompt": "The study was funded by _____.",
    "answer_key": "the government",
    "max_words": 3
  },
  {
    "index": 6,
    "type": "sentence_completion_reading",
    "prompt": "Results were published in _____.",
    "answer_key": "2019",
    "max_words": 3
  }
]
```

## Common Mistakes to Avoid

### Mistake 1: Paraphrasing
❌ **Wrong:** Using synonyms or different words
✅ **Correct:** Use exact words from passage

### Mistake 2: Exceeding Word Limit
❌ **Wrong:** Answer has more words than max_words allows
✅ **Correct:** Answer must be within word limit

### Mistake 3: Missing Blank
❌ **Wrong:** `"prompt": "The building was constructed using local materials."`
✅ **Correct:** `"prompt": "The building was constructed using _____."` (includes blank)
