from unittest.mock import MagicMock
from models.lanche import Lanche
from decimal import Decimal
from interfaces.lanches import ILanchesRepository
from repositories.lanches_repository import LanchesRepository

def test_criar_lanche():
    lanche_repo_mock = MagicMock()
    lanche = Lanche(nome="X-Bacon", preco=29.99, descricao="Lanche feito com hamburguer, bacon, queijo prado e calabresa.")

    lanche_repo_mock.criar.return_value = lanche

    criado = lanche_repo_mock.criar(lanche)

    assert criado is not None
    assert criado.nome == "X-Bacon"
    assert criado.preco == 29.99
    assert criado.descricao == "Lanche feito com hamburguer, bacon, queijo prado e calabresa."

def test_buscar_lanche_por_id():
    lanche_repo_mock = MagicMock()
    lanche = Lanche(nome="X-Ovo", preco=19.99, descricao="Lanche feito com hamburguer, queijo mussarela e dois ovos fritos.")

    lanche_repo_mock.criar.return_value = lanche
    lanche_repo_mock.buscar_por_id.return_value = lanche

    criado = lanche_repo_mock.criar(lanche)
    encontrado = lanche_repo_mock.buscar_por_id(criado.id)

    assert encontrado is not None
    assert encontrado.nome == "X-Ovo"
    assert encontrado.preco == 19.99
    assert encontrado.descricao == "Lanche feito com hamburguer, queijo mussarela e dois ovos fritos."

def test_listar_lanches():
    lanche_repo_mock = MagicMock()
    f1 = Lanche(nome="X-Bacon", preco=29.99, descricao="Lanche feito com hamburguer, bacon, queijo prado e calabresa.")
    f2 = Lanche(nome="X-Ovo", preco=19.99, descricao="Lanche feito com hamburguer, queijo mussarela e dois ovos fritos.")

    lanche_repo_mock.listar.return_value = [f1, f2]

    todos = lanche_repo_mock.listar()

    assert len(todos) == 2
    nomes = [f.nome for f in todos]
    assert "X-Bacon" in nomes
    assert "X-Ovo" in nomes

def test_atualizar_lanche():
    lanche_repo_mock = MagicMock()
    lanche = Lanche(nome="X-Bacon", preco=29.99, descricao="Lanche feito com hamburguer, bacon, queijo prado e calabresa.")

    lanche_repo_mock.criar.return_value = lanche
    lanche_repo_mock.buscar_por_id.return_value = lanche
    lanche_repo_mock.atualizar.return_value = lanche

    repo_mock = lanche_repo_mock
    repo_mock.criar(lanche)

    criado = repo_mock.buscar_por_id(lanche.id)

    criado.nome = "X-Calabresa"
    atual = repo_mock.atualizar(criado)

    assert atual.nome == "X-Calabresa"
    assert atual.preco == 29.99
    assert atual.descricao == "Lanche feito com hamburguer, bacon, queijo prado e calabresa."

def test_deletar_lanche():
    lanche_repo_mock = MagicMock()
    f1 = Lanche(nome="X-Bacon", preco=29.99, descricao="Lanche feito com hamburguer, bacon, queijo prado e calabresa.")
    f2 = Lanche(nome="X-Ovo", preco=19.99, descricao="Lanche feito com hamburguer, queijo mussarela e dois ovos fritos.")

    lanche_repo_mock.deletar.return_value = f2

    deletado = lanche_repo_mock.deletar(f2.id)

    assert deletado.nome == "X-Ovo"
    assert deletado.preco == 19.99
    assert deletado.descricao == "Lanche feito com hamburguer, queijo mussarela e dois ovos fritos."

def test_classe_abstrata_lanche_repo():
    assert issubclass(LanchesRepository, ILanchesRepository)
    assert hasattr(LanchesRepository, 'criar')
    assert hasattr(LanchesRepository, 'buscar_por_id')
    assert hasattr(LanchesRepository, 'listar')
    assert hasattr(LanchesRepository, 'atualizar')
    assert hasattr(LanchesRepository, 'deletar')