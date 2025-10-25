"""
Application settings and configuration
"""

import os
from typing import Optional
from pydantic import BaseSettings, Field

class Settings(BaseSettings):
    """Application settings"""
    
    # Database settings
    database_url: str = Field(default="sqlite:///./app.db", env="DATABASE_URL")
    
    # API settings
    api_v1_prefix: str = "/api/v1"
    project_name: str = "Local AI Agent v2"
    version: str = "2.0.0"
    
    # Security settings
    secret_key: str = Field(default="your-secret-key-here", env="SECRET_KEY")
    access_token_expire_minutes: int = 30
    
    # Gemini API settings
    gemini_api_key: Optional[str] = Field(default=None, env="GEMINI_API_KEY")
    gemini_model: str = Field(default="gemini-2.5-flash", env="GEMINI_MODEL")
    
    # OpenAI API settings (if using OpenAI as well)
    openai_api_key: Optional[str] = Field(default=None, env="OPENAI_API_KEY")
    openai_model: str = Field(default="gpt-3.5-turbo", env="OPENAI_MODEL")
    
    # CORS settings
    allowed_origins: list = ["http://localhost:3000", "http://localhost:5173"]
    
    # Logging settings
    log_level: str = Field(default="INFO", env="LOG_LEVEL")
    
    # Development settings
    debug: bool = Field(default=False, env="DEBUG")
    
    class Config:
        env_file = ".env"
        case_sensitive = False

# Global settings instance
settings = Settings()