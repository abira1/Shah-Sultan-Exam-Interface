# Fill in the Gaps Short Answers - Conversion Prompt

## Recognition
When you see these indicators in the PDF:
- Multiple blanks in a paragraph or passage
- "Complete the notes below"
- "Fill in the gaps in the summary"
- Several short answers required
- Usually Section 2 or 3

Use type: `fill_in_the_gaps_short_answers`

## Required Fields
- **index** (integer) - Question number
- **type** (string) - Must be "fill_in_the_gaps_short_answers"
- **prompt** (string) - Text with multiple blanks
- **answer_key** (array of strings) - Array of correct answers

## Optional Fields
- **max_words** (integer) - Maximum words per blank (default: 2)
- **blanks_count** (integer) - Number of blanks

## JSON Template
```json
{
  "index": 1,
  "type": "fill_in_the_gaps_short_answers",
  "prompt": "Name: _____\nAge: _____\nCity: _____",
  "answer_key": ["John Smith", "25", "London"],
  "max_words": 2
}
```

## Real Examples

### Example 1: Form Completion Style
**PDF Input:**
```
Questions 1-3
Complete the registration form below.

1. First name: _____
2. Phone number: _____
3. Email address: _____

Answers: 1. Sarah  2. 555-1234  3. sarah@email.com
```

**JSON Output:**
```json
{
  "index": 1,
  "type": "fill_in_the_gaps_short_answers",
  "prompt": "First name: _____\nPhone number: _____\nEmail address: _____",
  "answer_key": ["Sarah", "555-1234", "sarah@email.com"],
  "max_words": 2
}
```

### Example 2: Summary Completion
**PDF Input:**
```
Questions 4-6
Complete the summary.

The conference will be held in _____ (4) in the month of _____ (5). 
Participants should register by _____ (6).

Answers: 4. Sydney  5. November  6. October 15th
```

**JSON Output:**
```json
{
  "index": 4,
  "type": "fill_in_the_gaps_short_answers",
  "prompt": "The conference will be held in _____ in the month of _____. Participants should register by _____.",
  "answer_key": ["Sydney", "November", "October 15th"],
  "max_words": 2
}
```

## Common Mistakes to Avoid

### Mistake 1: Single String Instead of Array
❌ **Wrong:** `"answer_key": "John, 25, London"`
✅ **Correct:** `"answer_key": ["John", "25", "London"]`

### Mistake 2: Wrong Number of Answers
❌ **Wrong:** 3 blanks but only 2 answers in array
✅ **Correct:** Number of answers must match number of blanks

### Mistake 3: Using Wrong Type
❌ **Wrong:** Using `fill_in_the_gaps` for multiple blanks
✅ **Correct:** Use `fill_in_the_gaps_short_answers` for multiple blanks
