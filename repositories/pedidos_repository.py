from interfaces.pedidos import IPedidosRepository
from sqlalchemy.orm import joinedload
from models.pedido import Pedido
from models import db

class PedidosRepository(IPedidosRepository):
    def criar(self, pedido: Pedido) -> Pedido:
        db.session.add(pedido)
        db.session.commit()
        return pedido

    def buscar_por_id(self, id) -> Pedido:
        return db.session.query(Pedido).options(joinedload(Pedido.cliente), joinedload(Pedido.funcionario)).filter(Pedido.id == id).first()
    
    def listar(self):
        return db.session.query(Pedido).options(joinedload(Pedido.cliente), joinedload(Pedido.funcionario)).all()

    def atualizar(self, pedido: Pedido) -> Pedido:
        db.session.merge(pedido)
        db.session.commit()
        db.session.refresh(pedido)
        return pedido

    def deletar(self, id) -> Pedido:
        pedido = self.buscar_por_id(id)
        db.session.delete(pedido)
        db.session.commit()
        return pedido