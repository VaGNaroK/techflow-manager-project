class Task:
    def __init__(self, task_id, title, description, status="A Fazer", priority="Média"):
        self.id = task_id
        self.title = title
        self.description = description
        self.status = status  # Estado: A Fazer, Em Progresso, Concluído
        self.priority = priority  # Adicionado na alteração de escopo: Baixa, Média, Alta

    def to_dict(self):
        return {
            "id": self.id,
            "title": self.title,
            "description": self.description,
            "status": self.status,
            "priority": self.priority
        }
