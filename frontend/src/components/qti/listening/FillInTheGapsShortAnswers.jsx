import React from 'react';

/**
 * Fill in the Gaps Short Answers - Listening
 * Short factual answers to direct questions
 * Instructions: Write NO MORE THAN TWO WORDS
 * QTI Source: /app/Question type/Listening/Fill in the gaps short answers/
 */
const FillInTheGapsShortAnswers = ({ question, answer, onAnswerChange, onFocus }) => {
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
            className="w-64 px-3 py-2 border border-gray-300 rounded focus:outline-none focus:ring-2 focus:ring-blue-500"
            placeholder="Your answer"
          />
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

export default FillInTheGapsShortAnswers;
