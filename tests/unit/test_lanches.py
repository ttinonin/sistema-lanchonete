from models.lanche import Lanche
from repositories.lanches_repository import LanchesRepository
from sqlalchemy.orm.exc import UnmappedInstanceError
from decimal import Decimal
import pytest

def test_criar_lanche(session):
    lanche = Lanche(nome="X-Bacon", preco=29.99, descricao="Lanche feito com hamburguer, bacon, queijo prado e calabresa.")

    lanche_repo = LanchesRepository()
    criado = lanche_repo.criar(lanche)

    assert criado is not None
    assert criado.nome == "X-Bacon"
    assert criado.preco == Decimal("29.99")
    assert criado.descricao == "Lanche feito com hamburguer, bacon, queijo prado e calabresa."

def test_buscar_lanche_por_id(session):
    lanche = Lanche(nome="X-Ovo", preco=19.99, descricao="Lanche feito com hamburguer, queijo mussarela e dois ovos fritos.")

    lanche_repo = LanchesRepository()
    criado = lanche_repo.criar(lanche)

    encontrado = lanche_repo.buscar_por_id(criado.id)

    assert encontrado is not None
    assert encontrado.nome == "X-Ovo"
    assert encontrado.preco == Decimal("19.99")
    assert encontrado.descricao == "Lanche feito com hamburguer, queijo mussarela e dois ovos fritos."

def test_listar_lanches(session):
    f1 = Lanche(nome="X-Bacon", preco=29.99, descricao="Lanche feito com hamburguer, bacon, queijo prado e calabresa.")
    f2 = Lanche(nome="X-Ovo", preco=19.99, descricao="Lanche feito com hamburguer, queijo mussarela e dois ovos fritos.")

    session.add_all([f1, f2])
    session.commit()
    lanche_repo = LanchesRepository()

    todos = lanche_repo.listar()

    assert len(todos) == 2
    nomes = [f.nome for f in todos]
    assert "X-Bacon" in nomes
    assert "X-Ovo" in nomes

def test_atualizar_lanche(session):
    lanche = Lanche(nome="X-Bacon", preco=29.99, descricao="Lanche feito com hamburguer, bacon, queijo prado e calabresa.")
    repo = LanchesRepository()

    repo.criar(lanche)

    criado = repo.buscar_por_id(lanche.id)

    criado.nome = "X-Calabresa"
    atual = repo.atualizar(criado)
    
    assert atual.nome == "X-Calabresa"
    assert atual.preco == Decimal("29.99")
    assert atual.descricao == "Lanche feito com hamburguer, bacon, queijo prado e calabresa."

def test_deletar_lanche(session):
    repo = LanchesRepository()

    f1 = Lanche(nome="X-Bacon", preco=29.99, descricao="Lanche feito com hamburguer, bacon, queijo prado e calabresa.")
    f2 = Lanche(nome="X-Ovo", preco=19.99, descricao="Lanche feito com hamburguer, queijo mussarela e dois ovos fritos.")

    session.add_all([f1, f2])
    session.commit()

    deletado = repo.deletar(f2.id)

    assert deletado.id == 2
    assert deletado.nome == "X-Ovo"