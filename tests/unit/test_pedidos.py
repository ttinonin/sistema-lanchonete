from unittest.mock import MagicMock
from models.pedido import Pedido
from decimal import Decimal
from interfaces.pedidos import IPedidosRepository
from repositories.pedidos_repository import PedidosRepository

def test_criar_pedido():
    repo = MagicMock()
    pedido = Pedido(cliente_id=1, funcionario_id=2, valor=200.00)

    repo.criar.return_value = pedido

    criado = repo.criar(pedido)

    assert criado is not None
    assert criado.cliente_id == 1
    assert criado.funcionario_id == 2
    assert criado.valor == 200.00


def test_buscar_pedido_por_id():
    repo = MagicMock()
    pedido = Pedido(cliente_id=3, funcionario_id=5, valor=350.50)

    repo.criar.return_value = pedido
    repo.buscar_por_id.return_value = pedido

    criado = repo.criar(pedido)
    encontrado = repo.buscar_por_id(criado.id)

    assert encontrado is not None
    assert encontrado.cliente_id == 3
    assert encontrado.funcionario_id == 5
    assert encontrado.valor == 350.50


def test_listar_pedidos():
    repo = MagicMock()
    p1 = Pedido(cliente_id=1, funcionario_id=2, valor=200.00)
    p2 = Pedido(cliente_id=3, funcionario_id=4, valor=150.00)

    repo.listar.return_value = [p1, p2]

    todos = repo.listar()

    assert len(todos) == 2
    clientes = [p.cliente_id for p in todos]
    assert 1 in clientes
    assert 3 in clientes


def test_atualizar_pedido():
    repo = MagicMock()
    pedido = Pedido(cliente_id=1, funcionario_id=2, valor=200.00)

    repo.criar.return_value = pedido
    repo.buscar_por_id.return_value = pedido
    repo.atualizar.return_value = pedido

    criado = repo.criar(pedido)
    encontrado = repo.buscar_por_id(criado.id)

    encontrado.valor = 250.00
    atualizado = repo.atualizar(encontrado)

    assert atualizado.valor == 250.00
    assert atualizado.cliente_id == 1
    assert atualizado.funcionario_id == 2


def test_deletar_pedido():
    repo = MagicMock()
    p1 = Pedido(cliente_id=1, funcionario_id=2, valor=200.00)
    p2 = Pedido(cliente_id=3, funcionario_id=4, valor=150.00)

    repo.deletar.return_value = p2

    deletado = repo.deletar(p2.id)

    assert deletado is not None
    assert deletado.cliente_id == 3
    assert deletado.funcionario_id == 4
    assert deletado.valor == 150.00

def test_cliente_especial():
    repo = MagicMock()
    p1 = Pedido(cliente_id=1, funcionario_id=2, valor=200.00)

    repo.criar.return_value = p1
    repo.criar.return_value.valor = 200 - (200.00*0.25)

    criado = repo.criar(p1.id)

    assert criado is not None
    assert criado.cliente_id == 1
    assert criado.funcionario_id == 2
    assert criado.valor == 200 - (200.00*0.25)

def test_classe_abstrata_pedido_repo():
    assert issubclass(PedidosRepository, IPedidosRepository)
    assert hasattr(PedidosRepository, 'criar')
    assert hasattr(PedidosRepository, 'buscar_por_id')
    assert hasattr(PedidosRepository, 'listar')
    assert hasattr(PedidosRepository, 'atualizar')
    assert hasattr(PedidosRepository, 'deletar')