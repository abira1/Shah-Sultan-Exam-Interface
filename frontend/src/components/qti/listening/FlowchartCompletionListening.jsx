import React from 'react';

/**
 * Flowchart Completion - Listening
 * Complete flowchart by filling in missing labels/text
 * Instructions: Write NO MORE THAN TWO WORDS
 * QTI Source: /app/Question type/Listening/Flow-chart Completion/
 */
const FlowchartCompletionListening = ({ question, answer, onAnswerChange, onFocus }) => {
  const questionNum = question.index;
  const { prompt, image_url, max_words = 2 } = question.payload;

  return (
    <div 
      className="mb-4" 
      data-question-index={questionNum}
      onClick={() => onFocus && onFocus(questionNum)}
    >
      <div className="flex items-start gap-2">
        <span className="font-semibold min-w-[3rem]">{questionNum}.</span>
        <div className="flex-1">
          {image_url && (
            <img 
              src={image_url} 
              alt="Flowchart" 
              className="mb-3 max-w-full h-auto border border-gray-300 rounded"
            />
          )}
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

export default FlowchartCompletionListening;
