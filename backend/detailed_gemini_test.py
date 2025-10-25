"""
Detailed test for Gemini API connection with troubleshooting
"""

import os
import requests
from google import genai

def test_gemini_detailed():
    """Detailed test for Gemini API with troubleshooting"""
    print("=== Gemini API Detailed Test ===")
    
    # Check if API key is set
    api_key = os.getenv('GEMINI_API_KEY')
    if not api_key:
        print("ERROR: GEMINI_API_KEY environment variable not set")
        return False
    
    print(f"API Key: {api_key[:10]}...{api_key[-4:]}")
    print(f"Key Length: {len(api_key)} characters")
    
    # Test 1: Direct API call to check key validity
    print("\n--- Test 1: Direct API Validation ---")
    try:
        url = "https://generativelanguage.googleapis.com/v1beta/models"
        headers = {"x-goog-api-key": api_key}
        response = requests.get(url, headers=headers, timeout=10)
        
        if response.status_code == 200:
            print("SUCCESS: API key is valid for model listing")
            models = response.json()
            print(f"Available models: {len(models.get('models', []))}")
        else:
            print(f"ERROR: API key validation failed with status {response.status_code}")
            print(f"Response: {response.text}")
            return False
            
    except Exception as e:
        print(f"ERROR: Direct API test failed: {str(e)}")
        return False
    
    # Test 2: Simple generation with direct API call
    print("\n--- Test 2: Direct Generation API Call ---")
    try:
        url = "https://generativelanguage.googleapis.com/v1beta/models/gemini-2.5-flash:generateContent"
        headers = {
            "x-goog-api-key": api_key,
            "Content-Type": "application/json"
        }
        data = {
            "contents": [{
                "parts": [{"text": "Hello! Please respond with just 'Hi there!'"}]
            }]
        }
        
        response = requests.post(url, headers=headers, json=data, timeout=30)
        
        if response.status_code == 200:
            result = response.json()
            if 'candidates' in result and len(result['candidates']) > 0:
                text = result['candidates'][0]['content']['parts'][0]['text']
                print(f"SUCCESS: Direct API generation works!")
                print(f"Response: {text}")
            else:
                print("ERROR: No candidates in response")
                print(f"Response: {result}")
                return False
        else:
            print(f"ERROR: Generation failed with status {response.status_code}")
            print(f"Response: {response.text}")
            return False
            
    except Exception as e:
        print(f"ERROR: Direct generation test failed: {str(e)}")
        return False
    
    # Test 3: Google GenAI SDK
    print("\n--- Test 3: Google GenAI SDK ---")
    try:
        client = genai.Client(api_key=api_key)
        response = client.models.generate_content(
            model="gemini-2.5-flash",
            contents="Hello! Please respond with just 'SDK works!'"
        )
        
        print(f"SUCCESS: SDK generation works!")
        print(f"Response: {response.text}")
        
        return True
        
    except Exception as e:
        print(f"ERROR: SDK test failed: {str(e)}")
        return False

if __name__ == "__main__":
    success = test_gemini_detailed()
    if success:
        print("\n=== ALL TESTS PASSED ===")
        print("Gemini API is fully functional!")
    else:
        print("\n=== TESTS FAILED ===")
        print("Please check your API key and try again.")
