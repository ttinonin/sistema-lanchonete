from models.bebida import Bebida
from repositories.bebidas_repository import BebidasRepository
from sqlalchemy.orm.exc import UnmappedInstanceError
from decimal import Decimal
import pytest

def test_criar_bebida(session):
    bebida = Bebida(nome="Coca Cola", preco=13.99, litragem=2)

    bebida_repo = BebidasRepository()
    criado = bebida_repo.criar(bebida)

    assert criado is not None
    assert criado.nome == "Coca Cola"
    assert criado.preco == Decimal("13.99")
    assert criado.litragem == 2

def test_buscar_bebida_por_id(session):
    bebida = Bebida(nome="Guarana Xereta", preco=5.99, litragem=2)

    bebida_repo = BebidasRepository()
    criado = bebida_repo.criar(bebida)

    encontrado = bebida_repo.buscar_por_id(criado.id)

    assert encontrado is not None
    assert encontrado.nome == "Guarana Xereta"
    assert encontrado.preco == Decimal("5.99")
    assert encontrado.litragem == 2

def test_listar_bebidas(session):
    f1 = Bebida(nome="Coca Cola", preco=13.99, litragem=2)
    f2 = Bebida(nome="Guarana Xereta", preco=5.99, litragem=2)

    session.add_all([f1, f2])
    session.commit()
    bebida_repo = BebidasRepository()

    todos = bebida_repo.listar()

    assert len(todos) == 2
    nomes = [f.nome for f in todos]
    assert "Coca Cola" in nomes
    assert "Guarana Xereta" in nomes

def test_atualizar_bebida(session):
    bebida = Bebida(nome="Dolly Limao", preco=6.99, litragem=2)
    repo = BebidasRepository()

    repo.criar(bebida)

    criado = repo.buscar_por_id(bebida.id)

    criado.preco = 5.99
    atual = repo.atualizar(criado)
    
    assert atual.nome == "Dolly Limao"
    assert atual.preco == Decimal("5.99")
    assert atual.litragem == 2

def test_deletar_bebida(session):
    repo = BebidasRepository()

    f1 = Bebida(nome="Coca Cola", preco=13.99, litragem=2)
    f2 = Bebida(nome="Guarana Xereta", preco=5.99, litragem=2)

    session.add_all([f1, f2])
    session.commit()

    deletado = repo.deletar(f1.id)

    assert deletado.id == 1
    assert deletado.nome == "Coca Cola"
    assert deletado.preco == Decimal("13.99")
    assert deletado.litragem == 2