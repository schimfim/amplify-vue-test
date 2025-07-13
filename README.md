# Amplify Vue Template with Python Backend

A full-stack application with a Vue.js frontend and Python FastAPI backend running on AWS Lambda.

## 🏗️ Architecture

- **Frontend**: Vue.js 3 with TypeScript, Vite, and Vue Router
- **Backend**: Python FastAPI with AWS Lambda deployment
- **Infrastructure**: AWS Amplify + Serverless Framework
- **API**: RESTful APIs for About page data

## 🚀 Quick Start

### Prerequisites

- Node.js 18+
- Python 3.11+
- AWS CLI configured
- Serverless Framework

### Frontend Setup

1. Install dependencies:
```bash
npm install
```

2. Start development server:
```bash
npm run dev
```

3. Build for production:
```bash
npm run build
```

### Backend Setup

1. Navigate to backend directory:
```bash
cd backend
```

2. Install dependencies:
```bash
npm install
pip install -r requirements.txt
```

3. Start local development:
```bash
npm run dev
```

4. Test the API:
```bash
python test_api.py
```

### Deployment

#### Backend Deployment

1. Deploy to AWS Lambda:
```bash
cd backend
./deploy.sh
```

2. Or manually:
```bash
serverless deploy
```

#### Frontend Deployment

1. Deploy with Amplify:
```bash
amplify push
```

## 📁 Project Structure

```
├── src/                    # Vue.js frontend
│   ├── components/        # Vue components
│   │   ├── About.vue     # About page (now fetches from API)
│   │   └── Todos.vue     # Todo component
│   ├── App.vue           # Main app component
│   └── main.ts           # App entry point
├── backend/               # Python FastAPI backend
│   ├── main.py           # FastAPI application
│   ├── config.py         # Configuration
│   ├── requirements.txt  # Python dependencies
│   ├── serverless.yml    # AWS Lambda configuration
│   ├── tests/            # Unit tests
│   └── deploy.sh         # Deployment script
├── amplify/              # AWS Amplify configuration
└── package.json          # Frontend dependencies
```

## 🔌 API Endpoints

The backend provides the following REST API endpoints:

- `GET /` - Root endpoint
- `GET /health` - Health check
- `GET /api/about` - Get complete about data (name and email)
- `GET /api/about/name` - Get just the name

### Example API Response

```json
{
  "name": "John Doe",
  "email": "john.doe@example.com"
}
```

## 🔧 Configuration

### Environment Variables

Set these environment variables for the backend:

- `STAGE` - Deployment stage (dev/prod)
- `ABOUT_NAME` - Name to display on About page
- `ABOUT_EMAIL` - Email to display on About page
- `VITE_API_URL` - API base URL for frontend

### CORS Configuration

Update `backend/config.py` to add your frontend domain to the CORS origins list.

## 🧪 Testing

### Backend Tests

```bash
cd backend
python -m pytest tests/ -v
```

### API Testing

```bash
cd backend
python test_api.py
```

### Frontend Tests

```bash
npm run type-check
```

## 🐳 Docker Development

Run the backend in Docker:

```bash
cd backend
docker-compose up
```

## 📚 Documentation

- [FastAPI Documentation](https://fastapi.tiangolo.com/)
- [Serverless Framework](https://www.serverless.com/)
- [AWS Lambda](https://aws.amazon.com/lambda/)
- [Vue.js 3](https://vuejs.org/)

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Add tests
5. Submit a pull request

## 📄 License

This project is licensed under the MIT License.