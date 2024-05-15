from flask import Flask, jsonify, request
from models import Task

app = Flask(__name__)

tasks_db = {}
current_id = 1

@app.route('/tasks', methods=['POST'])
def create_task():
    global current_id
    data = request.get_json() or {}
    
    if not data.get('title') or not data.get('title').strip():
        return jsonify({"error": "O titulo da tarefa e obrigatorio."}), 400

    task = Task(
        task_id=current_id,
        title=data.get('title'),
        description=data.get('description', ''),
        status=data.get('status', 'A Fazer')
    )
    
    tasks_db[current_id] = task
    current_id += 1
    return jsonify(task.to_dict()), 201

if __name__ == '__main__':
    app.run(debug=True)
