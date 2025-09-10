# Create Prettier configuration
prettier_config = {
    "semi": True,
    "trailingComma": "es5",
    "singleQuote": True,
    "printWidth": 120,
    "tabWidth": 2,
    "useTabs": False,
    "quoteProps": "as-needed",
    "jsxSingleQuote": True,
    "bracketSpacing": True,
    "bracketSameLine": False,
    "arrowParens": "avoid",
    "endOfLine": "lf",
    "embeddedLanguageFormatting": "auto",
    "htmlWhitespaceSensitivity": "css",
    "insertPragma": False,
    "jsxBracketSameLine": False,
    "proseWrap": "preserve",
    "requirePragma": False,
    "vueIndentScriptAndStyle": False,
    "overrides": [
        {
            "files": ["*.json", "*.md"],
            "options": {
                "tabWidth": 2
            }
        },
        {
            "files": "*.yaml",
            "options": {
                "tabWidth": 2,
                "printWidth": 80
            }
        },
        {
            "files": "*.scss",
            "options": {
                "tabWidth": 2,
                "singleQuote": False
            }
        }
    ]
}

# Save Prettier config
with open('prettierrc.json', 'w') as f:
    json.dump(prettier_config, f, indent=2)

print("Prettier configuration created successfully!")

# Create Jest configuration for backend
jest_config = {
    "testEnvironment": "node",
    "setupFilesAfterEnv": ["<rootDir>/tests/setup.js"],
    "testMatch": [
        "**/__tests__/**/*.js",
        "**/?(*.)+(spec|test).js"
    ],
    "testPathIgnorePatterns": [
        "/node_modules/",
        "/dist/",
        "/build/"
    ],
    "collectCoverageFrom": [
        "src/**/*.js",
        "!src/server.js",
        "!src/config/**",
        "!**/node_modules/**"
    ],
    "coverageDirectory": "coverage",
    "coverageReporters": [
        "text",
        "lcov",
        "html"
    ],
    "coverageThreshold": {
        "global": {
            "branches": 80,
            "functions": 80,
            "lines": 80,
            "statements": 80
        }
    },
    "verbose": True,
    "forceExit": True,
    "detectOpenHandles": True,
    "testTimeout": 30000
}

# Save Jest config
with open('jest.config.json', 'w') as f:
    json.dump(jest_config, f, indent=2)

print("Jest configuration created successfully!")

print("\n=== Essential Development Files Created ===")
print("✓ README.md - Main project documentation")
print("✓ backend-package.json - Backend dependencies and scripts")
print("✓ frontend-package.json - Frontend dependencies and scripts")
print("✓ .gitignore - Git ignore patterns")
print("✓ .env.example - Environment configuration template")
print("✓ api-docs.yaml - OpenAPI/Swagger API documentation")
print("✓ database-schema.md - Complete database schema")
print("✓ workspace.code-workspace - VS Code workspace configuration")
print("✓ docker-compose.yml - Docker services configuration")
print("✓ backend-eslintrc.json - Backend ESLint configuration")
print("✓ frontend-eslintrc.json - Frontend ESLint configuration")
print("✓ DEVELOPMENT.md - Comprehensive development guide")
print("✓ prettierrc.json - Code formatting configuration")
print("✓ jest.config.json - Testing configuration")
print("\nAll essential files for VS Code development have been created!")