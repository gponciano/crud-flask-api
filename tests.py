import pytest
import requests

# CRUD

# Create
BASE_URL = 'http://127.0.0.1:5000'
tasks = []

def test_create_task():
    new_task_data = {
        "title": "Study Unit Testing",
        "description": "chapter 4 from Python book"
    }
    response = requests.post(f"{BASE_URL}/tasks", json=new_task_data)

    assert response.status_code == 200

    response_json = response.json()
    assert "message" in response_json
    assert "id" in response_json
    tasks.append(response_json['id'])


# Read
def test_get_tasks():
    response = requests.get(f"{BASE_URL}/tasks")
    response_json = response.json()

    assert response.status_code == 200

    assert "tasks" in response_json
    assert "total_tasks" in response_json
