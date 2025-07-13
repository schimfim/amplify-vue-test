#!/bin/bash

set -e

echo "🚀 Starting About API deployment..."

# Navigate to backend directory
cd backend

# Create virtual environment
echo "🐍 Setting up Python environment..."
python3 -m venv venv
source venv/bin/activate

# Install dependencies
echo "📦 Installing Python dependencies..."
pip install -r requirements.txt

# Install Serverless Framework
echo "☁️ Installing Serverless Framework..."
npm install -g serverless
npm install serverless-python-requirements

# Deploy to AWS Lambda
echo "☁️ Deploying to AWS Lambda..."
serverless deploy --stage $AWS_BRANCH --verbose

# Get the API Gateway URL
echo "🔗 Getting API Gateway URL..."
API_URL=$(serverless info --stage $AWS_BRANCH --verbose | grep -o 'https://[^/]*' | head -1)

if [ -n "$API_URL" ]; then
    echo "✅ API deployed successfully at: $API_URL"
    echo "VITE_API_URL=$API_URL" >> .env
else
    echo "❌ Failed to get API URL"
    exit 1
fi

echo "✅ About API deployment completed!"