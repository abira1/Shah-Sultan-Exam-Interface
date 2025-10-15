import React from 'react';

/**
 * Identifying Information (True/False/Not Given) - Reading
 * Determine if statements are TRUE, FALSE, or NOT GIVEN based on passage
 * QTI Source: /app/Question type/Reading/Identifying Information (TrueFalseNot Given)/
 */
const IdentifyingInformationTrueFalseNotGiven = ({ question, answer, onAnswerChange, onFocus }) => {
  const questionNum = question.index;
  const { prompt } = question.payload;
  const options = [
    { value: 'A', text: 'TRUE' },
    { value: 'B', text: 'FALSE' },
    { value: 'C', text: 'NOT GIVEN' }
  ];

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
            {options.map((option) => (
              <label key={option.value} className="flex items-start gap-2 cursor-pointer hover:bg-gray-50 p-2 rounded">
                <input
                  type="radio"
                  name={`question_${questionNum}`}
                  value={option.value}
                  checked={answer === option.value}
                  onChange={(e) => onAnswerChange(questionNum, e.target.value)}
                  onFocus={() => onFocus && onFocus(questionNum)}
                  className="mt-1"
                />
                <span className="text-gray-700 font-medium">{option.text}</span>
              </label>
            ))}
          </div>
        </div>
      </div>
    </div>
  );
};

export default IdentifyingInformationTrueFalseNotGiven;
