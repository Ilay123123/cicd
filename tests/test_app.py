# tests/test_app.py

# Import necessary testing tools
import pytest
from app import app  # This imports your Flask app

# This fixture provides a test client that we can use to make requests
@pytest.fixture
def client():
    # Create a test client using your Flask app
    # The 'with' context ensures proper setup and cleanup
    with app.test_client() as client:
        yield client

# This is our actual test function
def test_hello_route(client):
    # Make a GET request to the root route ('/')
    response = client.get('/')
    
    # Check if the response contains our expected message
    assert response.data.decode('utf-8') == 'Hello, CI/CD World!'
    # Check if the status code is 200 (OK)
    assert response.status_code == 200
