import React from 'react';

/**
 * Table Completion - Reading
 * Complete table with information from passage
 * Instructions: Write NO MORE THAN TWO WORDS from the passage
 * QTI Source: /app/Question type/Reading/Table Completion/
 */
const TableCompletionReading = ({ question, answer, onAnswerChange, onFocus }) => {
  const questionNum = question.index;
  const { prompt, max_words = 2 } = question.payload;

  return (
    <div 
      className="mb-4" 
      data-question-index={questionNum}
      onClick={() => onFocus && onFocus(questionNum)}
    >
      <div className="flex items-start gap-2">
        <span className="font-semibold min-w-[3rem]">{questionNum}.</span>
        <div className="flex-1">
          <p className="text-gray-700 mb-2">{prompt}</p>
          <input
            type="text"
            value={answer || ''}
            onChange={(e) => onAnswerChange(questionNum, e.target.value)}
            onFocus={() => onFocus && onFocus(questionNum)}
            className="w-full max-w-md px-3 py-2 border border-gray-300 rounded focus:outline-none focus:ring-2 focus:ring-blue-500"
            placeholder="Words from passage"
          />
          <p className="text-xs text-gray-500 mt-1">
            Use NO MORE THAN {max_words} WORD(S) from the passage
          </p>
        </div>
      </div>
    </div>
  );
};

export default TableCompletionReading;
