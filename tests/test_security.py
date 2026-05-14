from fastapi.testclient import TestClient
from app_secure import app

client = TestClient(app)


def test_allowed_file_returns_200():
    response = client.get("/read_file?path=fake_repo/README.md")
    assert response.status_code == 200


def test_secret_file_returns_403():
    response = client.get("/read_file?path=fake_repo/secret.env")
    assert response.status_code == 403


def test_arbitrary_path_returns_403():
    response = client.get("/read_file?path=app_secure.py")
    assert response.status_code == 403
