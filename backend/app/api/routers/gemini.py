"""
Gemini API Router
Handles all Gemini API endpoints
"""

from fastapi import APIRouter, HTTPException, Depends
from typing import List, Optional, Dict, Any
from pydantic import BaseModel
import logging

from app.services.gemini_service import GeminiService
from app.core.settings import settings

logger = logging.getLogger(__name__)

router = APIRouter(prefix="/gemini", tags=["gemini"])

# Pydantic models for request/response
class TextGenerationRequest(BaseModel):
    prompt: str
    model: Optional[str] = None

class TextGenerationResponse(BaseModel):
    success: bool
    text: Optional[str] = None
    model: str
    error: Optional[str] = None

class ChatRequest(BaseModel):
    messages: List[Dict[str, str]]
    model: Optional[str] = None

class DocumentAnalysisRequest(BaseModel):
    content: str
    analysis_type: str = "summary"

class CodeGenerationRequest(BaseModel):
    description: str
    language: str = "python"

class CodeReviewRequest(BaseModel):
    code: str
    language: str = "python"

class ContextRequest(BaseModel):
    prompt: str
    context: str
    model: Optional[str] = None

# Dependency to get Gemini service
def get_gemini_service() -> GeminiService:
    """Get Gemini service instance"""
    try:
        return GeminiService()
    except ValueError as e:
        raise HTTPException(status_code=500, detail=f"Gemini API not configured: {str(e)}")

@router.post("/generate", response_model=TextGenerationResponse)
async def generate_text(
    request: TextGenerationRequest,
    gemini: GeminiService = Depends(get_gemini_service)
):
    """Generate text using Gemini API"""
    try:
        result = await gemini.generate_text(request.prompt, request.model)
        return TextGenerationResponse(
            success=result["success"],
            text=result.get("text"),
            model=result.get("model", settings.gemini_model),
            error=result.get("error")
        )
    except Exception as e:
        logger.error(f"Error in text generation: {str(e)}")
        raise HTTPException(status_code=500, detail=str(e))

@router.post("/chat", response_model=TextGenerationResponse)
async def chat_completion(
    request: ChatRequest,
    gemini: GeminiService = Depends(get_gemini_service)
):
    """Chat completion using conversation history"""
    try:
        result = await gemini.chat_completion(request.messages, request.model)
        return TextGenerationResponse(
            success=result["success"],
            text=result.get("text"),
            model=result.get("model", settings.gemini_model),
            error=result.get("error")
        )
    except Exception as e:
        logger.error(f"Error in chat completion: {str(e)}")
        raise HTTPException(status_code=500, detail=str(e))

@router.post("/analyze", response_model=TextGenerationResponse)
async def analyze_document(
    request: DocumentAnalysisRequest,
    gemini: GeminiService = Depends(get_gemini_service)
):
    """Analyze document content"""
    try:
        result = await gemini.analyze_document(request.content, request.analysis_type)
        return TextGenerationResponse(
            success=result["success"],
            text=result.get("text"),
            model=result.get("model", settings.gemini_model),
            error=result.get("error")
        )
    except Exception as e:
        logger.error(f"Error in document analysis: {str(e)}")
        raise HTTPException(status_code=500, detail=str(e))

@router.post("/generate-code", response_model=TextGenerationResponse)
async def generate_code(
    request: CodeGenerationRequest,
    gemini: GeminiService = Depends(get_gemini_service)
):
    """Generate code based on description"""
    try:
        result = await gemini.code_generation(request.description, request.language)
        return TextGenerationResponse(
            success=result["success"],
            text=result.get("text"),
            model=result.get("model", settings.gemini_model),
            error=result.get("error")
        )
    except Exception as e:
        logger.error(f"Error in code generation: {str(e)}")
        raise HTTPException(status_code=500, detail=str(e))

@router.post("/review-code", response_model=TextGenerationResponse)
async def review_code(
    request: CodeReviewRequest,
    gemini: GeminiService = Depends(get_gemini_service)
):
    """Review and provide feedback on code"""
    try:
        result = await gemini.code_review(request.code, request.language)
        return TextGenerationResponse(
            success=result["success"],
            text=result.get("text"),
            model=result.get("model", settings.gemini_model),
            error=result.get("error")
        )
    except Exception as e:
        logger.error(f"Error in code review: {str(e)}")
        raise HTTPException(status_code=500, detail=str(e))

@router.post("/context", response_model=TextGenerationResponse)
async def generate_with_context(
    request: ContextRequest,
    gemini: GeminiService = Depends(get_gemini_service)
):
    """Generate text with additional context"""
    try:
        result = await gemini.generate_with_context(
            request.prompt, 
            request.context, 
            request.model
        )
        return TextGenerationResponse(
            success=result["success"],
            text=result.get("text"),
            model=result.get("model", settings.gemini_model),
            error=result.get("error")
        )
    except Exception as e:
        logger.error(f"Error in context generation: {str(e)}")
        raise HTTPException(status_code=500, detail=str(e))

@router.get("/models")
async def get_available_models(gemini: GeminiService = Depends(get_gemini_service)):
    """Get list of available Gemini models"""
    try:
        models = gemini.get_available_models()
        return {"models": models}
    except Exception as e:
        logger.error(f"Error getting models: {str(e)}")
        raise HTTPException(status_code=500, detail=str(e))

@router.get("/health")
async def health_check(gemini: GeminiService = Depends(get_gemini_service)):
    """Check Gemini API health status"""
    try:
        result = await gemini.health_check()
        return result
    except Exception as e:
        logger.error(f"Error in health check: {str(e)}")
        return {
            "status": "unhealthy",
            "error": str(e),
            "api_key_configured": bool(settings.gemini_api_key)
        }
