class TaskError(Exception):
    """Classe base para todas as exceções relacionadas a tarefas."""
    pass

class NameIsNotNone(TaskError):
    """Exceção levantada quando o nome da tarefa é nulo ou vazio."""

    def __init__(self):
        super().__init__("O nome da tarefa não pode ser vazio.")

class DueDateIsNotNone(TaskError):
    """Exceção levantada quando a data de previsão de término é nula ou vazia."""

    def __init__(self):
        super().__init__("A data de previsão de término da tarefa não pode estar vazia.")