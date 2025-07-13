#!/bin/bash

set -e

echo "🚀 Building and deploying Python backend with Amplify..."

# Set environment variables
export STAGE=${AWS_BRANCH:-dev}
export ABOUT_NAME=${ABOUT_NAME:-"John Doe"}
export ABOUT_EMAIL=${ABOUT_EMAIL:-"john.doe@example.com"}

echo "📋 Environment:"
echo "  STAGE: $STAGE"
echo "  ABOUT_NAME: $ABOUT_NAME"
echo "  ABOUT_EMAIL: $ABOUT_EMAIL"

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
serverless deploy --stage $STAGE --verbose

# Get the API Gateway URL
echo "🔗 Getting API Gateway URL..."
API_URL=$(serverless info --stage $STAGE --verbose | grep -o 'https://[^/]*' | head -1)

if [ -n "$API_URL" ]; then
    echo "✅ API deployed successfully at: $API_URL"
    # Create environment file for frontend
    echo "VITE_API_URL=$API_URL" > ../.env
    echo "✅ Environment file created with API URL"
else
    echo "❌ Failed to get API URL"
    exit 1
fi

echo "✅ Backend deployment completed successfully!"