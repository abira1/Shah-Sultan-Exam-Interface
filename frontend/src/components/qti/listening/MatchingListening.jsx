import React from 'react';

/**
 * Matching - Listening
 * Match items from two lists using dropdown selection
 * QTI Source: /app/Question type/Listening/Matching/
 */
const MatchingListening = ({ question, answer, onAnswerChange, onFocus }) => {
  const questionNum = question.index;
  const { prompt, options = [] } = question.payload;

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
            {options.map((opt, idx) => (
              <option key={idx} value={opt.value || opt}>
                {opt.text || opt}
              </option>
            ))}
          </select>
        </div>
      </div>
    </div>
  );
};

export default MatchingListening;
