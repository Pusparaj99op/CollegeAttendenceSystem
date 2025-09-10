#!/bin/bash

# ============================================================================
# ATOMIC COLLEGE ATTENDANCE SYSTEM - SETUP VERIFICATION
# ============================================================================
# This script verifies that the development environment is properly set up
# ============================================================================

echo "🚀 Atomic College Attendance System - Setup Verification"
echo "============================================================================="

# Colors for output
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
BLUE='\033[0;34m'
NC='\033[0m' # No Color

# Function to check if command exists
command_exists() {
    command -v "$1" >/dev/null 2>&1
}

# Function to print status
print_status() {
    if [ $2 -eq 0 ]; then
        echo -e "✅ ${GREEN}$1${NC}"
    else
        echo -e "❌ ${RED}$1${NC}"
    fi
}

# Function to check file exists
check_file() {
    if [ -f "$1" ]; then
        echo -e "✅ ${GREEN}$1 exists${NC}"
    else
        echo -e "❌ ${RED}$1 not found${NC}"
    fi
}

# Function to check directory exists
check_directory() {
    if [ -d "$1" ]; then
        echo -e "✅ ${GREEN}$1/ exists${NC}"
    else
        echo -e "❌ ${RED}$1/ not found${NC}"
    fi
}

echo ""
echo "📋 Checking Prerequisites..."
echo "============================================================================="

# Check Node.js
if command_exists node; then
    NODE_VERSION=$(node --version)
    echo -e "✅ ${GREEN}Node.js: $NODE_VERSION${NC}"
else
    echo -e "❌ ${RED}Node.js not found${NC}"
fi

# Check npm
if command_exists npm; then
    NPM_VERSION=$(npm --version)
    echo -e "✅ ${GREEN}npm: $NPM_VERSION${NC}"
else
    echo -e "❌ ${RED}npm not found${NC}"
fi

# Check MongoDB
if command_exists mongod; then
    echo -e "✅ ${GREEN}MongoDB installed${NC}"
else
    echo -e "⚠️  ${YELLOW}MongoDB not found (optional for development)${NC}"
fi

# Check Docker
if command_exists docker; then
    echo -e "✅ ${GREEN}Docker installed${NC}"
else
    echo -e "⚠️  ${YELLOW}Docker not found (optional)${NC}"
fi

# Check Git
if command_exists git; then
    GIT_VERSION=$(git --version)
    echo -e "✅ ${GREEN}$GIT_VERSION${NC}"
else
    echo -e "❌ ${RED}Git not found${NC}"
fi

echo ""
echo "📁 Checking Project Structure..."
echo "============================================================================="

# Check main directories
check_directory "backend"
check_directory "frontend"
check_directory "docs"
check_directory "scripts"
check_directory "tests"
check_directory "config"

# Check backend structure
check_directory "backend/src"
check_directory "backend/src/controllers"
check_directory "backend/src/models"
check_directory "backend/src/routes"
check_directory "backend/src/middleware"
check_directory "backend/src/services"
check_directory "backend/src/utils"
check_directory "backend/src/config"
check_directory "backend/tests"

# Check frontend structure
check_directory "frontend/src"
check_directory "frontend/src/components"
check_directory "frontend/src/pages"
check_directory "frontend/src/services"
check_directory "frontend/src/utils"
check_directory "frontend/src/hooks"
check_directory "frontend/src/context"
check_directory "frontend/src/assets"
check_directory "frontend/public"

echo ""
echo "📄 Checking Configuration Files..."
echo "============================================================================="

# Check important files
check_file "backend/package.json"
check_file "backend/.eslintrc.json"
check_file "backend/jest.config.json"
check_file "backend/src/server.js"

check_file "frontend/package.json"
check_file "frontend/.eslintrc.json"
check_file "frontend/src/index.js"
check_file "frontend/src/App.js"
check_file "frontend/public/index.html"

check_file ".prettierrc.json"
check_file ".gitignore"
check_file ".env.example"
check_file "frontend/.env.example"
check_file "docker-compose.yml"
check_file "workspace.code-workspace"

check_file "docs/api-docs.yaml"
check_file "docs/database-schema.md"
check_file "docs/DEVELOPMENT.md"

echo ""
echo "📦 Checking Dependencies..."
echo "============================================================================="

# Check if node_modules exist
if [ -d "backend/node_modules" ]; then
    echo -e "✅ ${GREEN}Backend dependencies installed${NC}"
else
    echo -e "⚠️  ${YELLOW}Backend dependencies not installed (run: cd backend && npm install)${NC}"
fi

if [ -d "frontend/node_modules" ]; then
    echo -e "✅ ${GREEN}Frontend dependencies installed${NC}"
else
    echo -e "⚠️  ${YELLOW}Frontend dependencies not installed (run: cd frontend && npm install)${NC}"
fi

echo ""
echo "🔧 Quick Start Commands..."
echo "============================================================================="
echo -e "${BLUE}Backend Development:${NC}"
echo "  cd backend && npm run dev"
echo ""
echo -e "${BLUE}Frontend Development:${NC}"
echo "  cd frontend && npm start"
echo ""
echo -e "${BLUE}Install Dependencies:${NC}"
echo "  cd backend && npm install"
echo "  cd frontend && npm install"
echo ""
echo -e "${BLUE}Docker (Alternative):${NC}"
echo "  docker-compose up -d"

echo ""
echo "📚 Documentation Links..."
echo "============================================================================="
echo "• API Documentation: docs/api-docs.yaml"
echo "• Database Schema: docs/database-schema.md"
echo "• Development Guide: docs/DEVELOPMENT.md"
echo "• VS Code Workspace: workspace.code-workspace"

echo ""
echo -e "${GREEN}✨ Setup verification complete!${NC}"
echo "============================================================================="
