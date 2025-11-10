from repositories.clientes_repository import ClientesRepository
from models.cliente import Cliente
from werkzeug.security import generate_password_hash

class ClienteController:
    def __init__(self):
        self.repo = ClientesRepository()
    
    def criar(self, nome: str, telefone: str, endereco: str):
        if not nome or not telefone or not endereco:
            raise ValueError("Preencher todos os campos!")
        
        cliente = Cliente(nome=nome, telefone=telefone, endereco=endereco)
        self.repo.criar(cliente)

    def listar(self):
        return self.repo.listar()
    
    def deletar(self, id: int):
        return self.repo.deletar(id)