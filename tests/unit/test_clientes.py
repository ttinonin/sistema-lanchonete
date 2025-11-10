from unittest.mock import MagicMock
from models.cliente import Cliente
from decimal import Decimal
from interfaces.clientes import IClientesRepository
from repositories.clientes_repository import ClientesRepository

def test_criar_cliente():
    cliente_repo_mock = MagicMock()
    cliente = Cliente(nome="Gabriel", endereco="Rua dos passarinhos 123", telefone="(11) 98223-4775")

    cliente_repo_mock.criar.return_value = cliente
    cliente_repo_mock.buscar_por_id.return_value = cliente

    criado = cliente_repo_mock.criar(cliente)
    encontrado = cliente_repo_mock.buscar_por_id(criado.id)

    assert encontrado is not None
    assert encontrado.nome == "Gabriel"
    assert encontrado.endereco == "Rua dos passarinhos 123"
    assert encontrado.telefone == "(11) 98223-4775"

def test_buscar_cliente_por_id():
    cliente_repo_mock = MagicMock()
    cliente = Cliente(nome="Heitor", endereco="Rua dos vianas 179", telefone="(13) 98773-4935")

    cliente_repo_mock.criar.return_value = cliente
    cliente_repo_mock.buscar_por_id.return_value = cliente

    criado = cliente_repo_mock.criar(cliente)
    encontrado = cliente_repo_mock.buscar_por_id(criado.id)

    assert encontrado is not None
    assert encontrado.nome == "Heitor"
    assert encontrado.endereco == "Rua dos vianas 179"
    assert encontrado.telefone == "(13) 98773-4935"

def test_listar_clientes():
    cliente_repo_mock = MagicMock()
    f1 = Cliente(nome="Gabriel", endereco="Rua dos passarinhos 123", telefone="(11) 98223-4775")
    f2 = Cliente(nome="Heitor", endereco="Rua dos vianas 179", telefone="(13) 98773-4935")

    cliente_repo_mock.listar.return_value = [f1, f2]

    todos = cliente_repo_mock.listar()

    assert len(todos) == 2
    nomes = [f.nome for f in todos]
    assert "Gabriel" in nomes
    assert "Heitor" in nomes

def test_atualizar_cliente():
    cliente_repo_mock = MagicMock()
    cliente = Cliente(nome="Eduardo", endereco="Rua dos passarinhos 123", telefone="(11) 93446-3775")

    cliente_repo_mock.criar.return_value = cliente
    cliente_repo_mock.buscar_por_id.return_value = cliente
    cliente_repo_mock.atualizar.return_value = cliente

    repo_mock = cliente_repo_mock
    repo_mock.criar(cliente)

    criado = repo_mock.buscar_por_id(cliente.id)

    criado.nome = "Daniel"
    atual = repo_mock.atualizar(criado)

    assert atual.nome == "Daniel"
    assert atual.endereco == "Rua dos passarinhos 123"
    assert atual.telefone == "(11) 93446-3775"

def test_deletar_cliente():
    cliente_repo_mock = MagicMock()
    f1 = Cliente(nome="Gabriel", endereco="Rua dos passarinhos 123", telefone="(11) 98223-4775")
    f2 = Cliente(nome="Heitor", endereco="Rua dos vianas 179", telefone="(13) 98773-4935")

    cliente_repo_mock.deletar.return_value = f1

    deletado = cliente_repo_mock.deletar(f1.id)

    assert deletado.nome == "Gabriel"
    assert deletado.endereco == "Rua dos passarinhos 123"
    assert deletado.telefone == "(11) 98223-4775"

def test_classe_abstrata_funcionario_repo():
    assert issubclass(ClientesRepository, IClientesRepository)
    assert hasattr(ClientesRepository, 'criar')
    assert hasattr(ClientesRepository, 'buscar_por_id')
    assert hasattr(ClientesRepository, 'listar')
    assert hasattr(ClientesRepository, 'atualizar')
    assert hasattr(ClientesRepository, 'deletar')