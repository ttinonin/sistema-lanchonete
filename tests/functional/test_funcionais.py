import pytest
from controller.pedido_controller import PedidoController
from datetime import datetime
from decimal import Decimal

def test_calcular_sem_desconto():
    valor_original = 100
    resultado = PedidoController.calcular_desconto(valor_original, 0)
    assert resultado == valor_original

def test_calcular_com_desconto():
    valor_original = 100
    resultado = PedidoController.calcular_desconto(valor_original, 10)
    valor_esperado = valor_original - (valor_original * (10 / 100))
    assert resultado == valor_esperado

def test_calcular_taxa_entrega_gratis():
    valor_total = 200.00
    resultado = PedidoController.calcular_taxa_entrega(valor_total)
    assert resultado == 0.00

def test_calcular_taxa_entrega_com_taxa():
    valor_total = 100.00
    resultado = PedidoController.calcular_taxa_entrega(valor_total)
    assert resultado == 15.00

def test_calcular_taxa_entrega_com_valor_exato():
    valor_total = 150.00
    resultado = PedidoController.calcular_taxa_entrega(valor_total)
    assert resultado == 15.00

def test_calcular_tempo_estimado():
    assert PedidoController.calcular_tempo_estimado(Decimal('30.00')) == 30
    assert PedidoController.calcular_tempo_estimado(Decimal('75.00')) == 45
    assert PedidoController.calcular_tempo_estimado(Decimal('150.00')) == 60

def test_calcular_pontos():
    assert PedidoController.calcular_pontos('cliente_1', Decimal('99.99')) == 9
    assert PedidoController.calcular_pontos('cliente_2', Decimal('150.00')) == 15

def test_verificar_entrega_gratis():
    valor_total = Decimal('150.00')
    resultado = PedidoController.verificar_entrega_gratis(valor_total)
    assert resultado is True

    valor_total = Decimal('99.99')
    resultado = PedidoController.verificar_entrega_gratis(valor_total)
    assert resultado is False
