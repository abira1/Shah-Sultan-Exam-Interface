# Form Completion - Conversion Prompt

## Recognition
When you see these indicators in the PDF:
- "Complete the form below"
- Structured form layout with fields
- Personal information, registration, booking forms
- Usually Section 1

Use type: `form_completion`

## Required Fields
- **index** (integer) - Question number
- **type** (string) - Must be "form_completion"
- **prompt** (string) - Form field label
- **answer_key** (string) - Correct answer

## Optional Fields
- **max_words** (integer) - Maximum words allowed
- **field_type** (string) - Type of form field (name, date, number, etc.)

## JSON Template
```json
{
  "index": 1,
  "type": "form_completion",
  "prompt": "Full name: _____",
  "answer_key": "John Smith",
  "max_words": 2
}
```

## Real Examples

### Example 1: Registration Form
**PDF Input:**
```
Questions 1-5
Complete the registration form.

1. Name: _____
2. Date of birth: _____
3. Nationality: _____
4. Occupation: _____
5. Contact number: _____

Answers: 1. Maria Garcia  2. 15 March 1995  3. Spanish  4. teacher  5. 555-7890
```

**JSON Output:**
```json
[
  {
    "index": 1,
    "type": "form_completion",
    "prompt": "Name: _____",
    "answer_key": "Maria Garcia",
    "max_words": 2
  },
  {
    "index": 2,
    "type": "form_completion",
    "prompt": "Date of birth: _____",
    "answer_key": "15 March 1995",
    "max_words": 3
  },
  {
    "index": 3,
    "type": "form_completion",
    "prompt": "Nationality: _____",
    "answer_key": "Spanish",
    "max_words": 1
  }
]
```

## Common Mistakes to Avoid

### Mistake 1: Including Form Title in Every Prompt
❌ **Wrong:** `"prompt": "Registration Form - Name: _____"`
✅ **Correct:** `"prompt": "Name: _____"`

### Mistake 2: Not Preserving Field Labels
❌ **Wrong:** `"prompt": "_____"` (missing context)
✅ **Correct:** `"prompt": "Name: _____"` (includes field label)
