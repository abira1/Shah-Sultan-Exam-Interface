import React from 'react';

/**
 * Multiple Choice (One Answer) - Listening
 * Choose one correct answer from options using radio buttons
 * QTI Source: /app/Question type/Listening/Multiple Choice (one answer)/
 */
const MultipleChoiceOneAnswerListening = ({ question, answer, onAnswerChange, onFocus }) => {
  const questionNum = question.index;
  const { prompt, options = [] } = question.payload;

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
          <div className="space-y-2">
            {options.map((option, idx) => {
              const optionValue = option.value || String.fromCharCode(65 + idx); // A, B, C, D
              const optionText = option.text || option;
              return (
                <label key={idx} className="flex items-start gap-2 cursor-pointer hover:bg-gray-50 p-2 rounded">
                  <input
                    type="radio"
                    name={`question_${questionNum}`}
                    value={optionValue}
                    checked={answer === optionValue}
                    onChange={(e) => onAnswerChange(questionNum, e.target.value)}
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

export default MultipleChoiceOneAnswerListening;
