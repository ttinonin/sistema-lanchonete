from datetime import datetime
from . import db

class Pedido(db.Model):
    __tablename__ = 'pedidos'

    id = db.Column(db.Integer, primary_key=True)
    cliente_id = db.Column(db.Integer, db.ForeignKey('clientes.id', ondelete='CASCADE', onupdate='CASCADE'), nullable=False)
    funcionario_id = db.Column(db.Integer, db.ForeignKey('funcionarios.id', ondelete='SET NULL', onupdate='CASCADE'), nullable=True)
    valor = db.Column(db.Numeric(10, 2))
    created_at = db.Column(db.DateTime, default=datetime.now)

    cliente = db.relationship('Cliente', back_populates='pedidos')
    funcionario = db.relationship('Funcionario', back_populates='pedidos')
    itens = db.relationship('PedidoItem', back_populates='pedido', cascade='all, delete-orphan')