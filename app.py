from flask import Flask, request, jsonify
from models.task import Task

# __name__ = "__main__"
app = Flask(__name__)


tasks = []
task_id_control = 1


@app.route("/tasks", methods=['POST'])
def create_task():
    data = request.get_json()
    global task_id_control
    # Leaving description as an optional field
    new_task = Task(id=task_id_control, title=data['title'], description=data.get("description", "")) 

    task_id_control += 1
    tasks.append(new_task)
    print(tasks)
    return jsonify({"message": "New task created succesfully"})

@app.route("/tasks", methods=['GET'])
def get_all():
    task_list = [task.to_dictionary() for task in tasks]
    output = {
                "tasks": task_list,
                "total_tasks": 0
            }
    return jsonify(output)

if __name__ == "__main__":
    app.run(debug=True)