# Relatorio de Testes

## Resumo Geral

Todos os testes executados foram aprovados

| Teste      | Casos Executados | Casos Aprovados |
| ----------- | ----------- | ---------- |
| Unitario      |   35    | 35 |
| Integracao   |  24    | 24 |
| Funcional   | 8 | 8 |
| Total   | 67 |  |

## Detalhamento de Testes

### Principais testes unitarios

| Teste      | Resultado | Observacao |
| ----------- | ----------- | ---------- |
| Criar Lanche      |   Aprovado    | Modelo cria os dados de forma correta |
| Buscar pedido por id   |  Aprovado    | Modeo realiza buscas com dados mocks |
| Atualizar funcionario   | Aprovado | Modelo atualiza todos os dados de funcionarios |

### Principais testes de integracao

| Teste      | Resultado | Observacao |
| ----------- | ----------- | ---------- |
| Criar Bebida      |   Aprovado    | Repositorio cria dados no banco com sucesso |
| Buscar cliente por id   |  Aprovado    | Repositorio busca dados escritos no banco |
| Atualizar funcionario   | Aprovado | Repositorio atualiza todos os dados de funcionarios e os reescrevem no banco |
| Deletar funcionario com id invalido gera erro   | Aprovado | Repositorio lanca uma excessao com sucesso |

### Principais testes funcioanis

| Teste      | Resultado | Observacao |
| ----------- | ----------- | ---------- |
| Calcular pedido sem desconto      |   Aprovado    | O valor permanece o mesmo sem aplicar o desconto |
| Calcular taxa de entrega gratis   |  Aprovado    | Valor da taxa esta zerado |
| Calcular tempo estimado para entrega   | Aprovado | O tempo para entrega varia conforme o valor do pedido |