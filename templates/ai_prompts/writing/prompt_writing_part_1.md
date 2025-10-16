# Writing Part 1 - Conversion Prompt

## Recognition
When you see these indicators in the PDF:
- "Write at least 150 words"
- "Spend about 20 minutes on this task"
- Chart, graph, diagram, table, or process description
- "Summarize the information"
- "Describe the main features"
- Writing Task 1

Use type: `writing_part_1`

## Required Fields
- **index** (integer) - Question number (usually 1)
- **type** (string) - Must be "writing_part_1"
- **prompt** (string) - Task description and instructions
- **min_words** (integer) - Minimum word count (usually 150)
- **answer_key** (null) - Always null for writing tasks

## Optional Fields
- **chart_image** (string) - URL to chart/graph/diagram image
- **instructions** (string) - Additional task instructions
- **task_type** (string) - Type of visual (chart, graph, table, process, map)

## JSON Template
```json
{
  "index": 1,
  "type": "writing_part_1",
  "prompt": "The chart below shows the percentage of households in owned and rented accommodation in England and Wales between 1918 and 2011. Summarize the information by selecting and reporting the main features, and make comparisons where relevant.",
  "min_words": 150,
  "chart_image": "https://example.com/chart.png",
  "answer_key": null
}
```

## Real Examples

### Example 1: Bar Chart
**PDF Input:**
```
Writing Task 1

You should spend about 20 minutes on this task.

The chart below shows the amount of money per week spent on fast foods in Britain.
The graph shows the trends in consumption of fast foods.

Summarise the information by selecting and reporting the main features, and make
comparisons where relevant.

Write at least 150 words.

[Chart image showing bar graph]
```

**JSON Output:**
```json
{
  "index": 1,
  "type": "writing_part_1",
  "prompt": "The chart below shows the amount of money per week spent on fast foods in Britain. The graph shows the trends in consumption of fast foods. Summarise the information by selecting and reporting the main features, and make comparisons where relevant.",
  "min_words": 150,
  "chart_image": "https://example.com/fast-food-chart.png",
  "task_type": "bar_chart",
  "answer_key": null
}
```

### Example 2: Process Diagram
**PDF Input:**
```
Writing Task 1

You should spend about 20 minutes on this task.

The diagram below shows the process of recycling plastic bottles.

Summarise the information by selecting and reporting the main features.

Write at least 150 words.

[Diagram showing recycling process]
```

**JSON Output:**
```json
{
  "index": 1,
  "type": "writing_part_1",
  "prompt": "The diagram below shows the process of recycling plastic bottles. Summarise the information by selecting and reporting the main features.",
  "min_words": 150,
  "chart_image": "https://example.com/recycling-diagram.png",
  "task_type": "process",
  "answer_key": null
}
```

### Example 3: Table
**PDF Input:**
```
Writing Task 1

You should spend about 20 minutes on this task.

The table below gives information about the underground railway systems in six cities.

Summarise the information by selecting and reporting the main features, and make
comparisons where relevant.

Write at least 150 words.

[Table with railway data]
```

**JSON Output:**
```json
{
  "index": 1,
  "type": "writing_part_1",
  "prompt": "The table below gives information about the underground railway systems in six cities. Summarise the information by selecting and reporting the main features, and make comparisons where relevant.",
  "min_words": 150,
  "chart_image": "https://example.com/railway-table.png",
  "task_type": "table",
  "answer_key": null
}
```

### Example 4: Map Comparison
**PDF Input:**
```
Writing Task 1

You should spend about 20 minutes on this task.

The two maps below show an island, before and after the construction of some tourist facilities.

Summarise the information by selecting and reporting the main features, and make
comparisons where relevant.

Write at least 150 words.

[Two maps showing before and after]
```

**JSON Output:**
```json
{
  "index": 1,
  "type": "writing_part_1",
  "prompt": "The two maps below show an island, before and after the construction of some tourist facilities. Summarise the information by selecting and reporting the main features, and make comparisons where relevant.",
  "min_words": 150,
  "chart_image": "https://example.com/island-maps.png",
  "task_type": "map",
  "answer_key": null
}
```

## Common Mistakes to Avoid

### Mistake 1: Including Answer Key
❌ **Wrong:** `"answer_key": "sample essay text"`
✅ **Correct:** `"answer_key": null` (writing tasks don't have answer keys)

### Mistake 2: Wrong Word Count
❌ **Wrong:** `"min_words": 250` (this is for Task 2)
✅ **Correct:** `"min_words": 150` (Task 1 requires 150+ words)

### Mistake 3: Using "writing_task_1"
❌ **Wrong:** `"type": "writing_task_1"`
✅ **Correct:** `"type": "writing_part_1"`

### Mistake 4: Not Including Full Task Instructions
❌ **Wrong:** Only including "Describe the chart"
✅ **Correct:** Include full prompt with all instructions from PDF

## Task Type Variations
- **Line graph:** Shows trends over time
- **Bar chart:** Compares quantities
- **Pie chart:** Shows proportions/percentages
- **Table:** Presents data in rows and columns
- **Process diagram:** Shows steps in a process
- **Map:** Shows location/layout changes
- **Multiple visuals:** Combination of two or more charts/graphs

## Grading
Writing Task 1 is NOT auto-graded. It requires manual evaluation based on:
- Task Achievement
- Coherence and Cohesion
- Lexical Resource
- Grammatical Range and Accuracy

Therefore, `answer_key` should always be `null`.
