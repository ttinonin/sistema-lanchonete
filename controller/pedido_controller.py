from repositories.pedidos_repository import PedidosRepository
from repositories.pedido_items_repository import PedidoItemsRepository
from models.pedido import Pedido
from models.pedido_items import PedidoItem
from decimal import Decimal
from datetime import datetime

class PedidoController:
    def __init__(self):
        self.repo = PedidosRepository()
        self.items_repo = PedidoItemsRepository()
    
    def criar(self, cliente_id: str, funcionario_id: str, valor: str, bebidas_id, lanches_id):
        if not cliente_id or not funcionario_id or not valor:
            raise ValueError("Preencher todos os campos!")
        
        pedido = Pedido(cliente_id=cliente_id, funcionario_id=funcionario_id, valor=Decimal(valor))
        self.repo.criar(pedido)

        for id in lanches_id:
            pedido_items = PedidoItem(pedido_id=pedido.id, lanche_id=id, bebida_id=None)
            self.items_repo.criar(pedido_items)

        for id in bebidas_id:
            pedido_items = PedidoItem(pedido_id=pedido.id, lanche_id=None, bebida_id=id)
            self.items_repo.criar(pedido_items)

        return pedido
    
    @staticmethod
    def calcular_tempo_estimado(valor_total: Decimal) -> int:
        """Calcula o tempo estimado de entrega com base no valor do pedido"""
        if valor_total < Decimal('50.00'):
            return 30
        elif valor_total <= Decimal('100.00'):
            return 45
        else:
            return 60
        
    @staticmethod
    def calcular_pontos(cliente_id: str, valor_total: Decimal) -> int:
        """Calcula a quantidade de pontos de fidelidade com base no valor total do pedido"""
        return int(valor_total // Decimal('10.00'))

    @staticmethod
    def verificar_entrega_gratis(valor_total: Decimal) -> bool:
        """Verifica se o pedido tem direito à entrega grátis"""
        return valor_total >= Decimal('100.00')


    @staticmethod
    def calcular_desconto(valor_original, percentual_desconto):
        desconto = valor_original * (percentual_desconto / 100)
        return valor_original - desconto

    @staticmethod
    def calcular_taxa_entrega(valor_total):
        if valor_total > 150.00:
            return 0
        else:
            return 15.00

    def buscar_pedido_items(self, id):
        return self.items_repo.buscar_por_pedido_id(id)

    def buscar(self, id):
        return self.repo.buscar_por_id(id)

    def listar(self):
        return self.repo.listar()
    
    def deletar(self, id: int):
        return self.repo.deletar(id)