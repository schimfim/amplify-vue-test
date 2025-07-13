import os
from typing import Dict, Any

class Config:
    """Configuration class for the About Page API"""
    
    # API Configuration
    API_TITLE = "About Page API"
    API_DESCRIPTION = "REST API for About page data"
    API_VERSION = "1.0.0"
    
    # Environment
    STAGE = os.getenv("STAGE", "dev")
    
    # CORS Configuration
    CORS_ORIGINS = [
        "http://localhost:3000",
        "http://localhost:5173",  # Vite default port
        "https://your-frontend-domain.com"  # Update with your frontend domain
    ]
    
    # Sample data - in production, this would come from a database
    ABOUT_DATA = {
        "name": os.getenv("ABOUT_NAME", "John Doe"),
        "email": os.getenv("ABOUT_EMAIL", "john.doe@example.com")
    }
    
    @classmethod
    def get_about_data(cls) -> Dict[str, Any]:
        """Get the about data with environment variable overrides"""
        return {
            "name": os.getenv("ABOUT_NAME", cls.ABOUT_DATA["name"]),
            "email": os.getenv("ABOUT_EMAIL", cls.ABOUT_DATA["email"])
        }