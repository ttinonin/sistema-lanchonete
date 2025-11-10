from models.pedido import Pedido
from repositories.pedidos_repository import PedidosRepository
from sqlalchemy.orm.exc import UnmappedInstanceError
from decimal import Decimal
import pytest

def test_criar_pedido(session):
    repo = PedidosRepository()

    pedido = Pedido(cliente_id=1, funcionario_id=2, valor=Decimal("10.00"))

    criado = repo.criar(pedido)

    assert criado is not None
    assert criado.cliente_id == 1
    assert criado.funcionario_id == 2
    assert criado.valor == Decimal("10.00")

def test_deletar_pedido(session):
    repo = PedidosRepository()

    pedido = Pedido(cliente_id=1, funcionario_id=2, valor=Decimal("10.00"))

    criado = repo.criar(pedido)

    deletado = repo.deletar(criado.id)

    assert deletado is not None
    assert deletado.cliente_id == 1
    assert deletado.funcionario_id == 2
    assert deletado.valor == Decimal("10.00")