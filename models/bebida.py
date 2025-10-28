from datetime import datetime
from . import db

class Bebida(db.Model):
    __tablename__ = 'bebidas'

    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String, nullable=False)
    preco = db.Column(db.Numeric(10, 2), nullable=False)
    litragem = db.Column(db.Integer, nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.now)

    pedido_items = db.relationship('PedidoItem', back_populates='bebida')