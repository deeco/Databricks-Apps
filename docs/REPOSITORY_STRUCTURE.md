# Repository Structure

This document explains the complete structure of the Databricks Apps DABs repository and the purpose of each file and directory.

## Root Directory

```
databricks-apps-dabs/
├── databricks.yml              # Main DABs bundle configuration
├── pyproject.toml              # Python project configuration
├── .gitignore                  # Git ignore rules
├── README.md                   # Main project documentation
├── LICENSE                     # MIT license
├── src/                        # Source code directory
├── resources/                  # DABs resource definitions
├── .github/                    # GitHub Actions workflows
├── scripts/                    # Setup and utility scripts
└── docs/                       # Documentation
```

## Configuration Files

### `databricks.yml`
The main Databricks Asset Bundle configuration file that defines:
- Bundle name and metadata
- Development and production environments
- Workspace configurations
- Resource mappings

### `pyproject.toml`
Modern Python project configuration including:
- Project metadata and dependencies
- Development dependencies (pytest, ruff, black)
- Tool configurations (ruff linting, pytest settings)

### `.gitignore`
Excludes common files from version control:
- Python cache and build files
- Virtual environments
- IDE configuration files
- Databricks configuration files
- Log files and temporary files

## Source Code (`src/`)

### `src/app/`
Contains the main Streamlit application:

- **`app.py`**: Main Streamlit application that provides a web interface to trigger Databricks jobs
- **`app.yaml`**: App configuration with environment variables and metadata
- **`requirements.txt`**: Python dependencies for the Streamlit app
- **`tests/test_app.py`**: Unit tests for the application

### `src/notebooks/`
Contains Databricks notebooks:

- **`hello_world_notebook.py`**: Sample notebook that gets triggered by the app

## Resources (`resources/`)

DABs resource definitions for Databricks infrastructure:

### `resources/app.yml`
Defines the Databricks App resource:
- App name and description
- Source code path
- Resource permissions (job access)

### `resources/jobs.yml`
Defines the Databricks Job resource:
- Job name and description
- Task configuration (notebook path)
- Cluster assignment

### `resources/clusters.yml`
Defines the Databricks Cluster resource:
- Cluster configuration (Spark version, node type)
- Worker count and Spark configurations

## GitHub Actions (`.github/workflows/`)

### `push.yml`
Continuous Integration workflow triggered on:
- Pull request creation/updates
- Pushes to main branch

Actions performed:
- Python environment setup
- Dependency installation
- Code linting with Ruff
- Unit test execution with pytest

### `release.yml`
Continuous Deployment workflow triggered on:
- GitHub release publication

Actions performed:
- Bundle deployment to production
- App resource creation/update
- App code deployment and startup

## Scripts (`scripts/`)

### `setup.sh` (macOS/Linux)
Automated setup script that:
- Checks Python version requirements
- Creates virtual environment
- Installs dependencies
- Creates .env template
- Verifies Databricks CLI installation

### `setup.bat` (Windows)
Windows equivalent of the setup script with the same functionality.

## Documentation (`docs/`)

### `DEPLOYMENT.md`
Comprehensive deployment guide covering:
- Prerequisites and initial setup
- Service principal configuration
- GitHub repository setup
- Local development workflow
- Production deployment process
- Troubleshooting guide

### `REPOSITORY_STRUCTURE.md` (this file)
Detailed explanation of the repository structure and file purposes.

## File Descriptions

### Core Application Files

| File | Purpose |
|------|---------|
| `src/app/app.py` | Main Streamlit application with job triggering functionality |
| `src/app/app.yaml` | App configuration with environment variables |
| `src/app/requirements.txt` | Python dependencies for the Streamlit app |
| `src/app/tests/test_app.py` | Unit tests for application functionality |

### Configuration Files

| File | Purpose |
|------|---------|
| `databricks.yml` | Main DABs bundle configuration with environment definitions |
| `pyproject.toml` | Python project configuration and tool settings |
| `.gitignore` | Git ignore patterns for common files |
| `src/app/app.yaml` | Streamlit app configuration |

### Resource Definitions

| File | Purpose |
|------|---------|
| `resources/app.yml` | Databricks App resource definition |
| `resources/jobs.yml` | Databricks Job resource definition |
| `resources/clusters.yml` | Databricks Cluster resource definition |

### CI/CD Files

| File | Purpose |
|------|---------|
| `.github/workflows/push.yml` | CI workflow for code quality and testing |
| `.github/workflows/release.yml` | CD workflow for production deployment |

### Documentation

| File | Purpose |
|------|---------|
| `README.md` | Main project documentation and quick start guide |
| `docs/DEPLOYMENT.md` | Detailed deployment instructions |
| `docs/REPOSITORY_STRUCTURE.md` | Repository structure documentation |
| `LICENSE` | MIT license for the project |

### Scripts

| File | Purpose |
|------|---------|
| `scripts/setup.sh` | Automated setup script for macOS/Linux |
| `scripts/setup.bat` | Automated setup script for Windows |

## Key Features

### 1. Complete CI/CD Pipeline
- Automated testing on pull requests
- Automated deployment on releases
- Code quality checks with Ruff
- Unit testing with pytest

### 2. Multi-Environment Support
- Development environment for testing
- Production environment for live deployment
- Environment-specific configurations

### 3. Local Development Support
- Easy local setup with automated scripts
- Local testing capabilities
- Development workflow documentation

### 4. Security Best Practices
- Service principal authentication
- Environment variable management
- Secure credential handling

### 5. Comprehensive Documentation
- Quick start guide
- Detailed deployment instructions
- Troubleshooting guide
- Repository structure documentation

## Usage Patterns

### Development Workflow
1. Clone repository
2. Run setup script
3. Configure workspace URLs
4. Develop locally with Streamlit
5. Test changes
6. Deploy to development environment
7. Create pull request
8. Merge and create release

### Production Deployment
1. Create GitHub release
2. Automated deployment triggers
3. Bundle deployment to production
4. App resource creation/update
5. Code deployment and startup

This repository structure provides a complete, production-ready setup for Databricks Apps deployment with modern CI/CD practices and comprehensive documentation. 