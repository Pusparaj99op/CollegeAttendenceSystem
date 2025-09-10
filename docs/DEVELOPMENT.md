# Atomic College Attendance System - Development Guide

## 📚 Table of Contents

1. [Project Overview](#project-overview)
2. [Development Environment Setup](#development-environment-setup)
3. [Project Structure](#project-structure)
4. [Development Workflow](#development-workflow)
5. [Coding Standards](#coding-standards)
6. [Testing Guidelines](#testing-guidelines)
7. [Database Management](#database-management)
8. [API Development](#api-development)
9. [Frontend Development](#frontend-development)
10. [Security Guidelines](#security-guidelines)
11. [Deployment](#deployment)
12. [Troubleshooting](#troubleshooting)

## 🎯 Project Overview

The Atomic College Attendance System is a comprehensive, secure attendance management solution that eliminates all forms of proxy attendance through multi-layered verification systems.

### Key Features
- **Faculty-initiated Sessions**: Only professors can start attendance sessions
- **Multi-factor Authentication**: Biometric + QR code + geolocation verification
- **Blockchain Integration**: Tamper-proof attendance records
- **Real-time Monitoring**: Live session tracking and fraud detection
- **Comprehensive Reporting**: Advanced analytics and compliance reports

## 🛠️ Development Environment Setup

### Prerequisites

Ensure you have the following installed:

```bash
# Required Software
Node.js (v18+)        # JavaScript runtime
MongoDB (v6.0+)       # Primary database
Redis (v7+)           # Caching and sessions
Docker (v24+)         # Containerization
Git (v2.30+)          # Version control

# Optional but Recommended
VS Code               # IDE with extensions
Postman/Thunder       # API testing
MongoDB Compass       # Database GUI
```

### Step 1: Clone Repository

```bash
git clone https://github.com/your-org/atomic-attendance-system.git
cd atomic-attendance-system
```

### Step 2: Environment Configuration

```bash
# Copy environment templates
cp .env.example .env
cp backend/.env.example backend/.env
cp frontend/.env.example frontend/.env

# Edit environment variables
nano .env  # Update with your local configuration
```

### Step 3: Install Dependencies

```bash
# Install backend dependencies
cd backend
npm install

# Install frontend dependencies
cd ../frontend
npm install

# Return to root directory
cd ..
```

### Step 4: Database Setup

```bash
# Start MongoDB and Redis (if running locally)
sudo systemctl start mongod
sudo systemctl start redis

# Or using Docker
docker-compose up -d mongodb redis

# Run database migrations
cd backend
npm run migrate

# Seed initial data
npm run seed
```

### Step 5: Start Development Servers

```bash
# Terminal 1: Backend API server
cd backend
npm run dev

# Terminal 2: Frontend development server
cd frontend
npm start

# Terminal 3: Background services (optional)
docker-compose up -d biometric-service qr-service
```

## 📁 Project Structure

```
atomic-attendance-system/
├── backend/                    # Node.js API server
│   ├── src/
│   │   ├── controllers/       # Route handlers
│   │   ├── models/           # Database models
│   │   ├── routes/           # API routes
│   │   ├── middleware/       # Custom middleware
│   │   ├── services/         # Business logic
│   │   ├── utils/            # Utility functions
│   │   ├── config/           # Configuration files
│   │   └── server.js         # Entry point
│   ├── tests/                # Backend tests
│   ├── uploads/              # File uploads
│   ├── logs/                 # Application logs
│   └── package.json          # Dependencies and scripts
│
├── frontend/                  # React application
│   ├── public/               # Static assets
│   ├── src/
│   │   ├── components/       # Reusable UI components
│   │   ├── pages/           # Page components
│   │   ├── hooks/           # Custom React hooks
│   │   ├── services/        # API services
│   │   ├── utils/           # Utility functions
│   │   ├── contexts/        # React contexts
│   │   ├── types/           # TypeScript types
│   │   └── App.tsx          # Main component
│   └── package.json         # Dependencies and scripts
│
├── mobile/                   # React Native app (optional)
├── services/                 # Microservices
│   ├── biometric/           # Biometric verification
│   ├── qr-code/            # QR code generation
│   └── blockchain/          # Blockchain integration
│
├── docs/                     # Documentation
├── tests/                    # Integration tests
├── scripts/                  # Utility scripts
├── monitoring/               # Monitoring configuration
├── nginx/                    # Reverse proxy config
├── docker-compose.yml        # Docker services
├── .gitignore               # Git ignore patterns
├── README.md                # Project overview
└── DEVELOPMENT.md           # This file
```

## 🔄 Development Workflow

### Branch Strategy

```bash
main                    # Production-ready code
├── develop            # Development integration
├── feature/*          # New features
├── bugfix/*           # Bug fixes
├── hotfix/*           # Critical production fixes
└── release/*          # Release preparation
```

### Feature Development Process

1. **Create Feature Branch**
```bash
git checkout develop
git pull origin develop
git checkout -b feature/attendance-qr-enhancement
```

2. **Development Cycle**
```bash
# Make changes
# Write tests
npm run test

# Lint and format code
npm run lint:fix
npm run format

# Commit changes
git add .
git commit -m "feat: add dynamic QR code rotation"
```

3. **Submit Pull Request**
```bash
git push origin feature/attendance-qr-enhancement
# Create PR via GitHub/GitLab
```

### Commit Message Convention

```bash
# Format: type(scope): description

feat(attendance): add biometric liveness detection
fix(api): resolve session timeout issue  
docs(readme): update installation instructions
test(auth): add unit tests for JWT validation
refactor(ui): restructure attendance components
style(frontend): fix ESLint warnings
perf(db): optimize attendance query performance
chore(deps): update React to v18.2.0
```

## 📋 Coding Standards

### Backend (Node.js/Express)

```javascript
// File Structure
const express = require('express');
const { validationResult } = require('express-validator');

const AttendanceService = require('../services/AttendanceService');
const { logger } = require('../utils/logger');

/**
 * Controller for attendance-related operations
 */
class AttendanceController {
  /**
   * Start a new attendance session
   * @param {Request} req - Express request object
   * @param {Response} res - Express response object
   */
  async startSession(req, res) {
    try {
      // Validate request
      const errors = validationResult(req);
      if (!errors.isEmpty()) {
        return res.status(400).json({
          success: false,
          message: 'Validation error',
          errors: errors.array(),
        });
      }

      const { classId, classroomId, duration } = req.body;
      const facultyId = req.user.id;

      const session = await AttendanceService.startSession({
        classId,
        classroomId,
        facultyId,
        duration,
      });

      logger.info('Attendance session started', {
        sessionId: session.id,
        facultyId,
        classId,
      });

      return res.status(201).json({
        success: true,
        message: 'Attendance session started successfully',
        data: session,
      });

    } catch (error) {
      logger.error('Error starting attendance session', {
        error: error.message,
        stack: error.stack,
        facultyId: req.user?.id,
      });

      return res.status(500).json({
        success: false,
        message: 'Internal server error',
      });
    }
  }
}

module.exports = AttendanceController;
```

### Frontend (React/TypeScript)

```typescript
// File Structure
import React, { useState, useEffect, useCallback } from 'react';
import { Alert, Button, CircularProgress } from '@mui/material';

import { useAttendance } from '@/hooks/useAttendance';
import { AttendanceSession } from '@/types/attendance';
import { formatTime } from '@/utils/dateUtils';

interface AttendanceSessionProps {
  classId: string;
  onSessionStart?: (session: AttendanceSession) => void;
}

/**
 * Component for managing attendance sessions
 */
export const AttendanceSessionComponent: React.FC<AttendanceSessionProps> = ({
  classId,
  onSessionStart,
}) => {
  const [isStarting, setIsStarting] = useState(false);
  const [error, setError] = useState<string | null>(null);
  
  const {
    currentSession,
    startSession,
    endSession,
    loading,
    error: attendanceError,
  } = useAttendance();

  // Handle session start
  const handleStartSession = useCallback(async () => {
    try {
      setIsStarting(true);
      setError(null);
      
      const session = await startSession({
        classId,
        duration: 60, // 60 minutes default
      });
      
      onSessionStart?.(session);
    } catch (err) {
      setError('Failed to start attendance session');
      console.error('Session start error:', err);
    } finally {
      setIsStarting(false);
    }
  }, [classId, startSession, onSessionStart]);

  // Effect for error handling
  useEffect(() => {
    if (attendanceError) {
      setError(attendanceError);
    }
  }, [attendanceError]);

  return (
    <div className="attendance-session">
      {error && (
        <Alert 
          severity="error" 
          onClose={() => setError(null)}
          sx={{ mb: 2 }}
        >
          {error}
        </Alert>
      )}

      {currentSession ? (
        <div className="session-active">
          <h3>Active Session</h3>
          <p>Started: {formatTime(currentSession.startTime)}</p>
          <p>Status: {currentSession.status}</p>
          
          <Button
            color="error"
            disabled={loading}
            variant="contained"
            onClick={() => endSession(currentSession.id)}
          >
            End Session
          </Button>
        </div>
      ) : (
        <Button
          color="primary"
          disabled={isStarting || loading}
          startIcon={isStarting && <CircularProgress size={20} />}
          variant="contained"
          onClick={handleStartSession}
        >
          {isStarting ? 'Starting Session...' : 'Start Attendance'}
        </Button>
      )}
    </div>
  );
};

export default AttendanceSessionComponent;
```

## 🧪 Testing Guidelines

### Backend Testing

```javascript
// tests/integration/attendance.test.js
const request = require('supertest');
const app = require('../../src/app');
const { setupTestDB, cleanupTestDB } = require('../helpers/database');

describe('Attendance API', () => {
  beforeAll(async () => {
    await setupTestDB();
  });

  afterAll(async () => {
    await cleanupTestDB();
  });

  describe('POST /api/v1/attendance/session/start', () => {
    it('should start attendance session successfully', async () => {
      const facultyToken = 'valid-jwt-token';
      const sessionData = {
        classId: '507f1f77bcf86cd799439011',
        classroomId: '507f1f77bcf86cd799439012',
        duration: 60,
      };

      const response = await request(app)
        .post('/api/v1/attendance/session/start')
        .set('Authorization', `Bearer ${facultyToken}`)
        .send(sessionData)
        .expect(201);

      expect(response.body.success).toBe(true);
      expect(response.body.data).toHaveProperty('id');
      expect(response.body.data.status).toBe('active');
    });

    it('should return 400 for invalid data', async () => {
      const facultyToken = 'valid-jwt-token';
      const invalidData = {
        classId: 'invalid-id',
      };

      const response = await request(app)
        .post('/api/v1/attendance/session/start')
        .set('Authorization', `Bearer ${facultyToken}`)
        .send(invalidData)
        .expect(400);

      expect(response.body.success).toBe(false);
      expect(response.body.errors).toBeDefined();
    });
  });
});
```

### Frontend Testing

```typescript
// src/components/__tests__/AttendanceSession.test.tsx
import React from 'react';
import { render, screen, fireEvent, waitFor } from '@testing-library/react';
import { QueryClient, QueryClientProvider } from 'react-query';

import AttendanceSessionComponent from '../AttendanceSession';
import { useAttendance } from '@/hooks/useAttendance';

// Mock the useAttendance hook
jest.mock('@/hooks/useAttendance');
const mockUseAttendance = useAttendance as jest.MockedFunction<typeof useAttendance>;

const createTestQueryClient = () => new QueryClient({
  defaultOptions: {
    queries: { retry: false },
    mutations: { retry: false },
  },
});

const renderWithQueryClient = (component: React.ReactElement) => {
  const queryClient = createTestQueryClient();
  return render(
    <QueryClientProvider client={queryClient}>
      {component}
    </QueryClientProvider>
  );
};

describe('AttendanceSessionComponent', () => {
  beforeEach(() => {
    mockUseAttendance.mockReturnValue({
      currentSession: null,
      startSession: jest.fn(),
      endSession: jest.fn(),
      loading: false,
      error: null,
    });
  });

  it('renders start session button when no active session', () => {
    renderWithQueryClient(
      <AttendanceSessionComponent classId="test-class-id" />
    );

    expect(screen.getByText('Start Attendance')).toBeInTheDocument();
  });

  it('calls startSession when start button clicked', async () => {
    const mockStartSession = jest.fn();
    mockUseAttendance.mockReturnValue({
      currentSession: null,
      startSession: mockStartSession,
      endSession: jest.fn(),
      loading: false,
      error: null,
    });

    renderWithQueryClient(
      <AttendanceSessionComponent classId="test-class-id" />
    );

    fireEvent.click(screen.getByText('Start Attendance'));

    await waitFor(() => {
      expect(mockStartSession).toHaveBeenCalledWith({
        classId: 'test-class-id',
        duration: 60,
      });
    });
  });

  it('displays error message when error occurs', () => {
    mockUseAttendance.mockReturnValue({
      currentSession: null,
      startSession: jest.fn(),
      endSession: jest.fn(),
      loading: false,
      error: 'Network error',
    });

    renderWithQueryClient(
      <AttendanceSessionComponent classId="test-class-id" />
    );

    expect(screen.getByText('Network error')).toBeInTheDocument();
  });
});
```

### Running Tests

```bash
# Backend tests
cd backend
npm run test                    # Run all tests
npm run test:watch             # Run tests in watch mode
npm run test:coverage          # Generate coverage report
npm run test:integration       # Run integration tests only

# Frontend tests
cd frontend
npm test                       # Run tests in watch mode
npm run test:ci               # Run tests once (CI mode)
npm run test:coverage         # Generate coverage report
```

## 🗄️ Database Management

### MongoDB Operations

```bash
# Connect to MongoDB
mongo "mongodb://localhost:27017/atomic_attendance"

# Common queries
db.attendance_sessions.find({"status": "active"})
db.students.countDocuments({"department": "Computer Science"})
db.attendance_records.aggregate([
  {$group: {_id: "$studentId", totalPresent: {$sum: 1}}}
])

# Backup database
mongodump --db atomic_attendance --out ./backups/$(date +%Y%m%d)

# Restore database
mongorestore --db atomic_attendance ./backups/20231201/atomic_attendance
```

### Database Migrations

```javascript
// migrations/001_create_indexes.js
module.exports = {
  async up(db) {
    // Create indexes for performance
    await db.collection('users').createIndex({ email: 1 }, { unique: true });
    await db.collection('students').createIndex({ rollNumber: 1 }, { unique: true });
    await db.collection('attendance_sessions').createIndex({ 
      classId: 1, 
      startTime: -1 
    });
  },

  async down(db) {
    // Rollback indexes
    await db.collection('users').dropIndex({ email: 1 });
    await db.collection('students').dropIndex({ rollNumber: 1 });
    await db.collection('attendance_sessions').dropIndex({ 
      classId: 1, 
      startTime: -1 
    });
  }
};
```

## 🔒 Security Guidelines

### Authentication Implementation

```javascript
// middleware/auth.js
const jwt = require('jsonwebtoken');
const rateLimit = require('express-rate-limit');

// Rate limiting for auth endpoints
const authLimiter = rateLimit({
  windowMs: 15 * 60 * 1000, // 15 minutes
  max: 5, // 5 attempts per window
  message: 'Too many login attempts, please try again later',
  standardHeaders: true,
  legacyHeaders: false,
});

// JWT verification middleware
const authenticateToken = (req, res, next) => {
  const authHeader = req.headers['authorization'];
  const token = authHeader && authHeader.split(' ')[1];

  if (!token) {
    return res.status(401).json({
      success: false,
      message: 'Access token required',
    });
  }

  jwt.verify(token, process.env.JWT_SECRET, (err, user) => {
    if (err) {
      return res.status(403).json({
        success: false,
        message: 'Invalid or expired token',
      });
    }
    req.user = user;
    next();
  });
};

module.exports = { authLimiter, authenticateToken };
```

### Input Validation

```javascript
// validation/attendance.js
const { body, param, query } = require('express-validator');

const startSessionValidation = [
  body('classId')
    .isMongoId()
    .withMessage('Invalid class ID format'),
  body('classroomId')
    .isMongoId()
    .withMessage('Invalid classroom ID format'),
  body('duration')
    .isInt({ min: 15, max: 300 })
    .withMessage('Duration must be between 15 and 300 minutes'),
  body('location.latitude')
    .isFloat({ min: -90, max: 90 })
    .withMessage('Invalid latitude'),
  body('location.longitude')
    .isFloat({ min: -180, max: 180 })
    .withMessage('Invalid longitude'),
];

module.exports = { startSessionValidation };
```

## 🚀 Deployment

### Production Environment Variables

```bash
# .env.production
NODE_ENV=production
PORT=5000

# Database
MONGODB_URI=mongodb://user:pass@mongo-cluster/atomic_attendance
REDIS_URL=redis://user:pass@redis-cluster:6379

# Security
JWT_SECRET=your-super-secure-production-jwt-secret-256-bit-key
CRYPTO_SECRET_KEY=your-encryption-key-for-sensitive-data

# External Services
BIOMETRIC_API_URL=https://biometric-service.internal
BLOCKCHAIN_NETWORK_URL=https://blockchain-node.internal

# Monitoring
SENTRY_DSN=https://your-sentry-dsn
NEW_RELIC_LICENSE_KEY=your-new-relic-key
```

### Docker Production Build

```dockerfile
# backend/Dockerfile
FROM node:18-alpine

WORKDIR /app

# Install dependencies
COPY package*.json ./
RUN npm ci --only=production

# Copy source code
COPY . .

# Create non-root user
RUN addgroup -g 1001 -S nodejs
RUN adduser -S nodeuser -u 1001

# Change ownership
RUN chown -R nodeuser:nodejs /app
USER nodeuser

EXPOSE 5000

CMD ["npm", "start"]
```

### Deployment Scripts

```bash
#!/bin/bash
# scripts/deploy.sh

set -e

echo "🚀 Starting deployment..."

# Build and test
npm run build
npm run test:ci

# Build Docker images
docker build -t attendance-backend:latest ./backend
docker build -t attendance-frontend:latest ./frontend

# Push to registry
docker tag attendance-backend:latest registry.yourorg.com/attendance-backend:latest
docker tag attendance-frontend:latest registry.yourorg.com/attendance-frontend:latest

docker push registry.yourorg.com/attendance-backend:latest
docker push registry.yourorg.com/attendance-frontend:latest

# Deploy to production
kubectl apply -f k8s/production/

echo "✅ Deployment completed successfully!"
```

## 🔧 Troubleshooting

### Common Issues

1. **MongoDB Connection Failed**
```bash
# Check MongoDB status
sudo systemctl status mongod

# Check connection string
mongo "mongodb://localhost:27017/atomic_attendance"

# Check firewall
sudo ufw allow 27017
```

2. **Redis Connection Issues**
```bash
# Test Redis connection
redis-cli ping

# Check Redis configuration
redis-cli config get "*"
```

3. **Node.js Version Conflicts**
```bash
# Use Node Version Manager
nvm install 18
nvm use 18
nvm alias default 18
```

4. **Port Already in Use**
```bash
# Find process using port
lsof -i :5000

# Kill process
kill -9 <PID>
```

### Debug Mode

```bash
# Backend debug mode
DEBUG=attendance:* npm run dev

# Frontend with debug info
REACT_APP_DEBUG=true npm start

# Database query debugging
MONGOOSE_DEBUG=true npm run dev
```

### Performance Monitoring

```bash
# Check application performance
npm run monitor

# Database performance
mongostat --host localhost:27017

# Memory usage
node --max-old-space-size=4096 src/server.js
```

## 📞 Support

- **Documentation**: [Project Wiki](https://github.com/your-org/atomic-attendance-system/wiki)
- **Issues**: [GitHub Issues](https://github.com/your-org/atomic-attendance-system/issues)
- **Discussions**: [GitHub Discussions](https://github.com/your-org/atomic-attendance-system/discussions)
- **Slack**: #attendance-system-dev

---

**Happy Coding! 🎉**