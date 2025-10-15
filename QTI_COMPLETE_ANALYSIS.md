# Complete QTI Question Types Analysis
## Source: `/app/Question type/` folders

**Total Question Types: 24**
- Listening: 10 types
- Reading: 12 types
- Writing: 2 types

---

## 🎧 LISTENING QUESTION TYPES (10)

### 1. fill_in_the_gaps
**Source Folder:** `Listening/Fill in the gaps/`
**Description:** Complete notes/tables by filling blank fields with text input
**HTML Structure:**
```html
<input connect:responseIdentifier="RESPONSE_ID" size="10" type="text"/>
```
**Answer Format:** 
- Single string per blank
- `cardinality="single"`, `baseType="string"`
- Instructions: "Write ONE WORD AND/OR A NUMBER in each gap"
**Max Words:** Usually 1-2 words per blank
**Example:** Table/form completion with inline text inputs

---

### 2. fill_in_the_gaps_short_answers
**Source Folder:** `Listening/Fill in the gaps short answers/`
**Description:** Similar to fill_in_the_gaps but focused on short factual answers
**HTML Structure:**
```html
<input connect:responseIdentifier="RESPONSE_ID" size="10" type="text"/>
```
**Answer Format:**
- Single string per answer
- `cardinality="single"`, `baseType="string"`
- Instructions: "Write NO MORE THAN TWO WORDS"
**Max Words:** 1-2 words
**Example:** Direct question-answer format

---

### 3. flowchart_completion_listening
**Source Folder:** `Listening/Flow-chart Completion/`
**Description:** Complete a flowchart/diagram by filling in missing labels/text
**HTML Structure:**
```html
<input connect:responseIdentifier="RESPONSE_ID" size="10" type="text"/>
<!-- Usually embedded in flowchart diagram/image -->
```
**Answer Format:**
- Single string per blank
- `cardinality="single"`, `baseType="string"`
- Instructions: "Write NO MORE THAN TWO WORDS"
**Visual:** Flowchart image with numbered blanks
**Max Words:** 1-2 words per blank

---

### 4. form_completion
**Source Folder:** `Listening/Form Completion/`
**Description:** Fill out a form with personal/factual information
**HTML Structure:**
```html
<table>
  <tr>
    <td>Label:</td>
    <td><input type="text" connect:responseIdentifier="RESPONSE_ID"/></td>
  </tr>
</table>
```
**Answer Format:**
- Single string per field
- `cardinality="single"`, `baseType="string"`
- Instructions: "Write NO MORE THAN THREE WORDS AND/OR A NUMBER"
**Fields:** Name, date, address, phone, etc.
**Max Words:** 1-3 words per field

---

### 5. labelling_on_a_map
**Source Folder:** `Listening/Labelling on a map/`
**Description:** Label locations on a map diagram
**HTML Structure:**
```html
<img src="map.png"/>
<div>
  <span class="questionNumber">1</span>
  <input type="text" connect:responseIdentifier="RESPONSE_ID"/>
</div>
```
**Answer Format:**
- Single string per location
- `cardinality="single"`, `baseType="string"`
- Usually building names, place names, or location types
**Visual:** Map image with numbered labels pointing to locations
**Max Words:** 1-3 words per label

---

### 6. matching_listening
**Source Folder:** `Listening/Matching/`
**Description:** Match items from two lists (e.g., people to opinions, places to features)
**HTML Structure:**
```html
<select connect:responseIdentifier="RESPONSE_ID">
  <option value="">Please select</option>
  <option value="A">Option A text</option>
  <option value="B">Option B text</option>
  <option value="C">Option C text</option>
</select>
```
**Answer Format:**
- Single letter per match
- `cardinality="single"`, `baseType="identifier"`
- Answer key: Letter (A, B, C, D, E, F, etc.)
**Pattern:** List of questions + dropdown of answer options
**Example:** Match speakers to statements

---

### 7. multiple_choice_more_than_one_answer_listening
**Source Folder:** `Listening/Multiple Choice (more than one answer)/`
**Description:** Choose multiple correct answers from options
**HTML Structure:**
```html
<ul>
  <li><label><input type="checkbox" value="A"/><p>Option A</p></label></li>
  <li><label><input type="checkbox" value="B"/><p>Option B</p></label></li>
  <li><label><input type="checkbox" value="C"/><p>Option C</p></label></li>
</ul>
```
**Answer Format:**
- Array of letters
- `cardinality="multiple"`, `baseType="identifier"`
- Answer key: Array like ["A", "C", "E"]
**Instructions:** "Choose TWO/THREE letters"
**Typical:** 2-3 correct answers from 5-7 options

---

### 8. multiple_choice_one_answer_listening
**Source Folder:** `Listening/Multiple Choice (one answer)/`
**Description:** Choose one correct answer from options
**HTML Structure:**
```html
<ul>
  <li><label><input type="radio" name="Q1" value="A"/><p>Option A</p></label></li>
  <li><label><input type="radio" name="Q1" value="B"/><p>Option B</p></label></li>
  <li><label><input type="radio" name="Q1" value="C"/><p>Option C</p></label></li>
</ul>
```
**Answer Format:**
- Single letter
- `cardinality="single"`, `baseType="identifier"`
- Answer key: Single letter like "B"
**Typical:** 3-4 options (A, B, C, D)

---

### 9. sentence_completion_listening
**Source Folder:** `Listening/Sentence Completion/`
**Description:** Complete sentences with missing words from audio
**HTML Structure:**
```html
<p>The building was completed in <input type="text" connect:responseIdentifier="RESPONSE_ID" size="10"/>.</p>
```
**Answer Format:**
- Single string per blank
- `cardinality="single"`, `baseType="string"`
- Instructions: "Write NO MORE THAN TWO WORDS"
**Pattern:** Incomplete sentences with inline text inputs
**Max Words:** 1-2 words per blank

---

### 10. table_completion_listening
**Source Folder:** `Listening/Table Completion/`
**Description:** Fill in missing information in a table
**HTML Structure:**
```html
<table>
  <tr>
    <td>Category</td>
    <td><input type="text" connect:responseIdentifier="RESPONSE_ID"/></td>
  </tr>
</table>
```
**Answer Format:**
- Single string per cell
- `cardinality="single"`, `baseType="string"`
- Instructions: "Write NO MORE THAN TWO WORDS AND/OR A NUMBER"
**Pattern:** Table with some cells filled, others blank for answers
**Max Words:** 1-3 words per cell

---

## 📖 READING QUESTION TYPES (12)

### 11. flowchart_completion_selecting_words_from_text
**Source Folder:** `Reading/Flow-chart Completion (selecting words from the text)/`
**Description:** Complete flowchart by selecting words directly from passage
**HTML Structure:**
```html
<input type="text" connect:responseIdentifier="RESPONSE_ID" size="15"/>
<!-- Flowchart diagram with numbered blanks -->
```
**Answer Format:**
- Single string per blank
- `cardinality="single"`, `baseType="string"`
- Instructions: "Choose NO MORE THAN TWO WORDS from the passage"
**Constraint:** Must use exact words from reading passage
**Max Words:** 1-2 words per blank

---

### 12. identifying_information_true_false_not_given
**Source Folder:** `Reading/Identifying Information (TrueFalseNot Given)/`
**Description:** Determine if statements are TRUE, FALSE, or NOT GIVEN based on passage
**HTML Structure:**
```html
<ul>
  <li><label><input type="radio" name="Q1" value="A"/><p>TRUE</p></label></li>
  <li><label><input type="radio" name="Q1" value="B"/><p>FALSE</p></label></li>
  <li><label><input type="radio" name="Q1" value="C"/><p>NOT GIVEN</p></label></li>
</ul>
```
**Answer Format:**
- Single letter (A=TRUE, B=FALSE, C=NOT GIVEN)
- `cardinality="single"`, `baseType="identifier"`
- Answer key: "A" or "B" or "C"
**Pattern:** Statement + 3 radio options

---

### 13. matching_features
**Source Folder:** `Reading/Matching Features/`
**Description:** Match features/characteristics to items (e.g., researchers to findings)
**HTML Structure:**
```html
<select connect:responseIdentifier="RESPONSE_ID">
  <option value="">Please select</option>
  <option value="A">Feature A</option>
  <option value="B">Feature B</option>
  <option value="C">Feature C</option>
</select>
```
**Answer Format:**
- Single letter per match
- `cardinality="single"`, `baseType="identifier"`
- Answer key: Letter (A-G typically)
**Pattern:** List of items + dropdown of features to match
**Example:** Match scientists to their discoveries

---

### 14. matching_headings
**Source Folder:** `Reading/Matching Headings/`
**Description:** Match paragraph headings to paragraphs
**HTML Structure:**
```html
<select connect:responseIdentifier="RESPONSE_ID">
  <option value="">Please select</option>
  <option value="i">Heading i</option>
  <option value="ii">Heading ii</option>
  <option value="iii">Heading iii</option>
</select>
```
**Answer Format:**
- Single roman numeral (i, ii, iii, iv, v, vi, vii, viii, etc.)
- `cardinality="single"`, `baseType="identifier"`
- Answer key: Roman numeral like "iv"
**Pattern:** List of paragraphs + dropdown of heading options
**Options:** Usually 8-10 headings for 5-7 paragraphs

---

### 15. matching_sentence_endings
**Source Folder:** `Reading/Matching Sentence Endings/`
**Description:** Match sentence beginnings to appropriate endings
**HTML Structure:**
```html
<select connect:responseIdentifier="RESPONSE_ID">
  <option value="">Please select</option>
  <option value="A">Ending A text...</option>
  <option value="B">Ending B text...</option>
  <option value="C">Ending C text...</option>
</select>
```
**Answer Format:**
- Single letter per match
- `cardinality="single"`, `baseType="identifier"`
- Answer key: Letter (A-H typically)
**Pattern:** Incomplete sentences + dropdown of ending options
**Options:** Usually 7-9 endings for 5-6 sentence starts

---

### 16. multiple_choice_more_than_one_answer_reading
**Source Folder:** `Reading/Multiple choice with more than one answer/`
**Description:** Choose multiple correct answers from options
**HTML Structure:**
```html
<ul>
  <li><label><input type="checkbox" value="A"/><p>Option A</p></label></li>
  <li><label><input type="checkbox" value="B"/><p>Option B</p></label></li>
  <li><label><input type="checkbox" value="C"/><p>Option C</p></label></li>
</ul>
```
**Answer Format:**
- Array of letters
- `cardinality="multiple"`, `baseType="identifier"`
- Answer key: Array like ["B", "D"]
**Instructions:** "Choose TWO letters"
**Typical:** 2-3 correct answers from 5-7 options

---

### 17. multiple_choice_one_answer_reading
**Source Folder:** `Reading/Multiple choice with one answer/`
**Description:** Choose one correct answer from options
**HTML Structure:**
```html
<ul>
  <li><label><input type="radio" name="Q1" value="A"/><p>Option A</p></label></li>
  <li><label><input type="radio" name="Q1" value="B"/><p>Option B</p></label></li>
  <li><label><input type="radio" name="Q1" value="C"/><p>Option C</p></label></li>
  <li><label><input type="radio" name="Q1" value="D"/><p>Option D</p></label></li>
</ul>
```
**Answer Format:**
- Single letter
- `cardinality="single"`, `baseType="identifier"`
- Answer key: Single letter like "C"
**Typical:** 4 options (A, B, C, D)

---

### 18. note_completion
**Source Folder:** `Reading/Note Completion/`
**Description:** Complete notes from passage
**HTML Structure:**
```html
<p>Main idea: <input type="text" connect:responseIdentifier="RESPONSE_ID" size="15"/></p>
```
**Answer Format:**
- Single string per blank
- `cardinality="single"`, `baseType="string"`
- Instructions: "Write NO MORE THAN TWO WORDS from the passage"
**Pattern:** Note-taking format with blanks
**Max Words:** 1-2 words per blank

---

### 19. sentence_completion_reading
**Source Folder:** `Reading/Sentence Completion/`
**Description:** Complete sentences using words from passage
**HTML Structure:**
```html
<p>The study found that <input type="text" connect:responseIdentifier="RESPONSE_ID" size="15"/>.</p>
```
**Answer Format:**
- Single string per blank
- `cardinality="single"`, `baseType="string"`
- Instructions: "Write NO MORE THAN TWO WORDS from the passage"
**Pattern:** Incomplete sentences with inline inputs
**Max Words:** 1-2 words per blank

---

### 20. summary_completion_selecting_from_list
**Source Folder:** `Reading/Summary Completion (selecting from a list of words or phrases)/`
**Description:** Complete summary by selecting from word bank
**HTML Structure:**
```html
<select connect:responseIdentifier="RESPONSE_ID">
  <option value="">Please select</option>
  <option value="A">Word/phrase A</option>
  <option value="B">Word/phrase B</option>
  <option value="C">Word/phrase C</option>
</select>
```
**Answer Format:**
- Single letter per blank
- `cardinality="single"`, `baseType="identifier"`
- Answer key: Letter (A-L typically)
**Pattern:** Summary paragraph with dropdown selections
**Options:** Usually 10-12 words for 5-7 blanks

---

### 21. summary_completion_selecting_words_from_text
**Source Folder:** `Reading/Summary Completion (selecting words from the text)/`
**Description:** Complete summary using exact words from passage
**HTML Structure:**
```html
<p>Summary text with <input type="text" connect:responseIdentifier="RESPONSE_ID" size="15"/> blank spaces.</p>
```
**Answer Format:**
- Single string per blank
- `cardinality="single"`, `baseType="string"`
- Instructions: "Write NO MORE THAN TWO WORDS from the passage"
**Constraint:** Must use exact words from passage
**Max Words:** 1-2 words per blank

---

### 22. table_completion_reading
**Source Folder:** `Reading/Table Completion/`
**Description:** Complete table with information from passage
**HTML Structure:**
```html
<table>
  <tr>
    <td>Category</td>
    <td><input type="text" connect:responseIdentifier="RESPONSE_ID" size="15"/></td>
  </tr>
</table>
```
**Answer Format:**
- Single string per cell
- `cardinality="single"`, `baseType="string"`
- Instructions: "Write NO MORE THAN TWO WORDS from the passage"
**Pattern:** Table with some filled cells, others blank
**Max Words:** 1-2 words per cell

---

## ✍️ WRITING QUESTION TYPES (2)

### 23. writing_part_1
**Source Folder:** `Writing/writing-part-1/`
**Description:** Academic Writing Task 1 - Describe visual data (chart/graph/diagram)
**HTML Structure:**
```html
<img src="chart.png"/>
<p>Task instructions: Summarize the information by selecting and reporting main features...</p>
<textarea connect:responseIdentifier="RESPONSE_ID" rows="20" cols="80"></textarea>
```
**Answer Format:**
- Long text (150+ words)
- `cardinality="single"`, `baseType="string"`
- No auto-grading (manual assessment only)
**Requirements:**
- Minimum 150 words
- 20 minutes recommended time
- Chart/graph/table/diagram description

---

### 24. writing_part_2
**Source Folder:** `Writing/writing-part-2/`
**Description:** Academic Writing Task 2 - Essay on given topic
**HTML Structure:**
```html
<p>Task instructions: Write about the following topic...</p>
<p>Essay prompt text here...</p>
<textarea connect:responseIdentifier="RESPONSE_ID" rows="25" cols="80"></textarea>
```
**Answer Format:**
- Long text (250+ words)
- `cardinality="single"`, `baseType="string"`
- No auto-grading (manual assessment only)
**Requirements:**
- Minimum 250 words
- 40 minutes recommended time
- Argumentative/discussion essay

---

## 🎯 Answer Format Summary

### Text Input (String)
**Types:** fill_in_the_gaps, fill_in_the_gaps_short_answers, flowchart_completion_listening, form_completion, labelling_on_a_map, sentence_completion_listening, table_completion_listening, flowchart_completion_selecting_words_from_text, note_completion, sentence_completion_reading, summary_completion_selecting_words_from_text, table_completion_reading, writing_part_1, writing_part_2

**Answer Format:** `string` (single word/phrase or long text)

### Single Choice (Radio)
**Types:** multiple_choice_one_answer_listening, multiple_choice_one_answer_reading, identifying_information_true_false_not_given

**Answer Format:** `single letter` (A, B, C, D)

### Multiple Choice (Checkbox)
**Types:** multiple_choice_more_than_one_answer_listening, multiple_choice_more_than_one_answer_reading

**Answer Format:** `array of letters` (["A", "C"], ["B", "D", "E"])

### Dropdown Selection
**Types:** matching_listening, matching_features, matching_headings, matching_sentence_endings, summary_completion_selecting_from_list

**Answer Format:** `single letter/identifier` (A-Z or i-viii for headings)

---

## 📊 Implementation Priority

### High Priority (Core IELTS Types) - 16 types
1. ✅ fill_in_the_gaps
2. ✅ multiple_choice_one_answer_listening
3. ✅ multiple_choice_more_than_one_answer_listening
4. ✅ sentence_completion_listening
5. ✅ table_completion_listening
6. ✅ identifying_information_true_false_not_given
7. ✅ multiple_choice_one_answer_reading
8. ✅ multiple_choice_more_than_one_answer_reading
9. ✅ sentence_completion_reading
10. ✅ matching_headings
11. ✅ summary_completion_selecting_from_list
12. ✅ summary_completion_selecting_words_from_text
13. ✅ table_completion_reading
14. ✅ note_completion
15. ✅ writing_part_1
16. ✅ writing_part_2

### Medium Priority (Common Types) - 5 types
17. ✅ form_completion
18. ✅ flowchart_completion_listening
19. ✅ matching_listening
20. ✅ matching_features
21. ✅ matching_sentence_endings

### Lower Priority (Less Common) - 3 types
22. ✅ fill_in_the_gaps_short_answers
23. ✅ labelling_on_a_map
24. ✅ flowchart_completion_selecting_words_from_text

---

## 🔑 Key Implementation Notes

### Auto-Grading Support
- **Supported (22 types):** All except writing_part_1 and writing_part_2
- **Case Sensitivity:** Should be case-insensitive for text answers
- **Whitespace:** Trim whitespace before comparison
- **Multiple Answers:** Check array equality for checkbox types

### Word Count Limits
- **Fill-in types:** Usually 1-2 words maximum
- **Form completion:** Up to 3 words and/or number
- **Reading types:** Usually "from the passage" constraint
- **Writing tasks:** Minimum word counts (150/250)

### Visual Elements
- **Map labeling:** Requires image upload field
- **Diagram/Flowchart:** Requires image upload field
- **Charts (Writing Task 1):** Requires image upload field

### Dropdown Options
- **Matching types:** Need flexible option lists (A-Z)
- **Headings:** Use roman numerals (i, ii, iii, etc.)
- **Features/Endings:** Use letters (A-H typically)

---

## ✅ Next Steps

1. **Backend Schema Update** - Create Pydantic models for all 24 types
2. **Validation Update** - Add all type names to Literal enum
3. **Frontend Components** - Build 24 React components
4. **Auto-Grading Logic** - Update scoring for each type
5. **Sample Tests** - Create test files with real QTI examples
6. **Testing** - Verify each type renders and submits correctly

---

**Status:** Analysis Complete ✅
**Document Created:** Ready for Phase 2 (Backend Implementation)
