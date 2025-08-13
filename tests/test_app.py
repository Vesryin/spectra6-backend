import pytest

# The client fixture is automatically sourced from conftest.py

def test_hello_world(client):
    response = client.get("/")
    assert response.status_code == 200
    assert response.text == "Hello, world!"
