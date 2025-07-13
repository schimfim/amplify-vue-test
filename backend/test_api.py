#!/usr/bin/env python3
"""
Simple test script to verify the API endpoints
"""

import requests
import json
import sys

def test_api(base_url="http://localhost:8000"):
    """Test all API endpoints"""
    
    endpoints = [
        ("/", "Root endpoint"),
        ("/health", "Health check"),
        ("/api/about", "About data"),
        ("/api/about/name", "Name only")
    ]
    
    print(f"🧪 Testing API at {base_url}")
    print("=" * 50)
    
    for endpoint, description in endpoints:
        try:
            url = f"{base_url}{endpoint}"
            response = requests.get(url, timeout=10)
            
            if response.status_code == 200:
                print(f"✅ {description}: {response.status_code}")
                print(f"   Response: {json.dumps(response.json(), indent=2)}")
            else:
                print(f"❌ {description}: {response.status_code}")
                print(f"   Error: {response.text}")
                
        except requests.exceptions.RequestException as e:
            print(f"❌ {description}: Connection failed")
            print(f"   Error: {e}")
        
        print("-" * 30)
    
    print("🎉 API testing completed!")

if __name__ == "__main__":
    # Allow custom base URL
    base_url = sys.argv[1] if len(sys.argv) > 1 else "http://localhost:8000"
    test_api(base_url)