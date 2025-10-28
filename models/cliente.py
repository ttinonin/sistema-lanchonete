from datetime import datetime
from . import db

class Cliente(db.Model):
    __tablename__ = 'clientes'

    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String, nullable=False)
    endereco = db.Column(db.String, nullable=False)
    telefone = db.Column(db.String, nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.now)

    pedido_items = db.relationship('PedidoItem', back_populates='bebida')