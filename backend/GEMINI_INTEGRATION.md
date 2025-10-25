# Gemini API Integration

This document explains how to set up and use the Gemini API integration in the Local AI Agent v2 backend.

## Setup

### 1. Get a Gemini API Key

1. Go to [Google AI Studio](https://aistudio.google.com/)
2. Sign in with your Google account
3. Click "Get API key" in the left sidebar
4. Create a new API key
5. Copy the API key

### 2. Configure Environment Variables

Create a `.env` file in the backend directory with your API key:

```bash
# Copy the example file
cp env.example .env

# Edit the .env file and add your API key
GEMINI_API_KEY=your-actual-api-key-here
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

## API Endpoints

The Gemini integration provides the following endpoints:

### Text Generation
- `POST /api/v1/gemini/generate` - Generate text from a prompt
- `POST /api/v1/gemini/chat` - Chat completion with conversation history
- `POST /api/v1/gemini/context` - Generate text with additional context

### Document Analysis
- `POST /api/v1/gemini/analyze` - Analyze document content (summary, key points, sentiment, etc.)

### Code Generation & Review
- `POST /api/v1/gemini/generate-code` - Generate code based on description
- `POST /api/v1/gemini/review-code` - Review and provide feedback on code

### Utility Endpoints
- `GET /api/v1/gemini/models` - Get available Gemini models
- `GET /api/v1/gemini/health` - Check API health status

## Usage Examples

### 1. Text Generation

```bash
curl -X POST "http://localhost:8000/api/v1/gemini/generate" \
  -H "Content-Type: application/json" \
  -d '{
    "prompt": "Explain quantum computing in simple terms",
    "model": "gemini-2.5-flash"
  }'
```

### 2. Chat Completion

```bash
curl -X POST "http://localhost:8000/api/v1/gemini/chat" \
  -H "Content-Type: application/json" \
  -d '{
    "messages": [
      {"role": "user", "content": "Hello, how are you?"},
      {"role": "assistant", "content": "I am doing well, thank you!"},
      {"role": "user", "content": "What can you help me with?"}
    ]
  }'
```

### 3. Document Analysis

```bash
curl -X POST "http://localhost:8000/api/v1/gemini/analyze" \
  -H "Content-Type: application/json" \
  -d '{
    "content": "Your document content here...",
    "analysis_type": "summary"
  }'
```

### 4. Code Generation

```bash
curl -X POST "http://localhost:8000/api/v1/gemini/generate-code" \
  -H "Content-Type: application/json" \
  -d '{
    "description": "Create a function to calculate fibonacci numbers",
    "language": "python"
  }'
```

## Available Models

- `gemini-2.5-flash` (default) - Fast and efficient
- `gemini-2.5-pro` - More capable for complex tasks
- `gemini-1.5-flash` - Legacy fast model
- `gemini-1.5-pro` - Legacy pro model

## Testing

Run the test script to verify your setup:

```bash
python test_gemini.py
```

## Error Handling

The API includes comprehensive error handling:

- Invalid API keys return 500 status with error details
- Rate limiting is handled gracefully
- Network errors are caught and reported
- All responses include success/error status

## Rate Limits

Gemini API has rate limits based on your usage tier. The integration handles rate limiting automatically and will return appropriate error messages when limits are exceeded.

## Security

- API keys are stored in environment variables
- Never commit API keys to version control
- Use the `.env` file for local development
- For production, use secure environment variable management

## Troubleshooting

### Common Issues

1. **"GEMINI_API_KEY environment variable is required"**
   - Make sure you've set the `GEMINI_API_KEY` in your `.env` file
   - Restart your application after setting the environment variable

2. **"Gemini API not configured"**
   - Check that your API key is valid
   - Verify the API key has the necessary permissions

3. **Rate limit exceeded**
   - Wait before making more requests
   - Consider upgrading your API tier if needed

4. **Network errors**
   - Check your internet connection
   - Verify the Gemini API is accessible from your network

### Getting Help

- Check the [Gemini API documentation](https://ai.google.dev/gemini-api/docs/quickstart)
- Review the error messages in the API responses
- Check the application logs for detailed error information
