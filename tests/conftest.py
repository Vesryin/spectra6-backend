import pytest
from unittest.mock import MagicMock
from app.factory import create_app

@pytest.fixture
def app():
    """Create and configure a new app instance for each test."""
    # create a mock database connection
    mock_db_conn = MagicMock()
    
    # create the app with the mock database connection
    app = create_app(db_connection=mock_db_conn)
    
    yield app

@pytest.fixture
def client(app):
    """A test client for the app."""
    from starlette.testclient import TestClient
    return TestClient(app)
