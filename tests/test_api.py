from fastapi.testclient import TestClient
from GeekyAnts.main import app

client = TestClient(app)

def test_chat():
    response = client.post("/chat", json={"query": "Find Python developer"})
    assert response.status_code == 200
    assert "response" in response.json()

def test_employee_search():
    response = client.get("/employees/search?skill=Python&experience=3")
    assert response.status_code == 200
    assert "results" in response.json()
