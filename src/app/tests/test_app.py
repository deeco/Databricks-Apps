import sys
from pathlib import Path

import pytest
import streamlit as st


def test_app_imports():
    """Test that the app can be imported without errors."""
    # Add the app directory to the path so we can import the app
    app_path = Path(__file__).parent.parent
    sys.path.insert(0, str(app_path))
    
    try:
        # Import the actual app.py module, not the package
        import app.app as app_module
        assert True, "App imported successfully"
    except Exception as e:
        pytest.fail(f"Failed to import app: {e}")


def test_app_has_required_components():
    """Test that the app has the required components."""
    # Add the app directory to the path so we can import the app
    app_path = Path(__file__).parent.parent
    sys.path.insert(0, str(app_path))
    
    # Import the actual app.py module, not the package
    import app.app as app_module
    
    # Check that JOB_ID is accessible (it's defined in the module)
    assert hasattr(app_module, "JOB_ID"), "JOB_ID should be available"
    
    # Check that WorkspaceClient is imported
    assert "WorkspaceClient" in dir(app_module), "WorkspaceClient should be imported" 