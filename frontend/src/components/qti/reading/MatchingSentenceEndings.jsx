import React from 'react';

/**
 * Matching Sentence Endings - Reading
 * Match sentence beginnings to appropriate endings using dropdown
 * QTI Source: /app/Question type/Reading/Matching Sentence Endings/
 */
const MatchingSentenceEndings = ({ question, answer, onAnswerChange, onFocus }) => {
  const questionNum = question.index;
  const { prompt, endings = [] } = question.payload;

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
            className="w-full px-3 py-2 border border-gray-300 rounded focus:outline-none focus:ring-2 focus:ring-blue-500"
          >
            <option value="">Please select</option>
            {endings.map((ending, idx) => (
              <option key={idx} value={ending.value || ending}>
                {ending.value || ending}: {ending.text || ending}
              </option>
            ))}
          </select>
        </div>
      </div>
    </div>
  );
};

export default MatchingSentenceEndings;
