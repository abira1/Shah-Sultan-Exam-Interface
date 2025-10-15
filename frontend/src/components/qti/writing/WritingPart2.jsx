import React, { useState, useEffect } from 'react';

/**
 * Writing Part 2 - Academic Writing Task 2
 * Essay on given topic
 * Minimum 250 words, 40 minutes recommended
 * QTI Source: /app/Question type/Writing/writing-part-2/
 */
const WritingPart2 = ({ question, answer, onAnswerChange, onFocus }) => {
  const questionNum = question.index;
  const { prompt, instructions, min_words = 250 } = question.payload;
  const [wordCount, setWordCount] = useState(0);

  useEffect(() => {
    const text = answer || '';
    const words = text.trim().split(/\s+/).filter(word => word.length > 0);
    setWordCount(words.length);
  }, [answer]);

  const isWordCountSufficient = wordCount >= min_words;

  return (
    <div 
      className="mb-6" 
      data-question-index={questionNum}
      onClick={() => onFocus && onFocus(questionNum)}
    >
      <div className="flex items-start gap-2">
        <span className="font-semibold min-w-[3rem]">{questionNum}.</span>
        <div className="flex-1">
          <div className="mb-4">
            {instructions && (
              <p className="text-sm text-gray-600 mb-3 italic">{instructions}</p>
            )}
            <p className="text-gray-700 mb-3 leading-relaxed">{prompt}</p>
          </div>
          
          <textarea
            value={answer || ''}
            onChange={(e) => onAnswerChange(questionNum, e.target.value)}
            onFocus={() => onFocus && onFocus(questionNum)}
            className="w-full min-h-[500px] px-3 py-2 border border-gray-300 rounded focus:outline-none focus:ring-2 focus:ring-blue-500 font-mono text-sm"
            placeholder="Write your essay here..."
          />
          
          <div className="flex items-center justify-between mt-2">
            <p className={`text-sm font-medium ${
              isWordCountSufficient ? 'text-green-600' : 'text-orange-600'
            }`}>
              Word count: {wordCount} / {min_words} minimum
            </p>
            <p className="text-xs text-gray-500">
              Recommended time: 40 minutes
            </p>
          </div>
        </div>
      </div>
    </div>
  );
};

export default WritingPart2;
