import unittest
from unittest.mock import Mock

from aluno import AlunoClass


class alunoTest(unittest.TestCase):

    def test_salvarAluno(self):

        # Criando um aluno
        aluno = AlunoClass("João", "Silva", 8.5)

        # Criando um Mock para simular o banco de dados
        conexaoMock = Mock()
        colecaoMock = Mock()

        # Chamando o método salvar
        aluno.salvar(conexaoMock, colecaoMock)

        # Verificando se o método insert_one foi chamado
        colecaoMock.insert_one.assert_called_once_with({
            "nome": "João",
            "sobrenome": "Silva",
            "nota": 8.5
        })


if __name__ == '__main__':
    unittest.main()
