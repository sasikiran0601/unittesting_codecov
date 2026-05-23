from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_read_root():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"message": "Hello World"}

def test_add():
    response = client.get("/add/5/3")
    assert response.status_code == 200
    assert response.json() == {"result": 8}

def test_multiply():
    response = client.get("/multiply/4/5")
    assert response.status_code == 200
    assert response.json() == {"result": 20}
