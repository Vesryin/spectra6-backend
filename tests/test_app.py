import pytest
from starlette.testclient import TestClient
from app import api

@pytest.fixture
def client():
    return TestClient(api)

def test_hello_world(client):
    response = client.get("/")
    assert response.status_code == 200
    assert response.text == "Hello, world!"
