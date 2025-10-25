# Gemini API Usage Guide for Local AI Agent v2

## 🚀 **What You Can Build Now**

### **1. AI-Powered Chat System**
```typescript
// Real-time chat with Gemini
const chatWithAI = async (message: string) => {
  const response = await fetch('/api/v1/gemini/chat', {
    method: 'POST',
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify({
      messages: [{ role: 'user', content: message }]
    })
  });
  return response.json();
};
```

**Use Cases:**
- Customer support chatbot
- Internal knowledge assistant
- Interactive help system
- Brainstorming partner

### **2. Smart Document Processing**
```typescript
// Analyze any document content
const analyzeDocument = async (content: string, type: string) => {
  const response = await fetch('/api/v1/gemini/analyze', {
    method: 'POST',
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify({
      content,
      analysis_type: type // summary, key_points, sentiment, translation
    })
  });
  return response.json();
};
```

**Use Cases:**
- PDF report summarization
- Email content analysis
- Meeting notes extraction
- Content translation
- Sentiment analysis of feedback

### **3. AI Code Generation & Review**
```typescript
// Generate code from description
const generateCode = async (description: string, language: string) => {
  const response = await fetch('/api/v1/gemini/generate-code', {
    method: 'POST',
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify({ description, language })
  });
  return response.json();
};

// Review existing code
const reviewCode = async (code: string, language: string) => {
  const response = await fetch('/api/v1/gemini/review-code', {
    method: 'POST',
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify({ code, language })
  });
  return response.json();
};
```

**Use Cases:**
- Auto-generate boilerplate code
- Code optimization suggestions
- Bug detection and fixes
- Documentation generation
- Code explanation and learning

## 🛠️ **Practical Implementation Examples**

### **Example 1: Email Assistant**
```typescript
const generateEmail = async (context: string, recipient: string, purpose: string) => {
  const prompt = `Write a professional email to ${recipient} about ${purpose}. Context: ${context}`;
  
  const response = await fetch('/api/v1/gemini/generate', {
    method: 'POST',
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify({ prompt })
  });
  
  return response.json();
};
```

### **Example 2: Meeting Notes Processor**
```typescript
const processMeetingNotes = async (notes: string) => {
  // Extract key points
  const keyPoints = await fetch('/api/v1/gemini/analyze', {
    method: 'POST',
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify({
      content: notes,
      analysis_type: 'key_points'
    })
  });
  
  // Generate action items
  const actionItems = await fetch('/api/v1/gemini/generate', {
    method: 'POST',
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify({
      prompt: `Based on these meeting notes, generate action items:\n\n${notes}`
    })
  });
  
  return {
    keyPoints: await keyPoints.json(),
    actionItems: await actionItems.json()
  };
};
```

### **Example 3: Content Creation Assistant**
```typescript
const createContent = async (topic: string, type: string, tone: string) => {
  const prompt = `Create a ${type} about ${topic} with a ${tone} tone. Make it engaging and informative.`;
  
  const response = await fetch('/api/v1/gemini/generate', {
    method: 'POST',
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify({ prompt })
  });
  
  return response.json();
};
```

## 🎯 **Integration with Your Existing App**

### **1. Add to Your Dashboard**
```typescript
// In your main Dashboard component
import GeminiChatInterface from '../components/ai/GeminiChatInterface';
import DocumentAnalyzer from '../components/ai/DocumentAnalyzer';
import CodeAssistant from '../components/ai/CodeAssistant';

const Dashboard = () => {
  const [activeTab, setActiveTab] = useState('chat');
  
  return (
    <div className="flex h-screen">
      <Sidebar />
      <div className="flex-1">
        {activeTab === 'chat' && <GeminiChatInterface />}
        {activeTab === 'documents' && <DocumentAnalyzer />}
        {activeTab === 'code' && <CodeAssistant />}
      </div>
    </div>
  );
};
```

### **2. Add AI Features to Existing Components**

**In your Task Management:**
```typescript
const generateTaskDescription = async (taskName: string) => {
  const response = await fetch('/api/v1/gemini/generate', {
    method: 'POST',
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify({
      prompt: `Create a detailed task description for: ${taskName}`
    })
  });
  return response.json();
};
```

**In your File Management:**
```typescript
const analyzeUploadedFile = async (fileContent: string, fileName: string) => {
  const response = await fetch('/api/v1/gemini/analyze', {
    method: 'POST',
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify({
      content: fileContent,
      analysis_type: 'summary'
    })
  });
  return response.json();
};
```

## 🚀 **Advanced Use Cases**

### **1. Automated Workflows**
- **Email Processing**: Auto-categorize and respond to emails
- **Document Pipeline**: Process uploaded documents automatically
- **Code Review**: Integrate with your Git workflow
- **Content Generation**: Auto-generate reports and documentation

### **2. User Experience Enhancements**
- **Smart Search**: Natural language search across your app
- **Intelligent Suggestions**: AI-powered recommendations
- **Context-Aware Help**: Dynamic help system
- **Personalized Interfaces**: Adapt UI based on user behavior

### **3. Business Intelligence**
- **Data Analysis**: Analyze user behavior and patterns
- **Report Generation**: Auto-create business reports
- **Trend Analysis**: Identify patterns in your data
- **Predictive Insights**: Forecast future trends

## 🔧 **Getting Started**

1. **Start your backend server:**
   ```bash
   cd backend
   uvicorn main:app --reload
   ```

2. **Test the API endpoints:**
   ```bash
   # Test text generation
   curl -X POST "http://localhost:8000/api/v1/gemini/generate" \
     -H "Content-Type: application/json" \
     -d '{"prompt": "Hello, how are you?"}'
   ```

3. **Integrate with your frontend:**
   - Use the provided React components
   - Customize the UI to match your design
   - Add error handling and loading states

4. **Build your features:**
   - Start with simple chat functionality
   - Add document analysis
   - Implement code generation
   - Create automated workflows

## 📊 **Monitoring and Analytics**

Track your Gemini API usage:
```typescript
const trackUsage = async (endpoint: string, tokens: number) => {
  // Log usage for analytics
  console.log(`API Usage: ${endpoint} - ${tokens} tokens`);
  
  // Send to your analytics service
  await fetch('/api/analytics/usage', {
    method: 'POST',
    body: JSON.stringify({ endpoint, tokens, timestamp: Date.now() })
  });
};
```

## 🎉 **You're Ready to Build!**

Your Local AI Agent v2 now has:
- ✅ **Full Gemini API integration**
- ✅ **Ready-to-use React components**
- ✅ **Multiple AI capabilities**
- ✅ **Production-ready backend**
- ✅ **Comprehensive documentation**

Start building amazing AI-powered features for your application! 🚀
