from flask import Flask, jsonify, request
from models import Task

app = Flask(__name__)

# Simulação do Banco de dados
tasks_db = {}
current_id = 1

@app.route('/tasks', methods=['POST'])
def create_task():
    global current_id
    data = request.get_json() or {}
    
    # Validação de Entrada
    if not data.get('title') or not data.get('title').strip():
        return jsonify({"error": "Ponha o título obrigatório da tarefa."}), 400

    task = Task(
        task_id=current_id,
        title=data.get('title'),
        description=data.get('description', ''),
        status=data.get('status', 'A Fazer'),
        priority=data.get('priority', 'Média') # Suporta a mudança de escopo
    )
    
    tasks_db[current_id] = task
    current_id += 1
    return jsonify(task.to_dict()), 201

@app.route('/tasks', methods=['GET'])
def get_tasks():
    return jsonify([task.to_dict() for task in tasks_db.values()]), 200

@app.route('/tasks/<int:task_id>', methods=['GET'])
def get_task(task_id):
    task = tasks_db.get(task_id)
    if not task:
        return jsonify({"error": "Tarefa não encontrada."}), 404
    return jsonify(task.to_dict()), 200

@app.route('/tasks/<int:task_id>', methods=['PUT'])
def update_task(task_id):
    task = tasks_db.get(task_id)
    if not task:
        return jsonify({"error": "Tarefa não encontrada."}), 404
    
    data = request.get_json() or {}
    
    if 'title' in data:
        if not data.get('title').strip():
            return jsonify({"error": "Ponha o título obrigatório da tarefa."}), 400
        task.title = data['title']
        
    if 'description' in data:
        task.description = data['description']
    if 'status' in data:
        task.status = data['status']
    if 'priority' in data:
        task.priority = data['priority']
        
    return jsonify(task.to_dict()), 200

@app.route('/tasks/<int:task_id>', methods=['DELETE'])
def delete_task(task_id):
    if task_id in tasks_db:
        del tasks_db[task_id]
        return jsonify({"message": "Tarefa removida com sucesso."}), 200
    return jsonify({"error": "Tarefa não encontrada."}), 404

if __name__ == '__main__':
    app.run(debug=True)
