# Create ESLint configuration for frontend (React)
frontend_eslint_config = {
    "env": {
        "browser": True,
        "es2022": True,
        "node": True,
        "jest": True
    },
    "extends": [
        "eslint:recommended",
        "react-app",
        "react-app/jest",
        "@typescript-eslint/recommended",
        "prettier"
    ],
    "plugins": [
        "react",
        "react-hooks",
        "jsx-a11y",
        "import",
        "@typescript-eslint",
        "security"
    ],
    "parser": "@typescript-eslint/parser",
    "parserOptions": {
        "ecmaFeatures": {
            "jsx": True
        },
        "ecmaVersion": 2022,
        "sourceType": "module"
    },
    "settings": {
        "react": {
            "version": "detect"
        },
        "import/resolver": {
            "node": {
                "extensions": [".js", ".jsx", ".ts", ".tsx"]
            }
        }
    },
    "rules": {
        # React Specific Rules
        "react/jsx-uses-react": "off",
        "react/react-in-jsx-scope": "off",
        "react/jsx-uses-vars": "error",
        "react/jsx-no-undef": "error",
        "react/jsx-no-duplicate-props": "error",
        "react/jsx-no-target-blank": "error",
        "react/jsx-pascal-case": "error",
        "react/jsx-closing-bracket-location": "error",
        "react/jsx-closing-tag-location": "error",
        "react/jsx-curly-spacing": ["error", { "when": "never" }],
        "react/jsx-equals-spacing": ["error", "never"],
        "react/jsx-first-prop-new-line": ["error", "multiline"],
        "react/jsx-indent": ["error", 2],
        "react/jsx-indent-props": ["error", 2],
        "react/jsx-max-props-per-line": ["error", { "maximum": 3 }],
        "react/jsx-no-comment-textnodes": "error",
        "react/jsx-no-literals": "off",
        "react/jsx-sort-props": ["error", {
            "ignoreCase": True,
            "callbacksLast": True,
            "shorthandFirst": True
        }],
        "react/jsx-wrap-multilines": ["error", {
            "declaration": "parens-new-line",
            "assignment": "parens-new-line",
            "return": "parens-new-line",
            "arrow": "parens-new-line",
            "condition": "parens-new-line",
            "logical": "parens-new-line",
            "prop": "parens-new-line"
        }],
        
        # React Component Rules
        "react/no-array-index-key": "warn",
        "react/no-danger": "error",
        "react/no-deprecated": "error",
        "react/no-did-mount-set-state": "error",
        "react/no-did-update-set-state": "error",
        "react/no-direct-mutation-state": "error",
        "react/no-find-dom-node": "error",
        "react/no-is-mounted": "error",
        "react/no-multi-comp": ["error", { "ignoreStateless": True }],
        "react/no-render-return-value": "error",
        "react/no-string-refs": "error",
        "react/no-unescaped-entities": "error",
        "react/no-unknown-property": "error",
        "react/no-unused-prop-types": "error",
        "react/prop-types": "off", # Using TypeScript instead
        "react/require-render-return": "error",
        "react/self-closing-comp": "error",
        "react/sort-comp": "error",
        
        # React Hooks Rules
        "react-hooks/rules-of-hooks": "error",
        "react-hooks/exhaustive-deps": "warn",
        
        # Accessibility Rules
        "jsx-a11y/accessible-emoji": "error",
        "jsx-a11y/alt-text": "error",
        "jsx-a11y/anchor-has-content": "error",
        "jsx-a11y/aria-activedescendant-has-tabindex": "error",
        "jsx-a11y/aria-props": "error",
        "jsx-a11y/aria-proptypes": "error",
        "jsx-a11y/aria-role": "error",
        "jsx-a11y/aria-unsupported-elements": "error",
        "jsx-a11y/click-events-have-key-events": "error",
        "jsx-a11y/heading-has-content": "error",
        "jsx-a11y/img-redundant-alt": "error",
        "jsx-a11y/interactive-supports-focus": "error",
        "jsx-a11y/label-has-associated-control": "error",
        "jsx-a11y/mouse-events-have-key-events": "error",
        "jsx-a11y/no-access-key": "error",
        "jsx-a11y/no-autofocus": "warn",
        "jsx-a11y/no-distracting-elements": "error",
        "jsx-a11y/no-redundant-roles": "error",
        "jsx-a11y/no-static-element-interactions": "error",
        "jsx-a11y/role-has-required-aria-props": "error",
        "jsx-a11y/role-supports-aria-props": "error",
        "jsx-a11y/scope": "error",
        "jsx-a11y/tabindex-no-positive": "error",
        
        # TypeScript Rules
        "@typescript-eslint/no-unused-vars": ["error", { "argsIgnorePattern": "^_" }],
        "@typescript-eslint/no-explicit-any": "warn",
        "@typescript-eslint/no-non-null-assertion": "warn",
        "@typescript-eslint/prefer-const": "error",
        "@typescript-eslint/prefer-nullish-coalescing": "error",
        "@typescript-eslint/prefer-optional-chain": "error",
        "@typescript-eslint/no-unnecessary-type-assertion": "error",
        "@typescript-eslint/no-inferrable-types": "error",
        "@typescript-eslint/ban-ts-comment": ["error", {
            "ts-expect-error": "allow-with-description",
            "ts-ignore": True,
            "ts-nocheck": True,
            "ts-check": False
        }],
        
        # Import Rules
        "import/order": ["error", {
            "groups": [
                "builtin",
                "external",
                "internal",
                "parent",
                "sibling",
                "index"
            ],
            "pathGroups": [
                {
                    "pattern": "react",
                    "group": "external",
                    "position": "before"
                },
                {
                    "pattern": "@/**",
                    "group": "internal",
                    "position": "before"
                }
            ],
            "pathGroupsExcludedImportTypes": ["react"],
            "newlines-between": "always",
            "alphabetize": {
                "order": "asc",
                "caseInsensitive": True
            }
        }],
        "import/newline-after-import": "error",
        "import/no-duplicate-imports": "error",
        "import/no-unresolved": "error",
        
        # Security Rules
        "security/detect-object-injection": "warn",
        "security/detect-non-literal-regexp": "error",
        "security/detect-unsafe-regex": "error",
        
        # General Rules
        "no-console": ["warn", { "allow": ["warn", "error"] }],
        "no-debugger": "error",
        "no-alert": "error",
        "no-var": "error",
        "prefer-const": "error",
        "eqeqeq": ["error", "always"],
        "curly": ["error", "all"],
        "brace-style": ["error", "1tbs"],
        "comma-dangle": ["error", "always-multiline"],
        "indent": ["error", 2, { "SwitchCase": 1 }],
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
        "max-len": ["error", {
            "code": 120,
            "ignoreUrls": True,
            "ignoreStrings": True,
            "ignoreTemplateLiterals": True
        }]
    },
    "overrides": [
        {
            "files": ["**/*.test.ts", "**/*.test.tsx", "**/*.spec.ts", "**/*.spec.tsx"],
            "env": {
                "jest": True
            },
            "rules": {
                "no-console": "off",
                "@typescript-eslint/no-explicit-any": "off"
            }
        },
        {
            "files": ["src/setupTests.ts"],
            "rules": {
                "import/no-unresolved": "off"
            }
        }
    ]
}

# Save frontend ESLint config
with open('frontend-eslintrc.json', 'w') as f:
    json.dump(frontend_eslint_config, f, indent=2)

print("Frontend ESLint configuration created successfully!")