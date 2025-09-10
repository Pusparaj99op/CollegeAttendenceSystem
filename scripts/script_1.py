# Create package.json for frontend
frontend_package_json = {
    "name": "atomic-attendance-frontend",
    "version": "1.0.0",
    "description": "Frontend application for Atomic College Attendance System",
    "private": True,
    "main": "src/index.js",
    "homepage": ".",
    "scripts": {
        "start": "react-scripts start",
        "build": "react-scripts build",
        "test": "react-scripts test",
        "eject": "react-scripts eject",
        "test:coverage": "react-scripts test --coverage --watchAll=false",
        "test:ci": "react-scripts test --coverage --watchAll=false --ci",
        "lint": "eslint src/ --ext .js,.jsx,.ts,.tsx",
        "lint:fix": "eslint src/ --ext .js,.jsx,.ts,.tsx --fix",
        "format": "prettier --write \"src/**/*.{js,jsx,ts,tsx,json,css,md}\"",
        "analyze": "npm run build && npx source-map-explorer 'build/static/js/*.js'",
        "storybook": "storybook dev -p 6006",
        "build-storybook": "storybook build",
        "serve": "serve -s build -l 3000",
        "docker:build": "docker build -t atomic-attendance-frontend .",
        "docker:run": "docker run -p 3000:3000 atomic-attendance-frontend"
    },
    "dependencies": {
        "react": "^18.2.0",
        "react-dom": "^18.2.0",
        "react-router-dom": "^6.15.0",
        "react-scripts": "5.0.1",
        "react-query": "^3.39.3",
        "axios": "^1.5.0",
        "@mui/material": "^5.14.10",
        "@mui/icons-material": "^5.14.9",
        "@emotion/react": "^11.11.1",
        "@emotion/styled": "^11.11.0",
        "@mui/x-data-grid": "^6.12.1",
        "react-hook-form": "^7.46.1",
        "react-hot-toast": "^2.4.1",
        "recharts": "^2.8.0",
        "date-fns": "^2.30.0",
        "qrcode.react": "^3.1.0",
        "socket.io-client": "^4.7.2",
        "react-webcam": "^7.1.1",
        "react-qr-scanner": "^1.0.0-alpha.11",
        "framer-motion": "^10.16.4",
        "react-helmet-async": "^1.3.0",
        "web-vitals": "^3.4.0"
    },
    "devDependencies": {
        "@testing-library/jest-dom": "^6.1.3",
        "@testing-library/react": "^13.4.0",
        "@testing-library/user-event": "^14.4.3",
        "@types/react": "^18.2.22",
        "@types/react-dom": "^18.2.7",
        "typescript": "^5.2.2",
        "eslint": "^8.49.0",
        "eslint-config-react-app": "^7.0.1",
        "prettier": "^3.0.3",
        "@storybook/addon-essentials": "^7.4.2",
        "@storybook/addon-interactions": "^7.4.2",
        "@storybook/addon-links": "^7.4.2",
        "@storybook/addon-onboarding": "^1.0.8",
        "@storybook/blocks": "^7.4.2",
        "@storybook/react": "^7.4.2",
        "@storybook/react-vite": "^7.4.2",
        "@storybook/testing-library": "^0.2.1",
        "source-map-explorer": "^2.5.3",
        "serve": "^14.2.1"
    },
    "engines": {
        "node": ">=18.0.0",
        "npm": ">=8.0.0"
    },
    "browserslist": {
        "production": [
            ">0.2%",
            "not dead",
            "not op_mini all"
        ],
        "development": [
            "last 1 chrome version",
            "last 1 firefox version",
            "last 1 safari version"
        ]
    },
    "proxy": "http://localhost:5000",
    "jest": {
        "collectCoverageFrom": [
            "src/**/*.{js,jsx,ts,tsx}",
            "!src/index.js",
            "!src/reportWebVitals.js",
            "!src/**/*.stories.{js,jsx,ts,tsx}",
            "!src/**/*.test.{js,jsx,ts,tsx}"
        ],
        "coverageReporters": [
            "json",
            "lcov",
            "text",
            "html"
        ],
        "coverageThreshold": {
            "global": {
                "branches": 80,
                "functions": 80,
                "lines": 80,
                "statements": 80
            }
        }
    }
}

# Save frontend package.json
with open('frontend-package.json', 'w') as f:
    json.dump(frontend_package_json, f, indent=2)

print("Frontend package.json created successfully!")