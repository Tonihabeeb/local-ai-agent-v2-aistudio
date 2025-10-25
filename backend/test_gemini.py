"""
Test script for Gemini API integration
"""

import asyncio
import os
from app.services.gemini_service import GeminiService

async def test_gemini_connection():
    """Test Gemini API connection"""
    print("Testing Gemini API connection...")
    
    # Check if API key is set
    api_key = os.getenv('GEMINI_API_KEY')
    if not api_key:
        print("ERROR: GEMINI_API_KEY environment variable not set")
        print("Please set your Gemini API key:")
        print("export GEMINI_API_KEY=your-api-key-here")
        return False

    print(f"SUCCESS: API key found: {api_key[:10]}...")
    
    try:
        # Initialize service
        gemini = GeminiService()
        print("SUCCESS: Gemini service initialized")
        
        # Test health check
        health = await gemini.health_check()
        print(f"Health check: {health}")
        
        if health.get('status') == 'healthy':
            print("SUCCESS: Gemini API is healthy")
            
            # Test simple text generation
            print("\nTesting text generation...")
            result = await gemini.generate_text("Hello, this is a test message. Please respond briefly.")
            
            if result.get('success'):
                print("SUCCESS: Text generation successful")
                print(f"Response: {result.get('text', 'No text returned')}")
            else:
                print(f"ERROR: Text generation failed: {result.get('error')}")
                return False
                
        else:
            print(f"ERROR: Gemini API is unhealthy: {health.get('error', 'Unknown error')}")
            return False
            
    except Exception as e:
        print(f"ERROR: Error testing Gemini API: {str(e)}")
        return False
    
    print("\nSUCCESS: All tests passed! Gemini API is working correctly.")
    return True

if __name__ == "__main__":
    asyncio.run(test_gemini_connection())
