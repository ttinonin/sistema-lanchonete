from models.funcionario import Funcionario
from repositories.funcionarios_repository import FuncionariosRepository
from sqlalchemy.orm.exc import UnmappedInstanceError
import pytest

def test_criar_funcionario(session):
    funcionario = Funcionario(nome="Nicholas", email="nicholas@gmail.com", senha="123")

    funcionario_repo = FuncionariosRepository()
    criado = funcionario_repo.criar(funcionario)

    encontrado = funcionario_repo.buscar_por_id(criado.id)

    assert encontrado is not None
    assert encontrado.nome == "Nicholas"
    assert encontrado.email == "nicholas@gmail.com"

def test_buscar_funcionario_por_id(session):
    funcionario = Funcionario(nome="Pedro", email="pedro@gmail.com", senha="123")

    funcionario_repo = FuncionariosRepository()
    criado = funcionario_repo.criar(funcionario)

    encontrado = funcionario_repo.buscar_por_id(criado.id)

    assert encontrado is not None
    assert encontrado.nome == "Pedro"
    assert encontrado.email == "pedro@gmail.com"

def test_buscar_funcionario_por_email(session):
    funcionario = Funcionario(nome="Pedro", email="pedro@gmail.com", senha="123")

    funcionario_repo = FuncionariosRepository()
    criado = funcionario_repo.criar(funcionario)

    encontrado = funcionario_repo.buscar_por_email(criado.email)

    assert encontrado is not None
    assert encontrado.nome == "Pedro"
    assert encontrado.email == "pedro@gmail.com"

def test_listar_funcionarios(session):
    f1 = Funcionario(nome="Nicholas", email="nicholas@gmail.com", senha="123")
    f2 = Funcionario(nome="Pedro", email="pedro@gmail.com", senha="123")

    session.add_all([f1, f2])
    session.commit()
    funcionario_repo = FuncionariosRepository()

    todos = funcionario_repo.listar()

    assert len(todos) == 2
    nomes = [f.nome for f in todos]
    assert "Nicholas" in nomes
    assert "Pedro" in nomes

def test_atualizar_funcionario(session):
    funcionario = Funcionario(
        nome="Eduardo", 
        email="eduardo@gmail.com", senha="123")
    repo = FuncionariosRepository()

    repo.criar(funcionario)

    criado = repo.buscar_por_id(funcionario.id)

    criado.nome = "Daniel"
    atual = repo.atualizar(criado)
    
    assert atual.nome == "Daniel"
    assert atual.email == "eduardo@gmail.com"

def test_deletar_funcionario(session):
    repo = FuncionariosRepository()

    f1 = Funcionario(nome="Eduardo", email="eduardo@gmail.com", senha="123")
    f2 = Funcionario(nome="Nicholas", email="nicholas@gmail.com", senha="123")

    session.add_all([f1, f2])
    session.commit()

    deletado = repo.deletar(f2.id)

    assert deletado.id == 2
    assert deletado.nome == "Nicholas"
    assert deletado.email == "nicholas@gmail.com"

def test_deletar_funcionario_id_invalido_gera_erro(session):
    repo = FuncionariosRepository()

    with pytest.raises(UnmappedInstanceError) as exc_info:
        deletado = repo.deletar(1)