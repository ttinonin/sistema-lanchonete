from datetime import datetime
from . import db

class Funcionario(db.Model):
    __tablename__ = 'funcionarios'

    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String, nullable=False)
    email = db.Column(db.String, nullable=False)
    senha = db.Column(db.String, nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.now)

    pedido_items = db.relationship('PedidoItem', back_populates='bebida')