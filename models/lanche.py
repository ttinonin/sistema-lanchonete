from datetime import datetime
from . import db

class Lanche(db.Model):
    __tablename__ = 'lanches'

    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String, nullable=False)
    preco = db.Column(db.Numeric(10, 2), nullable=False)
    descricao = db.Column(db.String)
    created_at = db.Column(db.DateTime, default=datetime.now)

    pedido_items = db.relationship('PedidoItem', back_populates='lanche')