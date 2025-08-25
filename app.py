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


@app.route('/tasks', methods=['GET'])
def get_all():
    task_list = [task.to_dictionary() for task in tasks]
    output = {
                "tasks": task_list,
                "total_tasks": len(task_list)
            }
    return jsonify(output)


@app.route('/tasks/<int:id>', methods=['GET'])
def get_task(id):
    
    for t in tasks:
        if t.id == id:
            return jsonify(t.to_dictionary())
        
    return jsonify({"message": "We were unable to find this task."}), 404

@app.route('/tasks/<int:id>', methods=['PUT'])
def update_task(id):
    
    task = None
    for t in tasks:
        if t.id == id:
            task = t
    print(task)
    if task == None:
        return jsonify({"message": "We were unable to find this task."}), 404
    
    data = request.get_json()
    task.title = data['title']
    task.description = data['description']
    task.completed = data['completed']

    print(task)
    return jsonify({"message": "Task updated succesfully"})


@app.route('/tasks/<int:id>', methods=['DELETE'])
def delete_task(id):
    task = None
    for t in tasks:
        if t.id == id:
            task = t
            break 
    
    if task == None:
        return jsonify({"message": "We were unable to find this task."}), 404
    
    
    tasks.remove(task)
    
    return jsonify({"message": "Task has been deleted"})

if __name__ == "__main__":
    app.run(debug=True)