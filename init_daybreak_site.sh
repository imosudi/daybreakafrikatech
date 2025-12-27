#!/usr/bin/env bash

# Exit immediately if a command exits with a non-zero status
set -e

PROJECT_ROOT="daybreak_site"

echo "Creating project structure for ${PROJECT_ROOT}..."

# Root directory
mkdir -p "${PROJECT_ROOT}"

# Top-level files
touch "${PROJECT_ROOT}/main.py"
touch "${PROJECT_ROOT}/main.wsgi"
touch "${PROJECT_ROOT}/config.py"
touch "${PROJECT_ROOT}/database.db"
touch "${PROJECT_ROOT}/requirements.txt"

# App directories
mkdir -p "${PROJECT_ROOT}/app/models"
mkdir -p "${PROJECT_ROOT}/app/routes"
mkdir -p "${PROJECT_ROOT}/app/templates"
mkdir -p "${PROJECT_ROOT}/app/static"

# App-level files
touch "${PROJECT_ROOT}/app/__init__.py"
touch "${PROJECT_ROOT}/app/extensions.py"

# Models
touch "${PROJECT_ROOT}/app/models/__init__.py"
touch "${PROJECT_ROOT}/app/models/inquiry.py"
touch "${PROJECT_ROOT}/app/models/portfolio.py"
touch "${PROJECT_ROOT}/app/models/api_key.py"

# Routes
touch "${PROJECT_ROOT}/app/routes/__init__.py"
touch "${PROJECT_ROOT}/app/routes/main.py"
touch "${PROJECT_ROOT}/app/routes/solutions.py"
touch "${PROJECT_ROOT}/app/routes/developer.py"
touch "${PROJECT_ROOT}/app/routes/ai.py"
touch "${PROJECT_ROOT}/app/routes/solution_finder.py"

echo "Project structure created successfully."
echo "Location: $(realpath "${PROJECT_ROOT}")"


PROJECT_ROOT="daybreak_site"
TEMPLATES_DIR="${PROJECT_ROOT}/app/templates"

echo "Creating template paths under ${TEMPLATES_DIR}..."

# Base templates directory
mkdir -p "${TEMPLATES_DIR}"

# Home
touch "${TEMPLATES_DIR}/home.html"

# Solutions
mkdir -p "${TEMPLATES_DIR}/solutions"
touch "${TEMPLATES_DIR}/solutions/index.html"
touch "${TEMPLATES_DIR}/solutions/infrastructure.html"
touch "${TEMPLATES_DIR}/solutions/software.html"
touch "${TEMPLATES_DIR}/solutions/ai.html"
touch "${TEMPLATES_DIR}/solutions/security.html"

# Developer
mkdir -p "${TEMPLATES_DIR}/developer"
touch "${TEMPLATES_DIR}/developer/index.html"
touch "${TEMPLATES_DIR}/developer/identity_apis.html"
touch "${TEMPLATES_DIR}/developer/fullstack.html"
touch "${TEMPLATES_DIR}/developer/docs.html"
touch "${TEMPLATES_DIR}/developer/sandbox.html"

# AI
mkdir -p "${TEMPLATES_DIR}/ai"
touch "${TEMPLATES_DIR}/ai/index.html"
touch "${TEMPLATES_DIR}/ai/digital_twins.html"
touch "${TEMPLATES_DIR}/ai/agent_based.html"
touch "${TEMPLATES_DIR}/ai/simulation.html"

# Solution Finder
mkdir -p "${TEMPLATES_DIR}/solution_finder"
touch "${TEMPLATES_DIR}/solution_finder/index.html"

echo "Template structure created successfully."
