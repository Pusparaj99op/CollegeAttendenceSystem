# Atomic College Attendance System

![License](https://img.shields.io/badge/license-MIT-blue.svg)
![Version](https://img.shields.io/badge/version-1.0.0-green.svg)
![Status](https://img.shields.io/badge/status-Development-orange.svg)

## 📋 Project Overview

The Atomic College Attendance System is a comprehensive, loophole-proof attendance management solution designed for educational institutions. The system ensures 100% accuracy through multi-layered authentication and eliminates all forms of proxy attendance.

### 🎯 Key Features

- **Faculty-Controlled Sessions**: Professors must initiate attendance sessions
- **Multi-Factor Authentication**: Biometric + QR code + location verification
- **Real-time Validation**: Instant verification and fraud detection
- **Atomic Operations**: Session-based control with automatic locking
- **Anti-Proxy Mechanisms**: Advanced security to prevent fake attendance
- **Blockchain Integration**: Tamper-proof attendance records

## 🏗️ Architecture

```
┌─────────────────┐    ┌──────────────────┐    ┌─────────────────┐
│   Frontend      │────│   API Gateway    │────│   Backend       │
│   (React/Vue)   │    │   (Express.js)   │    │   (Node.js)     │
└─────────────────┘    └──────────────────┘    └─────────────────┘
                                │
                    ┌───────────────────────┐
                    │   Database Layer      │
                    │   (MongoDB/MySQL)     │
                    └───────────────────────┘
                                │
                    ┌───────────────────────┐
                    │   Blockchain Layer    │
                    │   (Hyperledger)       │
                    └───────────────────────┘
```

## 🚀 Quick Start

### Prerequisites

- Node.js (v18+)
- MongoDB/MySQL
- React/Vue.js
- Git

### Installation

1. **Clone the repository**
```bash
git clone https://github.com/your-org/atomic-attendance-system.git
cd atomic-attendance-system
```

2. **Install dependencies**
```bash
# Backend dependencies
cd backend
npm install

# Frontend dependencies
cd ../frontend
npm install
```

3. **Environment Configuration**
```bash
cp .env.example .env
# Update .env with your configuration
```

4. **Database Setup**
```bash
# Run database migrations
npm run migrate

# Seed initial data
npm run seed
```

5. **Start Development Servers**
```bash
# Backend (Terminal 1)
cd backend && npm run dev

# Frontend (Terminal 2)
cd frontend && npm start
```

## 🛠️ Available Scripts

### Backend Scripts
```bash
cd backend
npm run dev          # Start development server with nodemon
npm start           # Start production server
npm test            # Run tests with Jest
npm run test:watch  # Run tests in watch mode
npm run lint        # Lint code with ESLint
npm run format      # Format code with Prettier
```

### Frontend Scripts
```bash
cd frontend
npm start           # Start development server
npm run build       # Build for production
npm test            # Run tests
npm run lint        # Lint code with ESLint
npm run format      # Format code with Prettier
```

### Docker Commands
```bash
# Build and start all services
docker-compose up -d

# Build specific services
docker-compose build backend frontend

# View logs
docker-compose logs -f backend
```

## 📂 Project Structure

```
atomic-attendance-system/
├── 📁 backend/                    # Node.js Backend API
│   ├── 📁 src/
│   │   ├── 📁 config/            # Database & app configuration
│   │   ├── 📁 controllers/       # Route controllers
│   │   ├── 📁 middleware/        # Authentication & validation
│   │   ├── 📁 models/            # Database models (Mongoose)
│   │   ├── 📁 routes/            # API endpoints
│   │   ├── 📁 services/          # Business logic services
│   │   ├── 📁 utils/             # Helper utilities
│   │   └── 📄 server.js          # Main server file
│   ├── 📁 tests/                 # Backend test files
│   ├── 📄 package.json           # Backend dependencies
│   ├── 📄 .eslintrc.json         # Backend ESLint config
│   └── 📄 jest.config.json       # Test configuration
├── 📁 frontend/                   # React Frontend Application
│   ├── 📁 public/               # Static public files
│   ├── 📁 src/
│   │   ├── 📁 components/       # Reusable UI components
│   │   ├── 📁 pages/            # Page components
│   │   ├── 📁 services/         # API services
│   │   ├── 📁 utils/            # Utility functions
│   │   ├── 📁 hooks/            # Custom React hooks
│   │   ├── 📁 context/          # React context providers
│   │   └── 📁 assets/           # Images, fonts, etc.
│   ├── 📄 package.json          # Frontend dependencies
│   ├── 📄 .eslintrc.json        # Frontend ESLint config
│   └── 📄 .env.example          # Frontend environment template
├── 📁 docs/                      # Documentation
│   ├── 📄 api-docs.yaml         # OpenAPI/Swagger API documentation
│   ├── 📄 database-schema.md    # Database schema documentation
│   └── 📄 DEVELOPMENT.md        # Development guide
├── 📁 scripts/                   # Utility scripts
│   ├── 📄 script.py             # Main setup script
│   ├── 📄 script_1.py           # Frontend package script
│   ├── 📄 script_2.py           # Backend ESLint script
│   ├── 📄 script_3.py           # Frontend ESLint script
│   └── 📄 script_4.py           # Prettier & Jest script
├── 📁 tests/                     # Integration & E2E tests
├── 📁 config/                    # Global configuration files
├── 📄 docker-compose.yml         # Docker services configuration
├── 📄 .prettierrc.json          # Code formatting rules
├── 📄 .gitignore                # Git ignore patterns
├── 📄 .env.example              # Environment variables template
├── 📄 workspace.code-workspace   # VS Code workspace config
├── 📄 README.md                 # Project documentation
└── 📄 LICENSE                   # Project license
```
└── deployment/               # Deployment configurations
```

## 🔧 Development Workflow

### 1. Feature Development
- Create feature branch: `git checkout -b feature/your-feature-name`
- Follow naming conventions in `docs/CODING_STANDARDS.md`
- Write tests for new functionality
- Update documentation

### 2. Testing
```bash
# Run unit tests
npm run test

# Run integration tests
npm run test:integration

# Run end-to-end tests
npm run test:e2e

# Generate coverage report
npm run test:coverage
```

### 3. Code Quality
```bash
# Lint code
npm run lint

# Format code
npm run format

# Type checking (if TypeScript)
npm run type-check
```

## 📚 API Documentation

### Authentication Endpoints
- `POST /api/auth/faculty-login` - Faculty authentication
- `POST /api/auth/student-verify` - Student verification

### Attendance Endpoints
- `POST /api/attendance/session/start` - Start attendance session
- `POST /api/attendance/session/end` - End attendance session
- `POST /api/attendance/mark` - Mark student attendance
- `GET /api/attendance/reports` - Generate attendance reports

### System Endpoints
- `GET /api/system/health` - System health check
- `POST /api/system/qr-generate` - Generate dynamic QR codes
- `POST /api/biometric/verify` - Biometric verification

## 🔒 Security Features

### Multi-Layer Authentication
1. **Faculty Layer**: Biometric + Location + Time validation
2. **Student Layer**: QR code + Biometric + Geolocation
3. **System Layer**: Blockchain verification + Audit trails

### Data Protection
- End-to-end encryption
- GDPR compliance
- Role-based access control
- Secure session management

## 🌍 Deployment

### Development Environment
```bash
npm run dev
```

### Production Environment
```bash
# Build applications
npm run build

# Start production servers
npm run start:prod
```

### Docker Deployment
```bash
# Build containers
docker-compose build

# Start services
docker-compose up -d
```

## 🧪 Testing Strategy

### Test Coverage Requirements
- Unit Tests: >90%
- Integration Tests: >85%
- E2E Tests: Critical user flows

### Testing Framework
- **Unit**: Jest + Testing Library
- **Integration**: Supertest
- **E2E**: Playwright/Cypress

## 📊 Monitoring & Analytics

### Performance Metrics
- Response time monitoring
- Error rate tracking
- User session analytics
- System resource utilization

### Logging
- Structured logging with Winston
- Log aggregation with ELK stack
- Real-time alerting

## 🤝 Contributing

1. Fork the repository
2. Create feature branch (`git checkout -b feature/amazing-feature`)
3. Commit changes (`git commit -m 'Add amazing feature'`)
4. Push to branch (`git push origin feature/amazing-feature`)
5. Open Pull Request

### Code Review Process
- All PRs require 2 approvals
- Automated tests must pass
- Code coverage must not decrease
- Documentation must be updated

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
