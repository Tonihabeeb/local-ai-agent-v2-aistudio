import React, { useState } from 'react';

interface AnalysisResult {
  type: string;
  content: string;
  timestamp: Date;
}

const DocumentAnalyzer: React.FC = () => {
  const [document, setDocument] = useState('');
  const [analysisType, setAnalysisType] = useState('summary');
  const [results, setResults] = useState<AnalysisResult[]>([]);
  const [loading, setLoading] = useState(false);

  const analyzeDocument = async () => {
    if (!document.trim()) return;

    setLoading(true);
    try {
      const response = await fetch('/api/v1/gemini/analyze', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({
          content: document,
          analysis_type: analysisType
        })
      });

      const data = await response.json();
      
      if (data.success) {
        const result: AnalysisResult = {
          type: analysisType,
          content: data.text,
          timestamp: new Date()
        };
        setResults(prev => [result, ...prev]);
      }
    } catch (error) {
      console.error('Error analyzing document:', error);
    } finally {
      setLoading(false);
    }
  };

  const analysisTypes = [
    { value: 'summary', label: 'Summary' },
    { value: 'key_points', label: 'Key Points' },
    { value: 'sentiment', label: 'Sentiment Analysis' },
    { value: 'translation', label: 'Translate to English' },
    { value: 'qa', label: 'Q&A Generation' }
  ];

  return (
    <div className="max-w-4xl mx-auto p-6">
      <h2 className="text-2xl font-bold mb-6">Document Analyzer</h2>
      
      <div className="grid grid-cols-1 lg:grid-cols-2 gap-6">
        {/* Input Section */}
        <div className="space-y-4">
          <div>
            <label className="block text-sm font-medium mb-2">
              Analysis Type
            </label>
            <select
              value={analysisType}
              onChange={(e) => setAnalysisType(e.target.value)}
              className="w-full border rounded-lg px-3 py-2 focus:outline-none focus:ring-2 focus:ring-blue-500"
            >
              {analysisTypes.map(type => (
                <option key={type.value} value={type.value}>
                  {type.label}
                </option>
              ))}
            </select>
          </div>
          
          <div>
            <label className="block text-sm font-medium mb-2">
              Document Content
            </label>
            <textarea
              value={document}
              onChange={(e) => setDocument(e.target.value)}
              placeholder="Paste your document content here..."
              className="w-full h-64 border rounded-lg px-3 py-2 focus:outline-none focus:ring-2 focus:ring-blue-500"
            />
          </div>
          
          <button
            onClick={analyzeDocument}
            disabled={loading || !document.trim()}
            className="w-full bg-blue-500 text-white py-2 px-4 rounded-lg hover:bg-blue-600 disabled:opacity-50"
          >
            {loading ? 'Analyzing...' : 'Analyze Document'}
          </button>
        </div>

        {/* Results Section */}
        <div className="space-y-4">
          <h3 className="text-lg font-semibold">Analysis Results</h3>
          {results.length === 0 ? (
            <p className="text-gray-500">No analysis results yet. Upload a document to get started.</p>
          ) : (
            <div className="space-y-4">
              {results.map((result, index) => (
                <div key={index} className="border rounded-lg p-4">
                  <div className="flex justify-between items-center mb-2">
                    <span className="text-sm font-medium text-blue-600 capitalize">
                      {result.type.replace('_', ' ')}
                    </span>
                    <span className="text-xs text-gray-500">
                      {result.timestamp.toLocaleString()}
                    </span>
                  </div>
                  <div className="text-sm text-gray-700 whitespace-pre-wrap">
                    {result.content}
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

export default DocumentAnalyzer;
