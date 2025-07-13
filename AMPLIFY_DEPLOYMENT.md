# Deploying with AWS Amplify

This guide explains how to deploy both the Vue.js frontend and Python backend using AWS Amplify.

## 🏗️ Architecture Overview

- **Frontend**: Vue.js 3 application deployed to Amplify Hosting
- **Backend**: Python FastAPI deployed to AWS Lambda via Serverless Framework
- **Build Process**: Amplify handles both frontend and backend builds automatically

## 📋 Prerequisites

1. **AWS Account** with appropriate permissions
2. **Amplify CLI** installed: `npm install -g @aws-amplify/cli`
3. **Git repository** connected to your project

## 🚀 Deployment Steps

### 1. Initialize Amplify (if not already done)

```bash
amplify init
```

### 2. Configure Environment Variables

Set these environment variables in your Amplify app settings:

- `ABOUT_NAME`: Name to display on About page
- `ABOUT_EMAIL`: Email to display on About page
- `AWS_ACCESS_KEY_ID`: Your AWS access key
- `AWS_SECRET_ACCESS_KEY`: Your AWS secret key

### 3. Deploy to Amplify

#### Option A: Using Amplify Console (Recommended)

1. Connect your repository to Amplify Console
2. Amplify will automatically detect the `amplify.yml` configuration
3. The build process will:
   - Deploy the Python backend to AWS Lambda
   - Build and deploy the Vue.js frontend
   - Configure the API URL automatically

#### Option B: Using Amplify CLI

```bash
# Push all changes to AWS
amplify push

# Deploy the application
amplify publish
```

### 4. Build Process Details

The `amplify.yml` file defines the build process:

#### Backend Phase
1. **preBuild**: Sets up the build script
2. **build**: Runs `build-backend.sh` which:
   - Creates Python virtual environment
   - Installs dependencies
   - Deploys to AWS Lambda using Serverless Framework
   - Extracts API Gateway URL
   - Creates `.env` file for frontend
3. **postBuild**: Deploys Amplify backend resources

#### Frontend Phase
1. **preBuild**: Installs Node.js dependencies
2. **build**: Builds the Vue.js application
3. **postBuild**: Finalizes the build

## 🔧 Configuration Files

### amplify.yml
Main build configuration for Amplify.

### build-backend.sh
Script that handles Python backend deployment.

### backend/serverless.yml
Serverless Framework configuration for Lambda deployment.

## 🌍 Environment Variables

The build process automatically sets:
- `VITE_API_URL`: API Gateway URL (set during backend deployment)
- `STAGE`: Deployment stage (based on branch name)

## 📊 Monitoring

### Backend Monitoring
- **CloudWatch Logs**: Lambda function logs
- **API Gateway**: Request/response monitoring
- **X-Ray**: Distributed tracing (if enabled)

### Frontend Monitoring
- **Amplify Console**: Build status and performance
- **CloudWatch**: Application logs

## 🔄 CI/CD Pipeline

Amplify automatically creates a CI/CD pipeline that:

1. **Triggers** on code push to connected branch
2. **Builds** backend and frontend
3. **Deploys** to staging/production based on branch
4. **Tests** the deployment
5. **Notifies** on success/failure

## 🛠️ Customization

### Adding New API Endpoints

1. Update `backend/main.py` with new endpoints
2. Update `backend/serverless.yml` if needed
3. Push changes - Amplify will redeploy automatically

### Environment-Specific Configuration

```bash
# Development
amplify env add dev

# Production  
amplify env add prod

# Switch environments
amplify env checkout prod
```

### Custom Build Commands

Modify `amplify.yml` to add custom build steps:

```yaml
backend:
  phases:
    build:
      commands:
        - ./build-backend.sh
        - echo "Custom build step"
        - npm run test
```

## 🚨 Troubleshooting

### Common Issues

1. **Python Dependencies**: Ensure all dependencies are in `requirements.txt`
2. **Serverless Framework**: Check `serverless.yml` configuration
3. **Environment Variables**: Verify all required variables are set in Amplify Console
4. **Build Timeout**: Increase build timeout in Amplify Console if needed

### Debug Commands

```bash
# Check Amplify status
amplify status

# View backend logs
amplify console

# Manual backend deployment
cd backend && serverless deploy --verbose

# Check frontend build
npm run build
```

## 📈 Scaling

### Backend Scaling
- **Lambda**: Automatically scales based on request volume
- **API Gateway**: Handles concurrent requests
- **CloudWatch**: Monitor performance metrics

### Frontend Scaling
- **Amplify Hosting**: Global CDN distribution
- **CloudFront**: Additional caching if needed

## 🔒 Security

### Backend Security
- **IAM Roles**: Least privilege access
- **API Gateway**: Request validation
- **Lambda**: Execution role restrictions

### Frontend Security
- **HTTPS**: Automatic SSL certificates
- **CORS**: Configured for API access
- **Environment Variables**: Secure storage in Amplify

## 💰 Cost Optimization

### Backend Costs
- **Lambda**: Pay per request
- **API Gateway**: Pay per API call
- **CloudWatch**: Basic monitoring included

### Frontend Costs
- **Amplify Hosting**: Free tier available
- **Bandwidth**: Pay for data transfer

## 📚 Additional Resources

- [Amplify Documentation](https://docs.amplify.aws/)
- [Serverless Framework Docs](https://www.serverless.com/framework/docs/)
- [AWS Lambda Documentation](https://docs.aws.amazon.com/lambda/)
- [Vue.js Deployment Guide](https://vuejs.org/guide/best-practices/production-deployment.html)