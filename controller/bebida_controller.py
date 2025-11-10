from repositories.bebidas_repository import BebidasRepository
from models.bebida import Bebida
from decimal import Decimal

class BebidaController:
    def __init__(self):
        self.repo = BebidasRepository()
    
    def criar(self, nome: str, preco: str, litragem: str):
        if not nome or not preco or not litragem:
            raise ValueError("Preencher todos os campos!")
        
        bebida = Bebida(nome=nome, preco=Decimal(preco), litragem=int(litragem))
        self.repo.criar(bebida)

    def buscar(self, id):
        return self.repo.buscar_por_id(id)

    def listar(self):
        return self.repo.listar()
    
    def deletar(self, id: int):
        return self.repo.deletar(id)