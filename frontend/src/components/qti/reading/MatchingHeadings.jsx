import React from 'react';

/**
 * Matching Headings - Reading
 * Match paragraph headings to paragraphs using dropdown
 * Uses roman numerals (i, ii, iii, iv, v, vi, vii, viii)
 * QTI Source: /app/Question type/Reading/Matching Headings/
 */
const MatchingHeadings = ({ question, answer, onAnswerChange, onFocus }) => {
  const questionNum = question.index;
  const { prompt, headings = [] } = question.payload;

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
            className="w-full max-w-md px-3 py-2 border border-gray-300 rounded focus:outline-none focus:ring-2 focus:ring-blue-500"
          >
            <option value="">Please select</option>
            {headings.map((heading, idx) => (
              <option key={idx} value={heading.value || heading}>
                {heading.value || heading}: {heading.text || heading}
              </option>
            ))}
          </select>
        </div>
      </div>
    </div>
  );
};

export default MatchingHeadings;
