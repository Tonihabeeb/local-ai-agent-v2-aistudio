"""
Gemini API Service
Handles communication with Google's Gemini API
"""

import os
from typing import Optional, Dict, Any, List
from google import genai
import logging

logger = logging.getLogger(__name__)

class GeminiService:
    """Service for interacting with Google's Gemini API"""
    
    def __init__(self):
        """Initialize the Gemini service with API key from environment"""
        self.api_key = os.getenv('GEMINI_API_KEY')
        if not self.api_key:
            raise ValueError("GEMINI_API_KEY environment variable is required")
        
        self.client = genai.Client(api_key=self.api_key)
        self.model = "gemini-2.5-flash"  # Default model
    
    async def generate_text(self, prompt: str, model: Optional[str] = None) -> Dict[str, Any]:
        """
        Generate text using Gemini API
        
        Args:
            prompt: The input prompt for text generation
            model: Optional model name (defaults to gemini-2.5-flash)
            
        Returns:
            Dict containing the generated text and metadata
        """
        try:
            model_name = model or self.model
            response = self.client.models.generate_content(
                model=model_name,
                contents=prompt
            )
            
            return {
                "success": True,
                "text": response.text,
                "model": model_name,
                "usage": getattr(response, 'usage_metadata', None)
            }
        except Exception as e:
            logger.error(f"Error generating text with Gemini: {str(e)}")
            return {
                "success": False,
                "error": str(e),
                "text": None
            }
    
    async def generate_with_context(self, prompt: str, context: str, model: Optional[str] = None) -> Dict[str, Any]:
        """
        Generate text with additional context
        
        Args:
            prompt: The main prompt
            context: Additional context to include
            model: Optional model name
            
        Returns:
            Dict containing the generated text and metadata
        """
        full_prompt = f"Context: {context}\n\nPrompt: {prompt}"
        return await self.generate_text(full_prompt, model)
    
    async def chat_completion(self, messages: List[Dict[str, str]], model: Optional[str] = None) -> Dict[str, Any]:
        """
        Chat completion using conversation history
        
        Args:
            messages: List of message objects with 'role' and 'content'
            model: Optional model name
            
        Returns:
            Dict containing the response and metadata
        """
        try:
            model_name = model or self.model
            
            # Convert messages to Gemini format
            contents = []
            for message in messages:
                role = message.get('role', 'user')
                content = message.get('content', '')
                
                if role == 'system':
                    # Gemini doesn't have system messages, prepend to first user message
                    if contents and contents[-1].get('role') == 'user':
                        contents[-1]['parts'][0]['text'] = f"System: {content}\n\n{contents[-1]['parts'][0]['text']}"
                    else:
                        # If no user message yet, create one
                        contents.append({
                            'role': 'user',
                            'parts': [{'text': f"System: {content}"}]
                        })
                elif role in ['user', 'assistant']:
                    contents.append({
                        'role': role,
                        'parts': [{'text': content}]
                    })
            
            response = self.client.models.generate_content(
                model=model_name,
                contents=contents
            )
            
            return {
                "success": True,
                "text": response.text,
                "model": model_name,
                "usage": getattr(response, 'usage_metadata', None)
            }
        except Exception as e:
            logger.error(f"Error in chat completion: {str(e)}")
            return {
                "success": False,
                "error": str(e),
                "text": None
            }
    
    async def analyze_document(self, content: str, analysis_type: str = "summary") -> Dict[str, Any]:
        """
        Analyze document content
        
        Args:
            content: Document content to analyze
            analysis_type: Type of analysis (summary, key_points, sentiment, etc.)
            
        Returns:
            Dict containing analysis results
        """
        prompts = {
            "summary": "Provide a concise summary of the following document:",
            "key_points": "Extract the key points from the following document:",
            "sentiment": "Analyze the sentiment of the following text:",
            "translation": "Translate the following text to English:",
            "qa": "Answer questions about the following document:"
        }
        
        prompt = prompts.get(analysis_type, "Analyze the following content:")
        full_prompt = f"{prompt}\n\n{content}"
        
        return await self.generate_text(full_prompt)
    
    async def code_generation(self, description: str, language: str = "python") -> Dict[str, Any]:
        """
        Generate code based on description
        
        Args:
            description: Description of what the code should do
            language: Programming language
            
        Returns:
            Dict containing generated code
        """
        prompt = f"Generate {language} code for: {description}"
        return await self.generate_text(prompt)
    
    async def code_review(self, code: str, language: str = "python") -> Dict[str, Any]:
        """
        Review and provide feedback on code
        
        Args:
            code: Code to review
            language: Programming language
            
        Returns:
            Dict containing code review feedback
        """
        prompt = f"Review the following {language} code and provide feedback on:\n1. Code quality\n2. Potential bugs\n3. Best practices\n4. Suggestions for improvement\n\nCode:\n{code}"
        return await self.generate_text(prompt)
    
    def get_available_models(self) -> List[str]:
        """
        Get list of available Gemini models
        
        Returns:
            List of available model names
        """
        return [
            "gemini-2.5-flash",
            "gemini-2.5-pro",
            "gemini-1.5-flash",
            "gemini-1.5-pro"
        ]
    
    async def health_check(self) -> Dict[str, Any]:
        """
        Check if the Gemini API is accessible
        
        Returns:
            Dict containing health status
        """
        try:
            response = await self.generate_text("Hello, this is a health check.")
            return {
                "status": "healthy" if response.get("success") else "unhealthy",
                "api_key_configured": bool(self.api_key),
                "client_initialized": bool(self.client)
            }
        except Exception as e:
            return {
                "status": "unhealthy",
                "error": str(e),
                "api_key_configured": bool(self.api_key),
                "client_initialized": bool(self.client)
            }
