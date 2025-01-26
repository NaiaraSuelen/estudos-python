from datetime import datetime

from todo_app.exceptions import NameIsNotNone, DueDateIsNotNone

class Task():
    def __init__(self, name: str, due_date: str, descricao: str = ""):
        if not name.strip():
            raise NameIsNotNone()

        if not due_date.strip():
            raise DueDateIsNotNone

        self.name = name
        self.descricao = descricao
        self.due_date = due_date
        self.created_at = datetime.now().strftime("%d/%m/%Y")
        self.status = "Pendente"

    def __str__(self):
        return (
            f"Tarefa: {self.name}\n"
            f"Descrição: {self.descricao}\n"
            f"Criado em: {self.created_at}\n"
            f"Previsão de término: {self.due_date}\n"
            f"Status: {self.status}"
        )