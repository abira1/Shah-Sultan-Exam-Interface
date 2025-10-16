# Writing Part 2 - Conversion Prompt

## Recognition
When you see these indicators in the PDF:
- "Write at least 250 words"
- "Spend about 40 minutes on this task"
- Essay question
- "Give reasons for your answer"
- "Include relevant examples"
- "To what extent do you agree or disagree?"
- "Discuss both views and give your opinion"
- Writing Task 2

Use type: `writing_part_2`

## Required Fields
- **index** (integer) - Question number (usually 2)
- **type** (string) - Must be "writing_part_2"
- **prompt** (string) - Essay question and instructions
- **min_words** (integer) - Minimum word count (usually 250)
- **answer_key** (null) - Always null for writing tasks

## Optional Fields
- **essay_type** (string) - Type of essay (opinion, discussion, problem-solution, advantages-disadvantages)
- **instructions** (string) - Additional task instructions

## JSON Template
```json
{
  "index": 2,
  "type": "writing_part_2",
  "prompt": "Some people believe that international news should be included in subjects that children study at school. Others think this is a waste of school time. Discuss both views and give your own opinion. Give reasons for your answer and include any relevant examples from your own knowledge or experience.",
  "min_words": 250,
  "essay_type": "discussion",
  "answer_key": null
}
```

## Real Examples

### Example 1: Opinion Essay (Agree/Disagree)
**PDF Input:**
```
Writing Task 2

You should spend about 40 minutes on this task.

Write about the following topic:

Some people think that all university students should study whatever they like.
Others believe that they should only be allowed to study subjects that will be
useful in the future, such as those related to science and technology.

Discuss both these views and give your own opinion.

Give reasons for your answer and include any relevant examples from your own
knowledge or experience.

Write at least 250 words.
```

**JSON Output:**
```json
{
  "index": 2,
  "type": "writing_part_2",
  "prompt": "Some people think that all university students should study whatever they like. Others believe that they should only be allowed to study subjects that will be useful in the future, such as those related to science and technology. Discuss both these views and give your own opinion. Give reasons for your answer and include any relevant examples from your own knowledge or experience.",
  "min_words": 250,
  "essay_type": "discussion",
  "answer_key": null
}
```

### Example 2: Problem-Solution Essay
**PDF Input:**
```
Writing Task 2

You should spend about 40 minutes on this task.

Write about the following topic:

Many cities around the world are facing serious air pollution problems.

What are the causes of this?
What solutions can you suggest?

Give reasons for your answer and include any relevant examples from your own
knowledge or experience.

Write at least 250 words.
```

**JSON Output:**
```json
{
  "index": 2,
  "type": "writing_part_2",
  "prompt": "Many cities around the world are facing serious air pollution problems. What are the causes of this? What solutions can you suggest? Give reasons for your answer and include any relevant examples from your own knowledge or experience.",
  "min_words": 250,
  "essay_type": "problem_solution",
  "answer_key": null
}
```

### Example 3: Advantages-Disadvantages Essay
**PDF Input:**
```
Writing Task 2

You should spend about 40 minutes on this task.

Write about the following topic:

In some countries, people are choosing to have children at a later age than in
the past.

Why is this?
Do the advantages of this development outweigh the disadvantages?

Give reasons for your answer and include any relevant examples from your own
knowledge or experience.

Write at least 250 words.
```

**JSON Output:**
```json
{
  "index": 2,
  "type": "writing_part_2",
  "prompt": "In some countries, people are choosing to have children at a later age than in the past. Why is this? Do the advantages of this development outweigh the disadvantages? Give reasons for your answer and include any relevant examples from your own knowledge or experience.",
  "min_words": 250,
  "essay_type": "advantages_disadvantages",
  "answer_key": null
}
```

### Example 4: Direct Opinion Essay
**PDF Input:**
```
Writing Task 2

You should spend about 40 minutes on this task.

Write about the following topic:

Some people believe that unpaid community service should be a compulsory part
of high school programmes (for example working for a charity, improving the
neighbourhood or teaching sports to younger children).

To what extent do you agree or disagree?

Give reasons for your answer and include any relevant examples from your own
knowledge or experience.

Write at least 250 words.
```

**JSON Output:**
```json
{
  "index": 2,
  "type": "writing_part_2",
  "prompt": "Some people believe that unpaid community service should be a compulsory part of high school programmes (for example working for a charity, improving the neighbourhood or teaching sports to younger children). To what extent do you agree or disagree? Give reasons for your answer and include any relevant examples from your own knowledge or experience.",
  "min_words": 250,
  "essay_type": "opinion",
  "answer_key": null
}
```

## Common Mistakes to Avoid

### Mistake 1: Including Answer Key
❌ **Wrong:** `"answer_key": "sample essay text"`
✅ **Correct:** `"answer_key": null` (writing tasks don't have answer keys)

### Mistake 2: Wrong Word Count
❌ **Wrong:** `"min_words": 150` (this is for Task 1)
✅ **Correct:** `"min_words": 250` (Task 2 requires 250+ words)

### Mistake 3: Using "writing_task_2"
❌ **Wrong:** `"type": "writing_task_2"`
✅ **Correct:** `"type": "writing_part_2"`

### Mistake 4: Not Including Full Instructions
❌ **Wrong:** Only including main question
✅ **Correct:** Include all instructions: question + "Give reasons..." + "Write at least 250 words"

## Essay Type Identification

### Opinion Essay (Agree/Disagree)
**Indicators:**
- "To what extent do you agree or disagree?"
- "Do you agree or disagree?"
- Requires your position on a single viewpoint

### Discussion Essay
**Indicators:**
- "Discuss both views and give your opinion"
- "Discuss both sides"
- Presents two opposing views

### Problem-Solution Essay
**Indicators:**
- "What are the causes?"
- "What are the problems?"
- "What solutions can you suggest?"
- "How can this be addressed?"

### Advantages-Disadvantages Essay
**Indicators:**
- "Do the advantages outweigh the disadvantages?"
- "What are the advantages and disadvantages?"
- Requires balanced evaluation

### Two-Part Question Essay
**Indicators:**
- Two distinct questions asked
- "Why is this? What can be done?"
- Must answer both parts

## Grading
Writing Task 2 is NOT auto-graded. It requires manual evaluation based on:
- Task Response
- Coherence and Cohesion
- Lexical Resource
- Grammatical Range and Accuracy

Therefore, `answer_key` should always be `null`.

## Word Count
- Task 2 counts for DOUBLE the marks of Task 1
- Minimum 250 words (recommended 270-290)
- Penalties for under-length essays
- No maximum word limit, but typically 250-350 words
