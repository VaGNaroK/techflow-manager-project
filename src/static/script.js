const API_URL = '/tasks';

const modal = document.getElementById('modal-tarefa');
const btnNovaTarefa = document.getElementById('btn-nova-tarefa');
const closeBtn = document.querySelector('.close-btn');
const formTarefa = document.getElementById('form-tarefa');

// Status Map
const nextStatus = {
    'A Fazer': 'Em Progresso',
    'Em Progresso': 'Concluído',
    'Concluído': null
};
const prevStatus = {
    'A Fazer': null,
    'Em Progresso': 'A Fazer',
    'Concluído': 'Em Progresso'
};

// Event Listeners for Modal
btnNovaTarefa.addEventListener('click', () => {
    modal.classList.remove('hidden');
    formTarefa.reset();
});

closeBtn.addEventListener('click', () => {
    modal.classList.add('hidden');
});

// Event Listener for Form Submit
formTarefa.addEventListener('submit', async (e) => {
    e.preventDefault();
    const titulo = document.getElementById('titulo').value;
    const descricao = document.getElementById('descricao').value;
    const prioridade = document.getElementById('prioridade').value;

    const data = {
        title: titulo,
        description: descricao,
        priority: prioridade,
        status: 'A Fazer'
    };

    try {
        const response = await fetch(API_URL, {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify(data)
        });
        if (response.ok) {
            modal.classList.add('hidden');
            loadTasks();
        } else {
            alert('Erro ao criar tarefa');
        }
    } catch (error) {
        console.error('Erro:', error);
    }
});

// Load tasks from API
async function loadTasks() {
    try {
        const response = await fetch(API_URL);
        const tasks = await response.json();
        
        // Clear all columns
        document.querySelectorAll('.task-list').forEach(col => col.innerHTML = '');

        tasks.forEach(task => {
            renderTask(task);
        });
    } catch (error) {
        console.error('Erro ao buscar tarefas:', error);
    }
}

// Render a single task card
function renderTask(task) {
    const colStatus = {
        'A Fazer': 'col-a-fazer',
        'Em Progresso': 'col-em-progresso',
        'Concluído': 'col-concluido'
    };

    const containerId = colStatus[task.status];
    const container = document.querySelector(`#${containerId} .task-list`);
    if (!container) return;

    const card = document.createElement('div');
    card.className = 'task-card';
    card.innerHTML = `
        <div class="task-header">
            <span class="task-title">${task.title}</span>
            <span class="task-priority priority-${task.priority}">${task.priority}</span>
        </div>
        <div class="task-desc">${task.description}</div>
        <div class="task-actions">
            ${prevStatus[task.status] ? `<button onclick="updateTaskStatus(${task.id}, '${prevStatus[task.status]}')">&larr;</button>` : ''}
            ${nextStatus[task.status] ? `<button onclick="updateTaskStatus(${task.id}, '${nextStatus[task.status]}')">&rarr;</button>` : ''}
            <button class="delete-btn" onclick="deleteTask(${task.id})">X</button>
        </div>
    `;

    container.appendChild(card);
}

// Update task status
window.updateTaskStatus = async (id, newStatus) => {
    try {
        const response = await fetch(`${API_URL}/${id}`, {
            method: 'PUT',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify({ status: newStatus })
        });
        if (response.ok) {
            loadTasks();
        }
    } catch (error) {
        console.error('Erro ao atualizar status:', error);
    }
};

// Delete task
window.deleteTask = async (id) => {
    if (!confirm('Deseja realmente excluir esta tarefa?')) return;
    try {
        const response = await fetch(`${API_URL}/${id}`, {
            method: 'DELETE'
        });
        if (response.ok) {
            loadTasks();
        }
    } catch (error) {
        console.error('Erro ao excluir tarefa:', error);
    }
};

// Initial load
loadTasks();
