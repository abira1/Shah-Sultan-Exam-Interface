import React from 'react';

/**
 * Multiple Choice (More Than One Answer) - Listening
 * Choose multiple correct answers from options using checkboxes
 * Instructions: Choose TWO/THREE letters
 * QTI Source: /app/Question type/Listening/Multiple Choice (more than one answer)/
 */
const MultipleChoiceMoreThanOneAnswerListening = ({ question, answer, onAnswerChange, onFocus }) => {
  const questionNum = question.index;
  const { prompt, options = [], max_choices = 2 } = question.payload;
  const selectedAnswers = Array.isArray(answer) ? answer : (answer ? [answer] : []);

  const handleCheckboxChange = (value, isChecked) => {
    let newAnswers;
    if (isChecked) {
      newAnswers = [...selectedAnswers, value];
    } else {
      newAnswers = selectedAnswers.filter(a => a !== value);
    }
    onAnswerChange(questionNum, newAnswers);
  };

  return (
    <div 
      className="mb-6" 
      data-question-index={questionNum}
      onClick={() => onFocus && onFocus(questionNum)}
    >
      <div className="flex items-start gap-2">
        <span className="font-semibold min-w-[3rem]">{questionNum}.</span>
        <div className="flex-1">
          <p className="text-gray-700 mb-3">{prompt}</p>
          <p className="text-sm text-gray-600 mb-2 font-medium">
            Choose {max_choices} letter{max_choices > 1 ? 's' : ''}
          </p>
          <div className="space-y-2">
            {options.map((option, idx) => {
              const optionValue = option.value || String.fromCharCode(65 + idx); // A, B, C, D
              const optionText = option.text || option;
              return (
                <label key={idx} className="flex items-start gap-2 cursor-pointer hover:bg-gray-50 p-2 rounded">
                  <input
                    type="checkbox"
                    value={optionValue}
                    checked={selectedAnswers.includes(optionValue)}
                    onChange={(e) => handleCheckboxChange(optionValue, e.target.checked)}
                    onFocus={() => onFocus && onFocus(questionNum)}
                    className="mt-1"
                  />
                  <span className="text-gray-700">
                    <span className="font-medium">{optionValue}.</span> {optionText}
                  </span>
                </label>
              );
            })}
          </div>
        </div>
      </div>
    </div>
  );
};

export default MultipleChoiceMoreThanOneAnswerListening;
