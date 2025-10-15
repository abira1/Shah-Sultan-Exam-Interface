import React from 'react';

/**
 * Summary Completion (Selecting from List) - Reading
 * Complete summary by selecting from word bank
 * QTI Source: /app/Question type/Reading/Summary Completion (selecting from a list of words or phrases)/
 */
const SummaryCompletionSelectingFromList = ({ question, answer, onAnswerChange, onFocus }) => {
  const questionNum = question.index;
  const { prompt, word_list = [] } = question.payload;

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
          <select
            value={answer || ''}
            onChange={(e) => onAnswerChange(questionNum, e.target.value)}
            onFocus={() => onFocus && onFocus(questionNum)}
            className="w-full max-w-xs px-3 py-2 border border-gray-300 rounded focus:outline-none focus:ring-2 focus:ring-blue-500"
          >
            <option value="">Please select</option>
            {word_list.map((word, idx) => {
              const wordValue = typeof word === 'object' ? word.value : String.fromCharCode(65 + idx);
              const wordText = typeof word === 'object' ? word.text : word;
              return (
                <option key={idx} value={wordValue}>
                  {wordValue}: {wordText}
                </option>
              );
            })}
          </select>
        </div>
      </div>
    </div>
  );
};

export default SummaryCompletionSelectingFromList;
