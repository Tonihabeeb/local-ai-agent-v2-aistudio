"""
Simple test for Gemini API connection
"""

import os
from google import genai

def test_gemini_simple():
    """Simple test for Gemini API"""
    print("Testing Gemini API connection...")
    
    # Check if API key is set
    api_key = os.getenv('GEMINI_API_KEY')
    if not api_key:
        print("ERROR: GEMINI_API_KEY environment variable not set")
        return False
    
    print(f"SUCCESS: API key found: {api_key[:10]}...")
    
    try:
        # Initialize client
        client = genai.Client(api_key=api_key)
        print("SUCCESS: Gemini client initialized")
        
        # Test simple generation
        print("Testing text generation...")
        response = client.models.generate_content(
            model="gemini-2.5-flash",
            contents="Hello! Please respond with a brief greeting."
        )
        
        print("SUCCESS: Text generation successful!")
        print(f"Response: {response.text}")
        
        return True
        
    except Exception as e:
        print(f"ERROR: {str(e)}")
        return False

if __name__ == "__main__":
    success = test_gemini_simple()
    if success:
        print("\nSUCCESS: Gemini API is working correctly!")
    else:
        print("\nFAILED: Gemini API test failed!")