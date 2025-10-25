import React, { useState } from 'react';

// A simple custom hook for handling API calls to the code assistant endpoints
const useApi = <T,>(url: string) => {
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState<string | null>(null);

  const execute = async (body: T) => {
    setLoading(true);
    setError(null);
    try {
      const response = await fetch(url, {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify(body),
      });

      if (!response.ok) {
        throw new Error(`API Error: ${response.status} ${response.statusText}`);
      }

      const data = await response.json();
      if (!data.success) {
        throw new Error(data.error || 'An unknown API error occurred.');
      }
      return data;
    } catch (err: any) {
      const errorMessage = err.message || 'An unexpected error occurred.';
      setError(errorMessage);
      console.error(`Error calling ${url}:`, err);
      return null;
    } finally {
      setLoading(false);
    }
  };

  return { execute, loading, error, setError };
};

interface CodeResult {
  type: 'generation' | 'review';
  language: string;
  code: string;
  result: string;
  timestamp: Date;
}

const CodeAssistant: React.FC = () => {
  const [activeTab, setActiveTab] = useState<'generate' | 'review'>('generate');
  const [description, setDescription] = useState('');
  const [language, setLanguage] = useState('python');
  const [code, setCode] = useState('');
  const [results, setResults] = useState<CodeResult[]>([]);
  
  const { execute: executeGenerate, loading: loadingGenerate, error: errorGenerate, setError: setErrorGenerate } = useApi('/api/v1/gemini/generate-code');
  const { execute: executeReview, loading: loadingReview, error: errorReview, setError: setErrorReview } = useApi('/api/v1/gemini/review-code');

  const loading = loadingGenerate || loadingReview;
  const error = errorGenerate || errorReview;

  const generateCode = async () => {
    if (!description.trim()) return;

    const data = await executeGenerate({ description, language });

    if (data) {
      const newResult: CodeResult = {
        type: 'generation',
        language,
        code: description,
        result: data.text,
        timestamp: new Date()
      };
      setResults(prev => [newResult, ...prev]);
      setDescription(''); // Clear input on success
    }
  };

  const reviewCode = async () => {
    if (!code.trim()) return;

    const data = await executeReview({ code, language });

    if (data) {
      const newResult: CodeResult = {
        type: 'review',
        language,
        code,
        result: data.text,
        timestamp: new Date()
      };
      setResults(prev => [newResult, ...prev]);
    }
  };

  const languages = [
    'python', 'javascript', 'typescript', 'java', 'c++', 'c#', 'go', 'rust', 'php', 'ruby'
  ];

  return (
    <div className="max-w-6xl mx-auto p-6">
      <h2 className="text-2xl font-bold mb-6">AI Code Assistant</h2>
      
      {/* Tab Navigation */}
      <div className="flex space-x-1 mb-6">
        <button
          onClick={() => setActiveTab('generate')}
          className={`px-4 py-2 rounded-lg font-medium ${
            activeTab === 'generate'
              ? 'bg-blue-500 text-white'
              : 'bg-gray-200 text-gray-700 hover:bg-gray-300'
          }`}
        >
          Generate Code
        </button>
        <button
          onClick={() => setActiveTab('review')}
          className={`px-4 py-2 rounded-lg font-medium ${
            activeTab === 'review'
              ? 'bg-blue-500 text-white'
              : 'bg-gray-200 text-gray-700 hover:bg-gray-300'
          }`}
        >
          Review Code
        </button>
      </div>

      <div className="grid grid-cols-1 lg:grid-cols-2 gap-6">
        {/* Input Section */}
        <div className="space-y-4">
          <div>
            <label className="block text-sm font-medium mb-2">
              Programming Language
            </label>
            <select
              value={language}
              onChange={(e) => setLanguage(e.target.value)}
              className="w-full border rounded-lg px-3 py-2 focus:outline-none focus:ring-2 focus:ring-blue-500"
            >
              {languages.map(lang => (
                <option key={lang} value={lang}>
                  {lang.charAt(0).toUpperCase() + lang.slice(1)}
                </option>
              ))}
            </select>
          </div>

          {activeTab === 'generate' ? (
            <div>
              <label className="block text-sm font-medium mb-2">
                Code Description
              </label>
              <textarea
                value={description}
                onChange={(e) => setDescription(e.target.value)}
                placeholder="Describe what you want the code to do..."
                className="w-full h-32 border rounded-lg px-3 py-2 focus:outline-none focus:ring-2 focus:ring-blue-500"
              />
              <button
                onClick={generateCode}
                disabled={loading || !description.trim()}
                className="mt-4 w-full bg-green-500 text-white py-2 px-4 rounded-lg hover:bg-green-600 disabled:opacity-50"
              >
                {loading ? 'Generating...' : 'Generate Code'}
              </button>
            </div>
          ) : (
            <div>
              <label className="block text-sm font-medium mb-2">
                Code to Review
              </label>
              <textarea
                value={code}
                onChange={(e) => setCode(e.target.value)}
                placeholder="Paste your code here for review..."
                className="w-full h-64 border rounded-lg px-3 py-2 focus:outline-none focus:ring-2 focus:ring-blue-500 font-mono text-sm"
              />
              <button
                onClick={reviewCode}
                disabled={loading || !code.trim()}
                className="mt-4 w-full bg-orange-500 text-white py-2 px-4 rounded-lg hover:bg-orange-600 disabled:opacity-50"
              >
                {loading ? 'Reviewing...' : 'Review Code'}
              </button>
            </div>
          )}
        </div>

        {/* Error Display */}
        {error && (
          <div className="lg:col-span-2 bg-red-100 border border-red-400 text-red-700 px-4 py-3 rounded relative" role="alert">
            <strong className="font-bold">Error: </strong>
            <span className="block sm:inline">{error}</span>
            <span className="absolute top-0 bottom-0 right-0 px-4 py-3" onClick={() => { setErrorGenerate(null); setErrorReview(null); }}>
              <svg className="fill-current h-6 w-6 text-red-500" role="button" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 20 20"><title>Close</title><path d="M14.348 14.849a1.2 1.2 0 0 1-1.697 0L10 11.819l-2.651 3.03a1.2 1.2 0 1 1-1.697-1.697l2.758-3.15-2.759-3.152a1.2 1.2 0 1 1 1.697-1.697L10 8.183l2.651-3.031a1.2 1.2 0 1 1 1.697 1.697l-2.758 3.152 2.758 3.15a1.2 1.2 0 0 1 0 1.698z"/></svg>
            </span>
          </div>
        )}

        {/* Results Section */}
        <div className="space-y-4">
          <h3 className="text-lg font-semibold">Results</h3>
          {results.length === 0 ? (
            <p className="text-gray-500">No results yet. Generate or review some code to get started.</p>
          ) : (
            <div className="space-y-4 max-h-96 overflow-y-auto">
              {results.map((result, index) => (
                <div key={result.timestamp.toISOString() + index} className="border rounded-lg p-4">
                  <div className="flex justify-between items-center mb-2">
                    <span className={`text-sm font-medium ${
                      result.type === 'generation' ? 'text-green-600' : 'text-orange-600'
                    }`}>
                      {result.type === 'generation' ? 'Generated' : 'Review'} - {result.language}
                    </span>
                    <span className="text-xs text-gray-500">
                      {result.timestamp.toLocaleString()}
                    </span>
                  </div>
                  
                  {result.type === 'generation' && (
                    <div className="mb-3">
                      <p className="text-sm text-gray-600 mb-2">Description:</p>
                      <p className="text-sm bg-gray-100 p-2 rounded">{result.code}</p>
                    </div>
                  )}
                  
                  {result.type === 'review' && (
                    <div className="mb-3">
                      <p className="text-sm text-gray-600 mb-2">Code:</p>
                      <pre className="text-xs bg-gray-100 p-2 rounded overflow-x-auto">
                        {result.code}
                      </pre>
                    </div>
                  )}
                  
                  <div>
                    <p className="text-sm text-gray-600 mb-2">
                      {result.type === 'generation' ? 'Generated Code:' : 'Review:'}
                    </p>
                    <div className="text-sm whitespace-pre-wrap bg-gray-50 p-3 rounded">
                      {result.result}
                    </div>
                  </div>
                </div>
              ))}
            </div>
          )}
        </div>
      </div>
    </div>
  );
};

export default CodeAssistant;