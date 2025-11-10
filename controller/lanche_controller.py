from repositories.lanches_repository import LanchesRepository
from models.lanche import Lanche
from decimal import Decimal

class LancheController:
    def __init__(self):
        self.repo = LanchesRepository()
    
    def criar(self, nome: str, preco: str, descricao: str):
        if not nome or not preco or not descricao:
            raise ValueError("Preencher todos os campos!")
        
        lanche = Lanche(nome=nome, preco=Decimal(preco), descricao=descricao)
        self.repo.criar(lanche)

    def buscar(self, id):
        return self.repo.buscar_por_id(id)

    def listar(self):
        return self.repo.listar()
    
    def deletar(self, id: int):
        return self.repo.deletar(id)