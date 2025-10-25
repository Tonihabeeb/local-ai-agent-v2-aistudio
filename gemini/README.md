# 🤖 Gemini AI Assistant Components

This folder contains all components related to the Gemini AI integration for the Local AI Agent v2 project.

## 📁 Folder Structure

```
gemini/
├── components/          # React components for AI features
│   ├── CodeAssistant.tsx
│   ├── DocumentAnalyzer.tsx
│   └── GeminiChatInterface.tsx
├── pages/              # React pages that use AI components
│   └── AIAssistant.tsx
├── standalone/         # Standalone HTML applications
│   ├── dev-assistant.html
│   ├── test-ai-assistant.html
│   ├── start-dev-assistant.bat
│   └── start-dev-assistant.ps1
├── docs/              # Documentation and guides
│   ├── GEMINI_INTEGRATION.md
│   ├── GEMINI_USAGE_GUIDE.md
│   ├── TROUBLESHOOTING_GEMINI.md
│   └── DEV-ASSISTANT-README.md
└── README.md          # This file
```

## 🚀 Quick Start

### **For Development Use (Standalone)**
```bash
cd gemini/standalone
# Windows
start-dev-assistant.bat
# PowerShell (Recommended)
.\start-dev-assistant.ps1
```

### **For Integration (React Components)**
```typescript
// Import components in your React app
import CodeAssistant from './gemini/components/CodeAssistant';
import DocumentAnalyzer from './gemini/components/DocumentAnalyzer';
import GeminiChatInterface from './gemini/components/GeminiChatInterface';
```

## 📋 Components Overview

### **🤖 AI Components**
- **`CodeAssistant.tsx`** - Code generation and review
- **`DocumentAnalyzer.tsx`** - Document analysis and processing
- **`GeminiChatInterface.tsx`** - Chat interface with AI

### **📄 Pages**
- **`AIAssistant.tsx`** - Main AI assistant page with tabs

### **🛠️ Standalone Tools**
- **`dev-assistant.html`** - Floating development assistant
- **`test-ai-assistant.html`** - Test interface for AI features
- **`start-dev-assistant.*`** - Launcher scripts

### **📚 Documentation**
- **`GEMINI_INTEGRATION.md`** - Backend integration guide
- **`GEMINI_USAGE_GUIDE.md`** - Usage examples and features
- **`TROUBLESHOOTING_GEMINI.md`** - Common issues and solutions
- **`DEV-ASSISTANT-README.md`** - Standalone assistant guide

## 🎯 Use Cases

### **1. Development Assistant (Standalone)**
Perfect for daily development work:
- Floating AI assistant while coding
- Quick code analysis and debugging
- Real-time help with development issues

### **2. Integrated AI Features**
For your main application:
- AI-powered chat system
- Document processing capabilities
- Code generation and review tools

### **3. Testing and Development**
For testing AI features:
- Test interface for all AI capabilities
- API endpoint testing
- Feature validation

## 🔧 Backend Requirements

All components require the backend server running:
```bash
cd backend
uvicorn main:app --reload --host 0.0.0.0 --port 8000
```

## 📖 Documentation

- **Integration Guide**: `docs/GEMINI_INTEGRATION.md`
- **Usage Examples**: `docs/GEMINI_USAGE_GUIDE.md`
- **Troubleshooting**: `docs/TROUBLESHOOTING_GEMINI.md`
- **Standalone Assistant**: `docs/DEV-ASSISTANT-README.md`

## 🎉 Getting Started

1. **For standalone use**: Go to `standalone/` folder
2. **For integration**: Import components from `components/` folder
3. **For testing**: Use files in `standalone/` folder
4. **For documentation**: Check `docs/` folder

All Gemini AI components are now organized and ready to use! 🚀
