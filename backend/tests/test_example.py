import pytest
from fastapi.testclient import TestClient
from backend.main import app

@pytest.fixture
def client():
    with TestClient(app) as c:
        yield c

def test_app_exists():
    assert app is not None

def test_root_not_found(client):
    # Testing a non-existent route just to show the client works
    response = client.get("/non-existent")
    assert response.status_code == 404
