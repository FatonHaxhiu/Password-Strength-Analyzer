import pytest
from app import app


@pytest.fixture
def client():
    """Create a test client for the Flask app."""
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client


def test_index_get(client):
    """Test GET request to index page."""
    response = client.get('/')
    assert response.status_code == 200
    assert b"Password Strength Analyzer" in response.data


def test_index_post_valid(client):
    """Test POST request with a valid password."""
    response = client.post('/', data={'password': 'Ab1@xyz789'})
    assert response.status_code == 200
    assert b"Score" in response.data
    assert b"Strength: Strong" in response.data


def test_index_post_empty(client):
    """Test POST request with an empty password."""
    response = client.post('/', data={'password': ''})
    assert response.status_code == 200
    assert b"Password cannot be empty." in response.data
