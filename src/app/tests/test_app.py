import streamlit as st
import sys
import os

# Add the app directory to the path so we can import the app
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))

def test_app_imports():
    """Test that the app can be imported without errors."""
    try:
        import app
        assert True, "App imported successfully"
    except Exception as e:
        assert False, f"Failed to import app: {e}"

def test_app_has_required_components():
    """Test that the app has the required components."""
    import app
    
    # Check that JOB_ID is accessible
    assert hasattr(app, 'JOB_ID') or 'JOB_ID' in os.environ, "JOB_ID should be available"
    
    # Check that WorkspaceClient is imported
    assert 'WorkspaceClient' in dir(app), "WorkspaceClient should be imported" 