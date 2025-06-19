#!/bin/bash

# Databricks Apps DABs Setup Script
# This script helps you set up the development environment

set -e

echo "🚀 Setting up Databricks Apps DABs project..."

# Check if Python 3.11+ is installed
python_version=$(python3 --version 2>&1 | awk '{print $2}' | cut -d. -f1,2)
required_version="3.11"

if [ "$(printf '%s\n' "$required_version" "$python_version" | sort -V | head -n1)" != "$required_version" ]; then
    echo "❌ Error: Python 3.11 or later is required. Current version: $python_version"
    exit 1
fi

echo "✅ Python version check passed: $python_version"

# Create virtual environment
echo "📦 Creating virtual environment..."
python3 -m venv .venv

# Activate virtual environment
echo "🔧 Activating virtual environment..."
source .venv/bin/activate

# Upgrade pip
echo "⬆️  Upgrading pip..."
pip install --upgrade pip

# Install dependencies
echo "📚 Installing dependencies..."
pip install -r src/app/requirements.txt

# Install development dependencies
echo "🔧 Installing development dependencies..."
pip install pytest ruff streamlit

# Create .env file if it doesn't exist
if [ ! -f .env ]; then
    echo "📝 Creating .env file..."
    cat > .env << EOF
# Databricks Configuration
# Update these values with your workspace details
DATABRICKS_HOST=https://your-workspace.cloud.databricks.com/
DATABRICKS_CLIENT_ID=your-client-id
DATABRICKS_CLIENT_SECRET=your-client-secret

# App Configuration
JOB_ID=your-job-id
EOF
    echo "⚠️  Please update the .env file with your actual Databricks credentials"
fi

# Check if databricks CLI is installed
if ! command -v databricks &> /dev/null; then
    echo "⚠️  Databricks CLI not found. Please install it:"
    echo "   pip install databricks-cli"
    echo "   or visit: https://docs.databricks.com/dev-tools/cli/index.html"
else
    echo "✅ Databricks CLI found"
fi

echo ""
echo "🎉 Setup complete!"
echo ""
echo "Next steps:"
echo "1. Update .env file with your Databricks credentials"
echo "2. Update databricks.yml with your workspace URLs"
echo "3. Run: streamlit run src/app/app.py"
echo "4. Run tests: python -m pytest src/app/tests -v"
echo ""
echo "For deployment:"
echo "1. Setup GitHub secrets (DATABRICKS_HOST, DATABRICKS_CLIENT_ID, DATABRICKS_CLIENT_SECRET)"
echo "2. Deploy to dev: databricks bundle deploy -t dev"
echo "3. Run app: databricks bundle run hello-world-app -t dev"
echo ""
echo "Happy coding! 🚀" 