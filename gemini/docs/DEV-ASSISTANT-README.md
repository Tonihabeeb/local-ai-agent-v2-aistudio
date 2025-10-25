# 🤖 Development AI Assistant

A standalone AI-powered development assistant that floats over your workspace to help you during coding.

## 🚀 Quick Start

### Option 1: Double-click to start
```
start-dev-assistant.bat
```

### Option 2: PowerShell (Recommended)
```powershell
.\start-dev-assistant.ps1
```

### Option 3: Manual start
1. Start backend: `cd backend && uvicorn main:app --reload`
2. Open: `dev-assistant.html`

## ✨ Features

### 🎯 **Floating Assistant**
- **Always on top** - Stays visible while you code
- **Minimizable** - Collapse to a small icon when not needed
- **Resizable** - Adjust size to your preference
- **Quick toggle** - Show/hide with one click

### 💬 **Smart Chat**
- **Context-aware** - Understands your development context
- **Code analysis** - Paste code for instant feedback
- **Debugging help** - Get assistance with errors and issues
- **Explanations** - Understand complex code quickly

### ⚡ **Quick Actions**
- **🐛 Debug Code** - Get help fixing issues
- **📝 Explain Code** - Understand what code does
- **⚡ Optimize** - Improve performance
- **👀 Code Review** - Get feedback and suggestions

### 🔧 **Development Tools**
- **Code generation** - Generate boilerplate and functions
- **Error analysis** - Debug stack traces and errors
- **Best practices** - Get coding standards advice
- **Documentation** - Generate comments and docs

## 🎮 How to Use

### 1. **Open the Assistant**
- Click the chat icon in the bottom-right corner
- The floating window will appear

### 2. **Ask for Help**
- Type your question or paste code
- Use quick action buttons for common tasks
- Get instant AI-powered responses

### 3. **Common Use Cases**
```
"Help me debug this React component"
"Explain this algorithm"
"Optimize this function for performance"
"Review this code for best practices"
"Generate a login form component"
"Fix this TypeScript error"
```

### 4. **Code Analysis**
- Paste code directly into the chat
- Get instant feedback and suggestions
- Ask for specific improvements
- Request explanations of complex logic

## 🛠️ **Development Workflow**

### **While Coding:**
1. **Keep assistant open** in floating window
2. **Paste problematic code** for instant help
3. **Ask specific questions** about implementation
4. **Get real-time feedback** on your code

### **Code Review:**
1. **Paste code** you want reviewed
2. **Ask for specific feedback** (performance, security, style)
3. **Get improvement suggestions**
4. **Learn best practices**

### **Debugging:**
1. **Describe the issue** you're facing
2. **Paste error messages** or problematic code
3. **Get step-by-step solutions**
4. **Understand root causes**

## 🎯 **Perfect For**

- **Frontend Development** - React, Vue, Angular help
- **Backend Development** - API design, database queries
- **Full-Stack Projects** - End-to-end development assistance
- **Code Reviews** - Get second opinions on your code
- **Learning** - Understand new technologies and patterns
- **Debugging** - Solve complex issues quickly

## 🔧 **Technical Details**

### **Backend Requirements:**
- Python 3.9+
- FastAPI server running on port 8000
- Gemini API key configured

### **Frontend:**
- Pure HTML/CSS/JavaScript
- No build process required
- Works in any modern browser
- Responsive design

### **API Endpoints Used:**
- `POST /api/v1/gemini/chat` - Main chat functionality
- `POST /api/v1/gemini/generate-code` - Code generation
- `POST /api/v1/gemini/review-code` - Code review
- `POST /api/v1/gemini/analyze` - Code analysis

## 🎨 **Customization**

### **Styling:**
- Edit `dev-assistant.html` to customize appearance
- Modify CSS variables for colors and sizing
- Add your own quick action buttons

### **Functionality:**
- Add new quick actions in the JavaScript
- Integrate with your favorite editors
- Connect to additional APIs

## 🚀 **Pro Tips**

1. **Keep it open** - Leave the assistant running while coding
2. **Use quick actions** - Faster than typing full questions
3. **Paste code directly** - Don't just describe, show the actual code
4. **Be specific** - Ask for exactly what you need
5. **Iterate** - Ask follow-up questions for better results

## 🔍 **Troubleshooting**

### **Assistant not responding:**
- Check if backend is running on port 8000
- Verify Gemini API key is set
- Check browser console for errors

### **Backend issues:**
- Ensure Python dependencies are installed
- Check API key configuration
- Verify network connectivity

### **Performance:**
- Minimize when not needed
- Close and reopen if it gets slow
- Check backend logs for issues

## 🎉 **Enjoy Your AI Development Assistant!**

This tool is designed to be your coding companion - always available, always helpful, and always ready to assist with your development tasks.

Happy coding! 🚀
