

from fastapi.testclient import TestClient
from app.main import app

client= TestClient(app)


def test_root():
    res = client.get("/")
    print(res.json())
    assert res.json().get('message') == 'Hello World'
    assert res.status_code == 200

def test_create_user():
    res = client.post("/create_user/",json={"email":"hello123@gmail.com",
    "password":"password123"})
    print(res.json())
    assert res.status_code == 201
