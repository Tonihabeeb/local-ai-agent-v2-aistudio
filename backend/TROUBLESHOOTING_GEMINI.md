# Gemini API Troubleshooting Guide

## Issue: API Key Not Valid

The error "API key not valid" typically occurs due to one of these reasons:

### 1. API Key Activation Delay
- **Problem**: New API keys sometimes take a few minutes to activate
- **Solution**: Wait 5-10 minutes and try again

### 2. Incorrect API Key Format
- **Problem**: The key might have extra characters or be truncated
- **Solution**: 
  1. Go back to [Google AI Studio](https://aistudio.google.com/)
  2. Click on your API key
  3. Copy the key again carefully
  4. Make sure there are no extra spaces or characters

### 3. API Key Permissions
- **Problem**: The API key might not have the right permissions
- **Solution**:
  1. In Google AI Studio, check your API key settings
  2. Make sure it has access to the Gemini API
  3. Verify the project is active

### 4. Billing/Quota Issues
- **Problem**: Your Google Cloud project might need billing enabled
- **Solution**:
  1. Go to [Google Cloud Console](https://console.cloud.google.com/)
  2. Select your project
  3. Enable billing if not already enabled
  4. Check quota limits

## Steps to Fix:

### Step 1: Verify API Key
1. Go to [Google AI Studio](https://aistudio.google.com/)
2. Click on "Get API key" in the left sidebar
3. Find your "Local agent aiStudio" key
4. Click on it to view details
5. Copy the key again (make sure it's exactly: `AlzaSyBuBtWuWDuX0SUWW-n_xWk7QA0qLOKsWcE`)

### Step 2: Test with cURL
Run this command to test the API key directly:

```bash
curl -H "x-goog-api-key: YOUR_API_KEY" \
  "https://generativelanguage.googleapis.com/v1beta/models"
```

### Step 3: Check Project Status
1. Go to [Google Cloud Console](https://console.cloud.google.com/)
2. Select project: `projects/951447911609`
3. Check if billing is enabled
4. Verify the Generative AI API is enabled

### Step 4: Regenerate API Key (if needed)
If the above doesn't work:
1. Delete the current API key
2. Create a new one
3. Test with the new key

## Alternative: Use Google AI Studio Directly

If you want to test the API without the backend:
1. Go to [Google AI Studio](https://aistudio.google.com/)
2. Use the "Get started" section
3. Test your prompts directly in the interface

## Next Steps

Once the API key is working:
1. Set it as an environment variable: `$env:GEMINI_API_KEY="your-key"`
2. Run the test: `python simple_gemini_test.py`
3. If successful, your backend will be ready to use!

## Support

If you continue having issues:
- Check the [Gemini API documentation](https://ai.google.dev/gemini-api/docs/quickstart)
- Verify your Google Cloud project settings
- Try creating a new API key
