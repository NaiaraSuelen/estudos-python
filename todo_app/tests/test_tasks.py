from todo_app.exceptions import NameIsNotNone, DueDateIsNotNone
from unittest.mock import patch
import pytest

from todo_app.tasks import Task

class TestTasks():

    def test_sucesso_criacao_da_task(self):
        task = Task("Fazer Compra", "20/02/2025", "Realizar compra da semana")
        assert task.name == "Fazer Compra"
        assert task.due_date == "20/02/2025"
        assert task.status == "Pendente"
        assert task.created_at is not None

    def test_criacao_de_tarefa_nao_pode_ter_nome_vazio(self):
        with pytest.raises(NameIsNotNone, match="O nome da tarefa não pode ser vazio."):
            Task("","20/02/2025")

    def test_criacao_de_tarefa_nao_pode_ter_data_de_previsao_de_termino_vazia(self):
        with pytest.raises(DueDateIsNotNone, match="A data de previsão de término da tarefa não pode estar vazia."):
            Task("Fazer Compra", "")

    def test_saida_tarefa_criada(self):
        mock_date = "26/01/2025"
        with patch('todo_app.tasks.datetime') as mock_datetime:
            mock_datetime.now.return_value = mock_date

        task = Task("Fazer Compras","20/02/2025","Realizar a compra da semana")
        task.created_at = mock_date

        esperado = (
            f"Tarefa: Fazer Compras\n"
            f"Descrição: Realizar a compra da semana\n"
            f"Criado em: 26/01/2025\n"
            f"Previsão de término: 20/02/2025\n"
            f"Status: Pendente"
        )

        assert str(task) == esperado