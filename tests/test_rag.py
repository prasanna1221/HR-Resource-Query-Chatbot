from app.rag_engine import answer_query
import json

def load_sample_data():
    with open("data/employees.json") as f:
        return json.load(f)["employees"]

def test_answer_query_keywords():
    employees = load_sample_data()
    query = "Find Python developers"
    response = answer_query(query, employees)
    assert "Python" in response or "developer" in response
