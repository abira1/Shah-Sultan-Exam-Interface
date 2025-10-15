import React from 'react';

/**
 * Fill in the Gaps - Listening
 * Complete notes/tables by filling blank fields with text input
 * Instructions: Write ONE WORD AND/OR A NUMBER in each gap
 * QTI Source: /app/Question type/Listening/Fill in the gaps/
 */
const FillInTheGaps = ({ question, answer, onAnswerChange, onFocus }) => {
  const questionNum = question.index;
  const { prompt, max_words = 2, table_data } = question.payload;

  return (
    <div 
      className="mb-4" 
      data-question-index={questionNum}
      onClick={() => onFocus && onFocus(questionNum)}
    >
      <div className="flex items-start gap-2">
        <span className="font-semibold min-w-[3rem]">{questionNum}.</span>
        <div className="flex-1">
          {/* Prompt with inline input for blanks */}
          <div className="text-gray-700 mb-2">
            {prompt.split('____').map((part, idx) => (
              <React.Fragment key={idx}>
                {part}
                {idx < prompt.split('____').length - 1 && (
                  <input
                    type="text"
                    value={answer || ''}
                    onChange={(e) => onAnswerChange(questionNum, e.target.value)}
                    onFocus={() => onFocus && onFocus(questionNum)}
                    className="inline-block w-32 px-2 py-1 border-b-2 border-gray-400 focus:border-blue-500 focus:outline-none bg-transparent"
                    placeholder="..."
                  />
                )}
              </React.Fragment>
            ))}
          </div>
          {max_words && (
            <p className="text-xs text-gray-500 mt-1">
              Maximum {max_words} word(s)
            </p>
          )}
        </div>
      </div>
    </div>
  );
};

export default FillInTheGaps;
