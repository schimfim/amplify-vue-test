import pytest
from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

def test_root_endpoint():
    """Test the root endpoint"""
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"message": "About Page API is running"}

def test_health_check():
    """Test the health check endpoint"""
    response = client.get("/health")
    assert response.status_code == 200
    assert response.json() == {"status": "healthy", "service": "about-api"}

def test_get_about_data():
    """Test getting complete about data"""
    response = client.get("/api/about")
    assert response.status_code == 200
    data = response.json()
    assert "name" in data
    assert "email" in data
    assert data["name"] == "John Doe"
    assert data["email"] == "john.doe@example.com"

def test_get_name_only():
    """Test getting just the name"""
    response = client.get("/api/about/name")
    assert response.status_code == 200
    data = response.json()
    assert "name" in data
    assert data["name"] == "John Doe"