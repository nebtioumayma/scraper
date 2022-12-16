from fastapi.testclient import TestClient

from spyder import app

client = TestClient(app)


def test_read_main():
    response = client.post("/")
    assert response.status_code == 200
    
