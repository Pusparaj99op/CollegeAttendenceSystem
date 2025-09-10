# Create ESLint configuration for backend
backend_eslint_config = {
    "env": {
        "node": True,
        "es2022": True,
        "jest": True
    },
    "extends": [
        "eslint:recommended",
        "node/recommended",
        "prettier"
    ],
    "plugins": [
        "node",
        "security",
        "import"
    ],
    "parserOptions": {
        "ecmaVersion": 2022,
        "sourceType": "module"
    },
    "rules": {
        # Code Quality
        "no-console": "warn",
        "no-debugger": "error",
        "no-unused-vars": ["error", { "argsIgnorePattern": "^_" }],
        "prefer-const": "error",
        "no-var": "error",
        
        # Security Rules
        "security/detect-buffer-noassert": "error",
        "security/detect-child-process": "warn",
        "security/detect-disable-mustache-escape": "error",
        "security/detect-eval-with-expression": "error",
        "security/detect-no-csrf-before-method-override": "error",
        "security/detect-non-literal-fs-filename": "warn",
        "security/detect-non-literal-regexp": "error",
        "security/detect-pseudoRandomBytes": "error",
        "security/detect-unsafe-regex": "error",
        
        # Node.js Specific
        "node/no-unsupported-features/es-syntax": "off",
        "node/no-missing-import": "error",
        "node/no-unpublished-require": "off",
        "node/exports-style": ["error", "module.exports"],
        "node/file-extension-in-import": ["error", "always"],
        "node/prefer-global/buffer": ["error", "always"],
        "node/prefer-global/console": ["error", "always"],
        "node/prefer-global/process": ["error", "always"],
        "node/prefer-global/url-search-params": ["error", "always"],
        "node/prefer-global/url": ["error", "always"],
        "node/prefer-promises/dns": "error",
        "node/prefer-promises/fs": "error",
        
        # Import Rules
        "import/order": ["error", {
            "groups": ["builtin", "external", "internal", "parent", "sibling", "index"],
            "newlines-between": "always"
        }],
        "import/newline-after-import": "error",
        "import/no-duplicate-imports": "error",
        
        # General Best Practices
        "eqeqeq": ["error", "always"],
        "curly": ["error", "all"],
        "brace-style": ["error", "1tbs"],
        "comma-dangle": ["error", "always-multiline"],
        "indent": ["error", 2],
        "quotes": ["error", "single"],
        "semi": ["error", "always"],
        "space-before-function-paren": ["error", {
            "anonymous": "always",
            "named": "never",
            "asyncArrow": "always"
        }],
        "object-curly-spacing": ["error", "always"],
        "array-bracket-spacing": ["error", "never"],
        "key-spacing": ["error", { "beforeColon": False, "afterColon": True }],
        "comma-spacing": ["error", { "before": False, "after": True }],
        "no-trailing-spaces": "error",
        "eol-last": "error",
        
        # Error Handling
        "no-throw-literal": "error",
        "prefer-promise-reject-errors": "error",
        
        # Performance
        "no-loop-func": "error",
        "no-await-in-loop": "warn"
    },
    "overrides": [
        {
            "files": ["**/*.test.js", "**/*.spec.js"],
            "env": {
                "jest": True
            },
            "rules": {
                "no-console": "off",
                "security/detect-non-literal-fs-filename": "off"
            }
        }
    ]
}

# Save backend ESLint config
with open('backend-eslintrc.json', 'w') as f:
    json.dump(backend_eslint_config, f, indent=2)

print("Backend ESLint configuration created successfully!")