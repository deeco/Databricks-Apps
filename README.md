# Databricks Apps with GitHub Actions and Databricks Asset Bundles

This repository demonstrates how to automate Databricks Apps deployments using GitHub Actions and Databricks Asset Bundles (DABs). It provides a complete CI/CD pipeline for building, testing, and deploying data applications on the Databricks Data Intelligence Platform.

## Overview

This project implements a Streamlit application that allows users to trigger Databricks jobs through a web interface. The deployment pipeline includes:

- **Local Development**: Run and test the app locally
- **Development Environment**: Deploy to a development workspace for testing
- **Production Environment**: Automated deployments via GitHub Actions
- **Continuous Integration**: Code quality checks and testing on pull requests
- **Continuous Deployment**: Automated production deployments on releases

## Project Structure

```
├── databricks.yml              # Main DABs bundle configuration
├── src/
│   └── app/
│       ├── app.py              # Main Streamlit application
│       ├── app.yaml            # App configuration
│       ├── requirements.txt    # Python dependencies
│       └── tests/
│           └── test_app.py     # Unit tests
├── resources/
│   ├── app.yml                 # App resource configuration
│   ├── jobs.yml                # Job resource configuration
│   └── clusters.yml            # Cluster resource configuration
├── .github/
│   └── workflows/
│       ├── push.yml            # CI workflow for pull requests
│       └── release.yml         # CD workflow for releases
└── README.md                   # This file
```

## Prerequisites

- Python 3.11 or later
- Databricks CLI 0.18.0 or later
- U2M OAuth authentication set up for your workspace
- GitHub repository with access to GitHub Actions

## Quick Start

### 1. Clone and Setup

```bash
git clone <your-repo-url>
cd databricks-apps-dabs
```

### 2. Configure Environments

Edit `databricks.yml` and update the workspace URLs:

```yaml
targets:
  dev:
    workspace:
      host: https://your-dev-workspace.cloud.databricks.com/
  prod:
    workspace:
      host: https://your-prod-workspace.cloud.databricks.com/
```

### 3. Local Development

Create a virtual environment and install dependencies:

```bash
python3 -m venv .venv
source .venv/bin/activate  # On Windows: .venv\Scripts\activate
pip install -r src/app/requirements.txt
```

Run the app locally:

```bash
streamlit run src/app/app.py
```

Run tests:

```bash
python -m pytest src/app/tests -v
```

### 4. Development Deployment

Deploy to your development environment:

```bash
databricks bundle deploy -t dev
databricks bundle run hello-world-app -t dev
```

### 5. Setup GitHub Secrets

In your GitHub repository, add these secrets:

- `DATABRICKS_HOST`: Your Databricks workspace URL
- `DATABRICKS_CLIENT_ID`: Service principal client ID
- `DATABRICKS_CLIENT_SECRET`: Service principal OAuth secret

### 6. Production Deployment

Create a release in GitHub to trigger automated production deployment:

```bash
git tag -a v1.0.0 -m "Release version 1.0.0"
git push origin v1.0.0
```

Then create a release in GitHub UI using this tag.

## Development Workflow

1. **Feature Development**: Create a feature branch
   ```bash
   git checkout -b feature/new-feature
   ```

2. **Local Testing**: Test your changes locally
   ```bash
   streamlit run src/app/app.py
   python -m pytest src/app/tests -v
   ```

3. **Development Deployment**: Deploy to dev environment
   ```bash
   databricks bundle deploy -t dev
   databricks bundle run hello-world-app -t dev
   ```

4. **Pull Request**: Create a PR to main branch
   - Triggers CI pipeline (linting, testing)
   - Requires code review approval

5. **Production Release**: Create a release
   - Triggers automated production deployment
   - Deploys to production environment

## Configuration

### Environment Variables

The app uses these environment variables:

- `JOB_ID`: ID of the Databricks job to trigger (set by DABs)

### Service Principal Setup

1. Create a service principal in your Databricks workspace
2. Generate OAuth credentials for the service principal
3. Add the credentials to GitHub repository secrets

### Workspace Configuration

- **Development**: Uses default workspace settings
- **Production**: Uses isolated workspace paths with proper permissions

## Best Practices

### Security
- Use service principals for automated deployments
- Rotate credentials regularly
- Protect main branch with branch protection rules
- Require code reviews for pull requests

### Development
- Develop in feature branches
- Test locally before deploying
- Use separate environments for different stages
- Monitor deployment pipelines

### Code Quality
- Run linting and tests locally
- Use automated code quality checks in CI
- Follow consistent coding standards
- Document code changes

## Troubleshooting

### Common Issues

1. **Authentication Errors**: Ensure U2M OAuth is properly configured
2. **Deployment Failures**: Check workspace permissions and service principal access
3. **App Not Starting**: Verify cluster configuration and resource limits
4. **Job Trigger Failures**: Ensure job ID is correct and permissions are set

### Debug Commands

```bash
# Check bundle status
databricks bundle status

# Validate bundle configuration
databricks bundle validate

# Check workspace connectivity
databricks workspace list

# View app logs
databricks apps logs --app-id <app-id>
```

## Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Add tests for new functionality
5. Ensure all tests pass
6. Submit a pull request

## Resources

- [Databricks Apps Documentation](https://docs.databricks.com/apps/index.html)
- [Databricks Asset Bundles](https://docs.databricks.com/dev-tools/bundles/index.html)
- [Databricks CLI](https://docs.databricks.com/dev-tools/cli/index.html)
- [GitHub Actions Documentation](https://docs.github.com/en/actions)

## License

This project is licensed under the MIT License - see the LICENSE file for details.
