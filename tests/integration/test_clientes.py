from models.cliente import Cliente
from repositories.clientes_repository import ClientesRepository
from sqlalchemy.orm.exc import UnmappedInstanceError
import pytest

def test_criar_cliente(session):
    cliente = Cliente(nome="Gabriel", endereco="Rua dos passarinhos 123", telefone="(11) 98223-4775")

    cliente_repo = ClientesRepository()
    criado = cliente_repo.criar(cliente)

    encontrado = cliente_repo.buscar_por_id(criado.id)

    assert encontrado is not None
    assert encontrado.nome == "Gabriel"
    assert encontrado.endereco == "Rua dos passarinhos 123"
    assert encontrado.telefone == "(11) 98223-4775"

def test_buscar_cliente_por_id(session):
    cliente = Cliente(nome="Heitor", endereco="Rua dos vianas 179", telefone="(13) 98773-4935")

    cliente_repo = ClientesRepository()
    criado = cliente_repo.criar(cliente)

    encontrado = cliente_repo.buscar_por_id(criado.id)

    assert encontrado is not None
    assert encontrado.nome == "Heitor"
    assert encontrado.endereco == "Rua dos vianas 179"
    assert encontrado.telefone == "(13) 98773-4935"

def test_listar_clientes(session):
    f1 = Cliente(nome="Gabriel", endereco="Rua dos passarinhos 123", telefone="(11) 98223-4775")
    f2 = Cliente(nome="Heitor", endereco="Rua dos vianas 179", telefone="(13) 98773-4935")

    session.add_all([f1, f2])
    session.commit()
    cliente_repo = ClientesRepository()

    todos = cliente_repo.listar()

    assert len(todos) == 2
    nomes = [f.nome for f in todos]
    assert "Gabriel" in nomes
    assert "Heitor" in nomes

def test_atualizar_cliente(session):
    cliente = Cliente(nome="Eduardo", endereco="Rua dos passarinhos 123", telefone="(11) 93446-3775")
    repo = ClientesRepository()

    repo.criar(cliente)

    criado = repo.buscar_por_id(cliente.id)

    criado.nome = "Daniel"
    atual = repo.atualizar(criado)
    
    assert atual.nome == "Daniel"
    assert atual.endereco == "Rua dos passarinhos 123"
    assert atual.telefone == "(11) 93446-3775"

def test_deletar_cliente(session):
    repo = ClientesRepository()

    f1 = Cliente(nome="Gabriel", endereco="Rua dos passarinhos 123", telefone="(11) 98223-4775")
    f2 = Cliente(nome="Heitor", endereco="Rua dos vianas 179", telefone="(13) 98773-4935")

    session.add_all([f1, f2])
    session.commit()

    deletado = repo.deletar(f1.id)

    assert deletado.id == 1
    assert deletado.nome == "Gabriel"
    assert deletado.endereco == "Rua dos passarinhos 123"
    assert deletado.telefone == "(11) 98223-4775"