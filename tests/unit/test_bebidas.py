from unittest.mock import MagicMock
from models.bebida import Bebida
from decimal import Decimal
import pytest
from sqlalchemy.exc import IntegrityError
from repositories.bebidas_repository import BebidasRepository
from interfaces.bebidas import IBebidasRepository

def test_criar_bebida():
    bebida_repo = MagicMock()

    bebida = Bebida(nome="Coca Cola", preco=13.99, litragem=2)

    bebida_repo.criar.return_value = bebida

    criado = bebida_repo.criar(bebida)

    assert criado is not None
    assert criado.nome == "Coca Cola"
    assert criado.preco == 13.99
    assert criado.litragem == 2

    bebida_repo.criar.assert_called_once_with(bebida)

def test_listar_bebidas():
    bebida_repo_mock = MagicMock()

    f1 = Bebida(nome="Coca Cola", preco=13.99, litragem=2)
    f2 = Bebida(nome="Guarana Xereta", preco=5.99, litragem=2)
    bebida_repo_mock.listar.return_value = [f1, f2]

    todos = bebida_repo_mock.listar()

    assert len(todos) == 2
    nomes = [f.nome for f in todos]
    assert "Coca Cola" in nomes
    assert "Guarana Xereta" in nomes

    bebida_repo_mock.listar.assert_called_once()

def test_atualizar_bebida():
    repo_mock = MagicMock()

    bebida = Bebida(nome="Dolly Limao", preco=6.99, litragem=2)
    repo_mock.criar.return_value = bebida

    repo_mock.buscar_por_id.return_value = bebida
    repo_mock.atualizar.return_value = bebida

    criado = repo_mock.criar(bebida)
    criado.preco = Decimal("5.99")
    atualizado = repo_mock.atualizar(criado)

    assert atualizado.nome == "Dolly Limao"
    assert atualizado.preco == Decimal("5.99")
    assert atualizado.litragem == 2

    repo_mock.criar.assert_called_once_with(bebida)
    repo_mock.atualizar.assert_called_once_with(criado)

def test_deletar_bebida():
    repo_mock = MagicMock()

    f1 = Bebida(nome="Coca Cola", preco=13.99, litragem=2)
    f2 = Bebida(nome="Guarana Xereta", preco=5.99, litragem=2)

    repo_mock.deletar.return_value = f1

    deletado = repo_mock.deletar(f1.id)

    assert deletado.nome == "Coca Cola"
    assert deletado.preco == 13.99
    assert deletado.litragem == 2

    repo_mock.deletar.assert_called_once_with(f1.id)


def test_criar_bebida_sem_nome_unitario():
    bebida_repo_mock = MagicMock()
    bebida = Bebida(nome=None, preco=13.99, litragem=2)

    bebida_repo_mock.criar(bebida)

@pytest.mark.parametrize(
    "nome, preco, litragem, esperado",
    [
        ("Coca Cola", Decimal("13.99"), 2, True),
        ("Guarana", Decimal("5.99"), 1, True),
        ("Fanta", Decimal("7.49"), 2, True),
        (None, Decimal("10.00"), 1, False),
    ]
)
def test_criar_bebida(nome, preco, litragem, esperado, session):
    bebida = Bebida(nome=nome, preco=preco, litragem=litragem)
    bebida_repo = BebidasRepository()

    if esperado:
        criado = bebida_repo.criar(bebida)
        assert criado is not None
        assert criado.nome == nome
        assert criado.preco == preco
        assert criado.litragem == litragem
    else:
        with pytest.raises(IntegrityError):
            bebida_repo.criar(bebida)

def test_classe_abstrata_bebida_repo():
    assert issubclass(BebidasRepository, IBebidasRepository)
    assert hasattr(BebidasRepository, 'criar')
    assert hasattr(BebidasRepository, 'buscar_por_id')
    assert hasattr(BebidasRepository, 'listar')
    assert hasattr(BebidasRepository, 'atualizar')
    assert hasattr(BebidasRepository, 'deletar')