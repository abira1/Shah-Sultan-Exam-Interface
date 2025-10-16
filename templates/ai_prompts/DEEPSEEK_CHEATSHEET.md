# DeepSeek Quick Reference - IELTS Question Converter

## Type Selection Matrix

| PDF Indicator | Question Type | Category |
|--------------|---------------|----------|
| "NO MORE THAN ONE WORD" | `sentence_completion_reading` or `fill_in_the_gaps` | Reading/Listening |
| "NO MORE THAN TWO/THREE WORDS" | `sentence_completion_reading` or `fill_in_the_gaps_short_answers` | Reading/Listening |
| "TRUE/FALSE/NOT GIVEN" | `identifying_information_true_false_not_given` | Reading |
| "YES/NO/NOT GIVEN" | `identifying_information_true_false_not_given` | Reading |
| "Choose correct heading" | `matching_headings` | Reading |
| "Match features" | `matching_features` | Reading |
| "Complete sentence endings" | `matching_sentence_endings` | Reading |
| "Complete from word list" / "box below" | `summary_completion_selecting_from_list` | Reading |
| "Complete from passage" / "words from text" | `summary_completion_selecting_words_from_text` | Reading |
| "Choose TWO letters" | `multiple_choice_more_than_one_answer_*` | Reading/Listening |
| "Choose THREE letters" | `multiple_choice_more_than_one_answer_*` | Reading/Listening |
| "Choose ONE letter A-D" | `multiple_choice_one_answer_*` | Reading/Listening |
| "Label the map/plan" | `labelling_on_a_map` | Listening |
| "Complete the form" | `form_completion` | Listening |
| "Complete the table" (listening) | `table_completion_listening` | Listening |
| "Complete the table" (reading) | `table_completion_reading` | Reading |
| "Complete flowchart" (listening) | `flowchart_completion_listening` | Listening |
| "Complete flowchart" (from text) | `flowchart_completion_selecting_words_from_text` | Reading |
| "Complete notes" | `note_completion` | Reading |
| "At least 150 words" | `writing_part_1` | Writing |
| "At least 250 words" | `writing_part_2` | Writing |

---

## All 24 Question Types - Quick Reference

### LISTENING (10 types)
1. `fill_in_the_gaps` - Single blank, 1 word
2. `fill_in_the_gaps_short_answers` - Multiple blanks
3. `flowchart_completion_listening` - Process from audio
4. `form_completion` - Registration/booking forms
5. `labelling_on_a_map` - Map/plan labeling
6. `matching_listening` - Match items from audio
7. `multiple_choice_more_than_one_answer_listening` - Choose 2-3
8. `multiple_choice_one_answer_listening` - Choose 1
9. `sentence_completion_listening` - Complete sentences
10. `table_completion_listening` - Fill table cells

### READING (12 types)
1. `flowchart_completion_selecting_words_from_text` - Flowchart from passage
2. `identifying_information_true_false_not_given` - TRUE/FALSE/NOT GIVEN
3. `matching_features` - Match to people/places
4. `matching_headings` - Paragraph headings (i, ii, iii)
5. `matching_sentence_endings` - Complete sentences (A-H)
6. `multiple_choice_more_than_one_answer_reading` - Choose 2-3
7. `multiple_choice_one_answer_reading` - Choose 1
8. `note_completion` - Complete notes/outline
9. `sentence_completion_reading` - Complete sentences
10. `summary_completion_selecting_from_list` - From word box
11. `summary_completion_selecting_words_from_text` - From passage
12. `table_completion_reading` - Fill table from text

### WRITING (2 types)
1. `writing_part_1` - Chart/graph/diagram (150+ words)
2. `writing_part_2` - Essay (250+ words)

---

## Field Requirements by Type

### All Question Types
```json
{
  "index": 1,          // Required: Sequential number
  "type": "...",       // Required: Exact type name
  "prompt": "...",     // Required: Question text
  "answer_key": "..."  // Required (except writing)
}
```

### Multiple Choice Types
```json
{
  "options": [         // Required
    {"value": "A", "text": "First option"},
    {"value": "B", "text": "Second option"}
  ],
  "max_choices": 2     // Optional: for "more than one answer" types
}
```

### TRUE/FALSE/NOT GIVEN
```json
{
  "options": [
    {"value": "TRUE", "text": "TRUE"},
    {"value": "FALSE", "text": "FALSE"},
    {"value": "NOT GIVEN", "text": "NOT GIVEN"}
  ]
}
```

### Matching Types
```json
{
  "headings": [...],   // For matching_headings (roman numerals: i, ii, iii)
  "features": [...],   // For matching_features (letters: A, B, C)
  "endings": [...]     // For matching_sentence_endings (letters: A-H)
}
```

### Word Limit Types
```json
{
  "max_words": 2       // For completion questions (1-5)
}
```

### Summary from List
```json
{
  "word_list": ["word1", "word2", "word3"]  // Simple string array
}
```

### Writing Types
```json
{
  "min_words": 150,           // Required (150 for Part 1, 250 for Part 2)
  "chart_image": "https://",  // Optional (Part 1)
  "answer_key": null          // Always null for writing
}
```

---

## Common Conversions - PDF → JSON

### Example 1: Basic Sentence Completion
**PDF:**
```
1. The building was constructed in _____.
Answer: 1990
```

**JSON:**
```json
{
  "index": 1,
  "type": "sentence_completion_reading",
  "prompt": "The building was constructed in _____.",
  "answer_key": "1990",
  "max_words": 1
}
```

---

### Example 2: Multiple Choice Single Answer
**PDF:**
```
2. What is the main purpose?
A. To inform
B. To entertain
C. To persuade
Answer: A
```

**JSON:**
```json
{
  "index": 2,
  "type": "multiple_choice_one_answer_reading",
  "prompt": "What is the main purpose?",
  "answer_key": "A",
  "options": [
    {"value": "A", "text": "To inform"},
    {"value": "B", "text": "To entertain"},
    {"value": "C", "text": "To persuade"}
  ]
}
```

---

### Example 3: TRUE/FALSE/NOT GIVEN
**PDF:**
```
3. The author supports the theory.
Answer: TRUE
```

**JSON:**
```json
{
  "index": 3,
  "type": "identifying_information_true_false_not_given",
  "prompt": "The author supports the theory.",
  "answer_key": "TRUE",
  "options": [
    {"value": "TRUE", "text": "TRUE"},
    {"value": "FALSE", "text": "FALSE"},
    {"value": "NOT GIVEN", "text": "NOT GIVEN"}
  ]
}
```

---

### Example 4: Choose TWO Answers
**PDF:**
```
Questions 15-16
Which TWO benefits are mentioned?
A. Cost savings
B. Improved quality
C. Faster delivery
D. Better safety
E. Increased capacity

Answers: B, D
```

**JSON:**
```json
{
  "index": 15,
  "type": "multiple_choice_more_than_one_answer_reading",
  "prompt": "Which TWO benefits are mentioned?",
  "answer_key": ["B", "D"],
  "max_choices": 2,
  "options": [
    {"value": "A", "text": "Cost savings"},
    {"value": "B", "text": "Improved quality"},
    {"value": "C", "text": "Faster delivery"},
    {"value": "D", "text": "Better safety"},
    {"value": "E", "text": "Increased capacity"}
  ]
}
```

---

### Example 5: Matching Headings
**PDF:**
```
14. Paragraph A

List of Headings:
i. Early development
ii. Modern applications
iii. Future prospects

Answer: i
```

**JSON:**
```json
{
  "index": 14,
  "type": "matching_headings",
  "prompt": "Paragraph A",
  "answer_key": "i",
  "headings": [
    {"value": "i", "text": "Early development"},
    {"value": "ii", "text": "Modern applications"},
    {"value": "iii", "text": "Future prospects"}
  ]
}
```

---

### Example 6: Summary from Word List
**PDF:**
```
36. The study examined the impact of _____ on ecosystems.

Word Box:
A. climate  B. pollution  C. technology

Answer: B
```

**JSON:**
```json
{
  "index": 36,
  "type": "summary_completion_selecting_from_list",
  "prompt": "The study examined the impact of _____ on ecosystems.",
  "answer_key": "pollution",
  "word_list": ["climate", "pollution", "technology"]
}
```

**Important:** Use the actual WORD, not the letter!

---

### Example 7: Form Completion
**PDF:**
```
Complete the form:
1. Name: _____
2. Phone: _____
3. Email: _____

Answers: 1. Sarah Johnson  2. 555-1234  3. sarah@email.com
```

**JSON:**
```json
[
  {
    "index": 1,
    "type": "form_completion",
    "prompt": "Name: _____",
    "answer_key": "Sarah Johnson",
    "max_words": 2
  },
  {
    "index": 2,
    "type": "form_completion",
    "prompt": "Phone: _____",
    "answer_key": "555-1234",
    "max_words": 1
  },
  {
    "index": 3,
    "type": "form_completion",
    "prompt": "Email: _____",
    "answer_key": "sarah@email.com",
    "max_words": 1
  }
]
```

---

### Example 8: Writing Task 1
**PDF:**
```
Writing Task 1

The chart shows milk export figures from 2008 to 2012.
Summarize the information.

Write at least 150 words.
```

**JSON:**
```json
{
  "index": 1,
  "type": "writing_part_1",
  "prompt": "The chart shows milk export figures from 2008 to 2012. Summarize the information by selecting and reporting the main features.",
  "min_words": 150,
  "chart_image": "https://example.com/chart.png",
  "answer_key": null
}
```

---

## Troubleshooting Guide

### Issue 1: Type Name Not Recognized

**Error Message:**
```
Invalid question type: 'true_false'
```

**Cause:** Using shortened or incorrect type name

**Solution:**
Use full exact name: `identifying_information_true_false_not_given`

See complete list of 24 types above.

---

### Issue 2: Options Format Wrong

**Error Message:**
```
Input should be a valid dictionary
```

**Cause:** Options as string array instead of dict array

**❌ Wrong:**
```json
"options": ["A", "B", "C"]
```

**✅ Correct:**
```json
"options": [
  {"value": "A", "text": "First option"},
  {"value": "B", "text": "Second option"}
]
```

**Note:** Backend should auto-convert, but best to use correct format.

---

### Issue 3: Missing answer_key

**Error Message:**
```
answer_key is required
```

**Cause:** Forgot to include answer_key

**Solution:**
Add answer_key for ALL question types EXCEPT:
- `writing_part_1`
- `writing_part_2`

These two should have `"answer_key": null`

---

### Issue 4: Sequential Indices

**Error Message:**
```
Duplicate question indices found
```

**Cause:** Non-sequential or duplicate question numbers

**❌ Wrong:**
```json
{"index": 1}, {"index": 3}, {"index": 5}  // Gaps
{"index": 1}, {"index": 1}, {"index": 2}  // Duplicates
```

**✅ Correct:**
```json
{"index": 1}, {"index": 2}, {"index": 3}  // Sequential
```

---

### Issue 5: answer_key Format for Multiple Answers

**Error Message:**
```
Expected array, got string
```

**Cause:** Multiple answer questions need array format

**❌ Wrong:**
```json
"answer_key": "B, D"
```

**✅ Correct:**
```json
"answer_key": ["B", "D"]
```

Only for `multiple_choice_more_than_one_answer_*` types.

---

### Issue 6: YES/NO/NOT GIVEN Conversion

**Cause:** Some PDFs use YES/NO instead of TRUE/FALSE

**Solution:**
Always convert to TRUE/FALSE/NOT GIVEN:
- YES → TRUE
- NO → FALSE
- NOT GIVEN → NOT GIVEN (stays the same)

**Example:**
```json
{
  "type": "identifying_information_true_false_not_given",
  "answer_key": "TRUE",  // Even if PDF says "YES"
  "options": [
    {"value": "TRUE", "text": "TRUE"},
    {"value": "FALSE", "text": "FALSE"},
    {"value": "NOT GIVEN", "text": "NOT GIVEN"}
  ]
}
```

---

### Issue 7: Word List vs Letter Answer

**For summary_completion_selecting_from_list:**

**❌ Wrong:**
```json
"answer_key": "B"  // Letter from word box
```

**✅ Correct:**
```json
"answer_key": "pollution"  // Actual word
"word_list": ["climate", "pollution", "technology"]
```

Use the WORD itself, not the letter label!

---

### Issue 8: Roman Numerals Format

**For matching_headings:**

**❌ Wrong:**
```json
"answer_key": "III"  // Uppercase
"answer_key": "3"    // Number
```

**✅ Correct:**
```json
"answer_key": "iii"  // Lowercase roman numeral
```

Always use lowercase: i, ii, iii, iv, v, vi, vii, viii, ix, x

---

### Issue 9: Missing Blank in Prompt

**❌ Wrong:**
```json
"prompt": "The building was constructed in 1990."
```

**✅ Correct:**
```json
"prompt": "The building was constructed in _____."
```

For completion types, always include the blank (_____)

---

### Issue 10: Passage Text Missing

**Error Message:**
```
passage_text required for reading tests
```

**Cause:** Reading test without passage text

**Solution:**
For `test_type: "reading"`, each section must have:
```json
"passage_text": "A\nFirst paragraph...\n\nB\nSecond paragraph..."
```

Include full passage with paragraph markers (A, B, C, etc.)

---

## Quick Decision Tree

```
START: Look at PDF question

├─ "NO MORE THAN X WORDS"?
│  ├─ From listening → fill_in_the_gaps or fill_in_the_gaps_short_answers
│  └─ From passage → sentence_completion_reading or note_completion
│
├─ "TRUE/FALSE/NOT GIVEN"?
│  └─ identifying_information_true_false_not_given
│
├─ "Choose correct heading"?
│  └─ matching_headings (use roman numerals: i, ii, iii)
│
├─ "Match features/people/places"?
│  └─ matching_features
│
├─ "Complete sentence endings"?
│  └─ matching_sentence_endings
│
├─ "Choose TWO/THREE letters"?
│  ├─ Listening → multiple_choice_more_than_one_answer_listening
│  └─ Reading → multiple_choice_more_than_one_answer_reading
│
├─ "Choose ONE letter"?
│  ├─ Listening → multiple_choice_one_answer_listening
│  └─ Reading → multiple_choice_one_answer_reading
│
├─ "Complete from word box/list"?
│  └─ summary_completion_selecting_from_list
│
├─ "Complete from passage/text"?
│  └─ summary_completion_selecting_words_from_text
│
├─ "Label the map/plan"?
│  └─ labelling_on_a_map
│
├─ "Complete the form"?
│  └─ form_completion
│
├─ "Complete the table"?
│  ├─ Listening → table_completion_listening
│  └─ Reading → table_completion_reading
│
├─ "Complete flowchart"?
│  ├─ Listening → flowchart_completion_listening
│  └─ Reading → flowchart_completion_selecting_words_from_text
│
├─ "At least 150 words"?
│  └─ writing_part_1
│
└─ "At least 250 words"?
   └─ writing_part_2
```

---

## Quick Check Before Submit

✅ **test_type** is "listening", "reading", or "writing"

✅ **All types** match exact names from the 24-type list

✅ **Questions numbered** 1, 2, 3... sequentially (no gaps)

✅ **answer_key** present for all except writing_part_1 and writing_part_2

✅ **options** format is array of objects: `[{"value": "A", "text": "..."}]`

✅ **Valid JSON** (no missing commas/brackets)

✅ **passage_text** included for reading tests

✅ **audio_url** included for listening tests

✅ **Blanks (_____)** included in prompts for completion questions

✅ **Word limits** specified when mentioned in PDF (max_words)

✅ **All options/headings/features** included from PDF list

---

## Field Naming Cheat Sheet

| Question Type | Special Field | Format |
|--------------|---------------|--------|
| Multiple choice | `options` | `[{"value": "A", "text": "..."}]` |
| TRUE/FALSE/NOT GIVEN | `options` | Always same 3 options |
| Matching headings | `headings` | `[{"value": "i", "text": "..."}]` |
| Matching features | `features` | `[{"value": "A", "text": "..."}]` |
| Matching sentence endings | `endings` | `[{"value": "A", "text": "..."}]` |
| Summary from list | `word_list` | `["word1", "word2", ...]` |
| Completion questions | `max_words` | Integer (1-5) |
| Writing tasks | `min_words` | 150 or 250 |
| Writing Part 1 | `chart_image` | URL string |

---

## Common PDF Keywords → Type

| PDF Says | Use This Type |
|----------|---------------|
| "Write NO MORE THAN" | Check if listening or reading completion |
| "TRUE/FALSE/NOT GIVEN" | `identifying_information_true_false_not_given` |
| "Choose correct heading" | `matching_headings` |
| "Match each statement" | `matching_features` |
| "Complete sentence" | `matching_sentence_endings` (if choosing endings) |
| "Choose from the box" | `summary_completion_selecting_from_list` |
| "words from the passage" | Check if summary, sentence, or note completion |
| "Choose TWO/THREE" | `multiple_choice_more_than_one_answer_*` |
| "Label the map" | `labelling_on_a_map` |
| "Complete the form" | `form_completion` |
| "Complete the table" | `table_completion_*` |
| "Flowchart" | `flowchart_completion_*` |
| "150 words" | `writing_part_1` |
| "250 words" | `writing_part_2` |

---

## Pro Tips

1. **Copy-paste carefully:** Type names must be EXACT (no typos)

2. **Roman numerals:** Always lowercase for headings (i, ii, iii)

3. **Letters:** Always uppercase for options (A, B, C)

4. **Word lists:** Use actual words, not letters

5. **Sequential indices:** Start at 1, no gaps

6. **Blanks:** Always include _____ in completion prompts

7. **Writing:** Always `"answer_key": null`

8. **Arrays:** Use `["A", "B"]` not `"A, B"` for multiple answers

9. **Options:** Always `[{"value": "A", "text": "..."}]` format

10. **Test type:** Must be exactly "listening", "reading", or "writing"
