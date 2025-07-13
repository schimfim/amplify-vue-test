from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from mangum import Mangum
from pydantic import BaseModel
from typing import Dict, Any
from config import Config

app = FastAPI(
    title=Config.API_TITLE,
    description=Config.API_DESCRIPTION,
    version=Config.API_VERSION
)

# Add CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=Config.CORS_ORIGINS,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class AboutData(BaseModel):
    name: str
    email: str

@app.get("/")
async def root():
    """Root endpoint"""
    return {"message": "About Page API is running"}

@app.get("/health")
async def health_check():
    """Health check endpoint"""
    return {"status": "healthy", "service": "about-api"}

@app.get("/api/about", response_model=AboutData)
async def get_about_data():
    """Get the about page data including name and email"""
    try:
        about_data = Config.get_about_data()
        return AboutData(**about_data)
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Internal server error: {str(e)}")

@app.get("/api/about/name")
async def get_name():
    """Get just the name for the about page"""
    try:
        about_data = Config.get_about_data()
        return {"name": about_data["name"]}
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Internal server error: {str(e)}")

# Handler for AWS Lambda
handler = Mangum(app, lifespan="off")