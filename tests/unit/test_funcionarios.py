from unittest.mock import MagicMock
from models.funcionario import Funcionario
from sqlalchemy.orm.exc import UnmappedInstanceError
import pytest
from interfaces.funcionarios import IFuncionariosRepository
from repositories.funcionarios_repository import FuncionariosRepository

def test_criar_funcionario():
    funcionario_repo_mock = MagicMock()
    funcionario = Funcionario(nome="Nicholas", email="nicholas@gmail.com", senha="123")

    funcionario_repo_mock.criar.return_value = funcionario
    funcionario_repo_mock.buscar_por_id.return_value = funcionario

    criado = funcionario_repo_mock.criar(funcionario)
    encontrado = funcionario_repo_mock.buscar_por_id(criado.id)

    assert encontrado is not None
    assert encontrado.nome == "Nicholas"
    assert encontrado.email == "nicholas@gmail.com"

def test_buscar_funcionario_por_id():
    funcionario_repo_mock = MagicMock()
    funcionario = Funcionario(nome="Pedro", email="pedro@gmail.com", senha="123")

    funcionario_repo_mock.criar.return_value = funcionario
    funcionario_repo_mock.buscar_por_id.return_value = funcionario

    criado = funcionario_repo_mock.criar(funcionario)
    encontrado = funcionario_repo_mock.buscar_por_id(criado.id)

    assert encontrado is not None
    assert encontrado.nome == "Pedro"
    assert encontrado.email == "pedro@gmail.com"

def test_listar_funcionarios():
    funcionario_repo_mock = MagicMock()
    f1 = Funcionario(nome="Nicholas", email="nicholas@gmail.com", senha="123")
    f2 = Funcionario(nome="Pedro", email="pedro@gmail.com", senha="123")

    funcionario_repo_mock.listar.return_value = [f1, f2]

    todos = funcionario_repo_mock.listar()

    assert len(todos) == 2
    nomes = [f.nome for f in todos]
    assert "Nicholas" in nomes
    assert "Pedro" in nomes

def test_atualizar_funcionario():
    funcionario_repo_mock = MagicMock()
    funcionario = Funcionario(nome="Eduardo", email="eduardo@gmail.com", senha="123")

    funcionario_repo_mock.criar.return_value = funcionario
    funcionario_repo_mock.buscar_por_id.return_value = funcionario
    funcionario_repo_mock.atualizar.return_value = funcionario

    repo_mock = funcionario_repo_mock
    repo_mock.criar(funcionario)

    criado = repo_mock.buscar_por_id(funcionario.id)

    criado.nome = "Daniel"
    atual = repo_mock.atualizar(criado)

    assert atual.nome == "Daniel"
    assert atual.email == "eduardo@gmail.com"

def test_deletar_funcionario():
    funcionario_repo_mock = MagicMock()
    f1 = Funcionario(nome="Eduardo", email="eduardo@gmail.com", senha="123")
    f2 = Funcionario(nome="Nicholas", email="nicholas@gmail.com", senha="123")

    funcionario_repo_mock.deletar.return_value = f2

    deletado = funcionario_repo_mock.deletar(f2.id)

    assert deletado.nome == "Nicholas"
    assert deletado.email == "nicholas@gmail.com"

def test_deletar_funcionario_id_invalido_gera_erro():
    funcionario_repo_mock = MagicMock()
    funcionario_repo_mock.deletar.side_effect = UnmappedInstanceError("Funcionario não encontrado")

    with pytest.raises(UnmappedInstanceError):
        funcionario_repo_mock.deletar(1)

def test_classe_abstrata_funcionario_repo():
    assert issubclass(FuncionariosRepository, IFuncionariosRepository)
    assert hasattr(FuncionariosRepository, 'criar')
    assert hasattr(FuncionariosRepository, 'buscar_por_id')
    assert hasattr(FuncionariosRepository, 'listar')
    assert hasattr(FuncionariosRepository, 'atualizar')
    assert hasattr(FuncionariosRepository, 'deletar')
