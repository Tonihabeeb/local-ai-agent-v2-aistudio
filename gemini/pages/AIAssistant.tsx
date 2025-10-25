import React, { useState } from 'react';
import GeminiChatInterface from '../components/ai/GeminiChatInterface';
import DocumentAnalyzer from '../components/ai/DocumentAnalyzer';
import CodeAssistant from '../components/ai/CodeAssistant';

const AIAssistant: React.FC = () => {
  const [activeTab, setActiveTab] = useState<'chat' | 'documents' | 'code'>('chat');

  return (
    <div className="min-h-screen bg-gray-50">
      {/* Header */}
      <div className="bg-white shadow-sm border-b">
        <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
          <div className="flex justify-between items-center py-4">
            <div>
              <h1 className="text-2xl font-bold text-gray-900">AI Assistant</h1>
              <p className="text-sm text-gray-600">Powered by Google Gemini API</p>
            </div>
            <div className="flex items-center space-x-2">
              <div className="w-3 h-3 bg-green-500 rounded-full"></div>
              <span className="text-sm text-gray-600">Backend Connected</span>
            </div>
          </div>
        </div>
      </div>

      {/* Navigation Tabs */}
      <div className="bg-white border-b">
        <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
          <nav className="flex space-x-8">
            <button
              onClick={() => setActiveTab('chat')}
              className={`py-4 px-1 border-b-2 font-medium text-sm ${
                activeTab === 'chat'
                  ? 'border-blue-500 text-blue-600'
                  : 'border-transparent text-gray-500 hover:text-gray-700 hover:border-gray-300'
              }`}
            >
              💬 Chat Assistant
            </button>
            <button
              onClick={() => setActiveTab('documents')}
              className={`py-4 px-1 border-b-2 font-medium text-sm ${
                activeTab === 'documents'
                  ? 'border-blue-500 text-blue-600'
                  : 'border-transparent text-gray-500 hover:text-gray-700 hover:border-gray-300'
              }`}
            >
              📄 Document Analysis
            </button>
            <button
              onClick={() => setActiveTab('code')}
              className={`py-4 px-1 border-b-2 font-medium text-sm ${
                activeTab === 'code'
                  ? 'border-blue-500 text-blue-600'
                  : 'border-transparent text-gray-500 hover:text-gray-700 hover:border-gray-300'
              }`}
            >
              💻 Code Assistant
            </button>
          </nav>
        </div>
      </div>

      {/* Main Content */}
      <div className="max-w-7xl mx-auto py-6">
        {activeTab === 'chat' && (
          <div className="bg-white rounded-lg shadow">
            <div className="h-96">
              <GeminiChatInterface />
            </div>
          </div>
        )}

        {activeTab === 'documents' && (
          <div className="bg-white rounded-lg shadow">
            <DocumentAnalyzer />
          </div>
        )}

        {activeTab === 'code' && (
          <div className="bg-white rounded-lg shadow">
            <CodeAssistant />
          </div>
        )}
      </div>

      {/* Quick Start Guide */}
      <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 py-6">
        <div className="bg-blue-50 border border-blue-200 rounded-lg p-6">
          <h3 className="text-lg font-semibold text-blue-900 mb-3">🚀 Quick Start Guide</h3>
          <div className="grid grid-cols-1 md:grid-cols-3 gap-4 text-sm">
            <div>
              <h4 className="font-medium text-blue-800 mb-2">💬 Chat Assistant</h4>
              <p className="text-blue-700">Ask questions, get help, or have a conversation with AI</p>
            </div>
            <div>
              <h4 className="font-medium text-blue-800 mb-2">📄 Document Analysis</h4>
              <p className="text-blue-700">Upload documents for summarization, translation, or analysis</p>
            </div>
            <div>
              <h4 className="font-medium text-blue-800 mb-2">💻 Code Assistant</h4>
              <p className="text-blue-700">Generate code or get code reviews and suggestions</p>
            </div>
          </div>
        </div>
      </div>
    </div>
  );
};

export default AIAssistant;
