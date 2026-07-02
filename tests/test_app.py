import sys
import os
import pytest

# Adiciona o diretório src ao path para os testes localizarem os módulos
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../src')))

from app import app, tasks_db

@pytest.fixture
def client():
    app.config['TESTING'] = True
    with app.test_client() as client:
        with app.app_context():
            tasks_db.clear()  # Limpa o banco antes de cada teste
        yield client

def test_create_task_success(client):
    """Garante que uma tarefa válida de logística é criada com sucesso."""
    response = client.post('/tasks', json={
        "title": "Carregamento Caminhao 01",
        "description": "Fazer a triagem e embarque de 40 pacotes prioritarios."
    })
    assert response.status_code == 201
    data = response.get_json()
    assert data['id'] == 1
    assert data['title'] == "Carregamento Caminhao 01"
    assert data['status'] == "A Fazer"

def test_create_task_missing_title(client):
    """Controle de Qualidade: Garante que validações de entrada barram dados inconsistentes."""
    response = client.post('/tasks', json={
        "title": "   ",
        "description": "Sem titulo valido"
    })
    assert response.status_code == 400
    assert "error" in response.get_json()

def test_get_all_tasks(client):
    """Garante a listagem correta das demandas do quadro."""
    client.post('/tasks', json={"title": "Tarefa 1"})
    client.post('/tasks', json={"title": "Tarefa 2"})
    
    response = client.get('/tasks')
    assert response.status_code == 200
    assert len(response.get_json()) == 2

def test_update_task_status(client):
    """Simula a movimentação de uma tarefa no fluxo Kanban (A Fazer -> Em Progresso)."""
    create_res = client.post('/tasks', json={"title": "Alocacao de Motoristas"})
    task_id = create_res.get_json()['id']
    
    update_res = client.put('/tasks/{task_id}', json={"status": "Em Progresso"})
    assert update_res.status_code == 200
    assert update_res.get_json()['status'] == "Em Progresso"
