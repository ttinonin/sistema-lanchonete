from datetime import datetime
from . import db

class PedidoItem(db.Model):
    __tablename__ = 'pedido_items'

    pedido_id = db.Column(db.Integer, db.ForeignKey('pedidos.id', ondelete='CASCADE', onupdate='CASCADE'), primary_key=True)
    lanche_id = db.Column(db.Integer, db.ForeignKey('lanches.id', ondelete='SET NULL', onupdate='CASCADE'), primary_key=True, nullable=True)
    bebida_id = db.Column(db.Integer, db.ForeignKey('bebidas.id', ondelete='SET NULL', onupdate='CASCADE'), primary_key=True, nullable=True)

    pedido = db.relationship('Pedido', back_populates='itens')
    lanche = db.relationship('Lanche', back_populates='pedido_items')
    bebida = db.relationship('Bebida', back_populates='pedido_items')