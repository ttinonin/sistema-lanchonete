from interfaces.clientes import IClientesRepository
from models.cliente import Cliente
from models import db

class ClientesRepository(IClientesRepository):
    def criar(self, cliente: Cliente) -> Cliente:
        db.session.add(cliente)
        db.session.commit()
        return cliente

    def buscar_por_id(self, id) -> Cliente:
        return db.session.get(Cliente, id)
    
    def listar(self):
        return db.session.query(Cliente).all()

    def atualizar(self, cliente: Cliente) -> Cliente:
        db.session.merge(cliente)
        db.session.commit()
        db.session.refresh(cliente)
        return cliente

    def deletar(self, id) -> Cliente:
        cliente = self.buscar_por_id(id)
        db.session.delete(cliente)
        db.session.commit()
        return cliente