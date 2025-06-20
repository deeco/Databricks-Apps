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
        import app
        assert True, "App imported successfully"
    except Exception as e:
        pytest.fail(f"Failed to import app: {e}")


def test_app_has_required_components():
    """Test that the app has the required components."""
    # Add the app directory to the path so we can import the app
    app_path = Path(__file__).parent.parent
    sys.path.insert(0, str(app_path))
    
    import app
    
    # Check that JOB_ID is accessible
    assert hasattr(app, "JOB_ID") or "JOB_ID" in app.__dict__, "JOB_ID should be available"
    
    # Check that WorkspaceClient is imported
    assert "WorkspaceClient" in dir(app), "WorkspaceClient should be imported" 