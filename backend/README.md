# About Page API Backend

A Python FastAPI backend that provides REST APIs for the About page data. This service runs on AWS Lambda using the Serverless Framework.

## Features

- REST API endpoints for About page data
- AWS Lambda deployment
- Health check endpoint
- Unit tests
- FastAPI with automatic OpenAPI documentation

## API Endpoints

- `GET /` - Root endpoint
- `GET /health` - Health check
- `GET /api/about` - Get complete about data (name and email)
- `GET /api/about/name` - Get just the name

## Setup

### Prerequisites

- Python 3.11+
- Node.js 18+
- AWS CLI configured
- Serverless Framework

### Installation

1. Install Python dependencies:
```bash
pip install -r requirements.txt
```

2. Install Node.js dependencies:
```bash
npm install
```

3. Configure AWS credentials:
```bash
aws configure
```

## Development

### Local Development

Run the API locally for development:
```bash
npm run dev
```

The API will be available at `http://localhost:8000`

### Testing

Run the test suite:
```bash
npm test
```

## Deployment

### Deploy to AWS Lambda

Deploy to development stage:
```bash
npm run deploy
```

Deploy to production stage:
```bash
npm run deploy:prod
```

### Remove Deployment

Remove the deployed resources:
```bash
npm run remove
```

## Environment Variables

- `STAGE` - Deployment stage (dev/prod)

## Architecture

- **Framework**: FastAPI
- **AWS Integration**: Mangum adapter for Lambda
- **Deployment**: Serverless Framework
- **Runtime**: Python 3.11 on AWS Lambda

## API Response Examples

### Get About Data
```json
{
  "name": "John Doe",
  "email": "john.doe@example.com"
}
```

### Get Name Only
```json
{
  "name": "John Doe"
}
```