from flask import Flask, request
from models.task import Task

# __name__ = "__main__"
app = Flask(__name__)


tasks = []

@app.route("/tasks", methods=['POST'])
def create_task():
    data = request.get_json()
    print(data)
    return "Testing"

if __name__ == "__main__":
    app.run(debug=True)