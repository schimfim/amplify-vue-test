#!/bin/bash

# About Page API Deployment Script

set -e

echo "🚀 Starting deployment of About Page API..."

# Check if AWS CLI is configured
if ! aws sts get-caller-identity &> /dev/null; then
    echo "❌ AWS CLI is not configured. Please run 'aws configure' first."
    exit 1
fi

# Check if serverless is installed
if ! command -v serverless &> /dev/null; then
    echo "❌ Serverless Framework is not installed. Installing..."
    npm install -g serverless
fi

# Install dependencies
echo "📦 Installing dependencies..."
npm install

# Create virtual environment and install Python dependencies
echo "🐍 Setting up Python environment..."
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt

# Run tests
echo "🧪 Running tests..."
python -m pytest tests/ -v

# Deploy to AWS
echo "☁️ Deploying to AWS Lambda..."
serverless deploy --verbose

echo "✅ Deployment completed successfully!"
echo ""
echo "📋 API Endpoints:"
echo "  - Root: $(serverless info --verbose | grep -o 'https://[^/]*')/"
echo "  - Health: $(serverless info --verbose | grep -o 'https://[^/]*')/health"
echo "  - About: $(serverless info --verbose | grep -o 'https://[^/]*')/api/about"
echo "  - Name: $(serverless info --verbose | grep -o 'https://[^/]*')/api/about/name"
echo ""
echo "🔧 To update the frontend API URL, set VITE_API_URL to the base URL above"