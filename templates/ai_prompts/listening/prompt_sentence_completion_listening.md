# Sentence Completion Listening - Conversion Prompt

## Recognition
When you see these indicators in the PDF:
- "Complete the sentences below"
- "Write NO MORE THAN TWO/THREE WORDS"
- Sentences with blanks at the end or middle
- Usually Section 3 or 4

Use type: `sentence_completion_listening`

## Required Fields
- **index** (integer) - Question number
- **type** (string) - Must be "sentence_completion_listening"
- **prompt** (string) - Sentence with blank (_____)
- **answer_key** (string) - Correct answer

## Optional Fields
- **max_words** (integer) - Maximum words allowed (default: 3)

## JSON Template
```json
{
  "index": 1,
  "type": "sentence_completion_listening",
  "prompt": "The research was funded by _____.",
  "answer_key": "the government",
  "max_words": 2
}
```

## Real Examples

### Example 1: End Completion
**PDF Input:**
```
Questions 31-33
Complete the sentences below.
Write NO MORE THAN TWO WORDS for each answer.

31. The project aims to reduce _____.
32. The team consists of _____.
33. The deadline is _____.

Answers: 31. carbon emissions  32. five researchers  33. next month
```

**JSON Output:**
```json
[
  {
    "index": 31,
    "type": "sentence_completion_listening",
    "prompt": "The project aims to reduce _____.",
    "answer_key": "carbon emissions",
    "max_words": 2
  },
  {
    "index": 32,
    "type": "sentence_completion_listening",
    "prompt": "The team consists of _____.",
    "answer_key": "five researchers",
    "max_words": 2
  },
  {
    "index": 33,
    "type": "sentence_completion_listening",
    "prompt": "The deadline is _____.",
    "answer_key": "next month",
    "max_words": 2
  }
]
```

### Example 2: Middle Completion
**PDF Input:**
```
Questions 25-27
Write NO MORE THAN THREE WORDS.

25. The building, constructed in _____, is a historical landmark.
26. Students who _____ must register by Friday.
27. The library, located on _____, is open daily.

Answers: 25. the 18th century  26. need assistance  27. the third floor
```

**JSON Output:**
```json
[
  {
    "index": 25,
    "type": "sentence_completion_listening",
    "prompt": "The building, constructed in _____, is a historical landmark.",
    "answer_key": "the 18th century",
    "max_words": 3
  },
  {
    "index": 26,
    "type": "sentence_completion_listening",
    "prompt": "Students who _____ must register by Friday.",
    "answer_key": "need assistance",
    "max_words": 3
  }
]
```

## Common Mistakes to Avoid

### Mistake 1: Not Including max_words
❌ **Wrong:** Missing max_words when specified in PDF
✅ **Correct:** Always include max_words from instructions

### Mistake 2: Answer Exceeds Word Limit
❌ **Wrong:** `"answer_key": "the government organization"` when max_words is 2
✅ **Correct:** `"answer_key": "the government"` (2 words)

### Mistake 3: Missing Context in Prompt
❌ **Wrong:** `"prompt": "_____"`
✅ **Correct:** `"prompt": "The research was funded by _____."` (complete sentence)
