from models.pedido_items import PedidoItem
from sqlalchemy.orm import subqueryload, joinedload, join, outerjoin
from models import db

class PedidoItemsRepository:
    def criar(self, pedido_item: PedidoItem) -> PedidoItem:
        db.session.add(pedido_item)
        db.session.commit()
        return pedido_item

    def buscar_por_pedido_id(self, id):
        return db.session.query(PedidoItem).filter(PedidoItem.pedido_id == id).all()

    def buscar_por_id(self, id) -> PedidoItem:
        return db.session.query(PedidoItem).options(subqueryload(PedidoItem.bebida), subqueryload(PedidoItem.lanche)).filter(PedidoItem.pedido_id == id).all()
    
    def listar(self):
        return db.session.query(PedidoItem).all()

    def atualizar(self, pedido: PedidoItem) -> PedidoItem:
        db.session.merge(pedido)
        db.session.commit()
        db.session.refresh(pedido)
        return pedido

    def deletar(self, id) -> PedidoItem:
        pedido = self.buscar_por_id(id)
        db.session.delete(pedido)
        db.session.commit()
        return pedido