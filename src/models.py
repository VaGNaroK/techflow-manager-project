class Task:
    def __init__(self, task_id, title, description, status="A Fazer", priority="MÃ©dia"):
        self.id = task_id
        self.title = title
        self.description = description
        self.status = status  # A Fazer, Em Progresso, ConcluÃ­do
        self.priority = priority  # Adicionado na alteraÃ§Ã£o de escopo: Baixa, MÃ©dia, Alta

    def to_dict(self):
        return {
            "id": self.id,
            "title": self.title,
            "description": self.description,
            "status": self.status,
            "priority": self.priority
        }
