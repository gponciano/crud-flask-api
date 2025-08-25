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