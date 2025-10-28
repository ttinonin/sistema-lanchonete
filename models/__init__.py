from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

from .cliente import Cliente
from .funcionario import Funcionario
from .lanche import Lanche
from .bebida import Bebida
from .pedido import Pedido
from .pedido_items import PedidoItem