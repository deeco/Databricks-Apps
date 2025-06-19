@echo off
REM Databricks Apps DABs Setup Script for Windows
REM This script helps you set up the development environment

echo 🚀 Setting up Databricks Apps DABs project...

REM Check if Python 3.11+ is installed
python --version >nul 2>&1
if errorlevel 1 (
    echo ❌ Error: Python is not installed or not in PATH
    echo Please install Python 3.11 or later from https://python.org
    pause
    exit /b 1
)

echo ✅ Python found

REM Create virtual environment
echo 📦 Creating virtual environment...
python -m venv .venv

REM Activate virtual environment
echo 🔧 Activating virtual environment...
call .venv\Scripts\activate.bat

REM Upgrade pip
echo ⬆️  Upgrading pip...
python -m pip install --upgrade pip

REM Install dependencies
echo 📚 Installing dependencies...
pip install -r src\app\requirements.txt

REM Install development dependencies
echo 🔧 Installing development dependencies...
pip install pytest ruff streamlit

REM Create .env file if it doesn't exist
if not exist .env (
    echo 📝 Creating .env file...
    (
        echo # Databricks Configuration
        echo # Update these values with your workspace details
        echo DATABRICKS_HOST=https://your-workspace.cloud.databricks.com/
        echo DATABRICKS_CLIENT_ID=your-client-id
        echo DATABRICKS_CLIENT_SECRET=your-client-secret
        echo.
        echo # App Configuration
        echo JOB_ID=your-job-id
    ) > .env
    echo ⚠️  Please update the .env file with your actual Databricks credentials
)

REM Check if databricks CLI is installed
databricks --version >nul 2>&1
if errorlevel 1 (
    echo ⚠️  Databricks CLI not found. Please install it:
    echo    pip install databricks-cli
    echo    or visit: https://docs.databricks.com/dev-tools/cli/index.html
) else (
    echo ✅ Databricks CLI found
)

echo.
echo 🎉 Setup complete!
echo.
echo Next steps:
echo 1. Update .env file with your Databricks credentials
echo 2. Update databricks.yml with your workspace URLs
echo 3. Run: streamlit run src\app\app.py
echo 4. Run tests: python -m pytest src\app\tests -v
echo.
echo For deployment:
echo 1. Setup GitHub secrets (DATABRICKS_HOST, DATABRICKS_CLIENT_ID, DATABRICKS_CLIENT_SECRET)
echo 2. Deploy to dev: databricks bundle deploy -t dev
echo 3. Run app: databricks bundle run hello-world-app -t dev
echo.
echo Happy coding! 🚀
pause 