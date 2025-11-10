# Plano de Testes de Software

## Projeto

- Nome do sistema: Sistema para gerenciamento de lanchonete
- Versao: 1.0

## Objetivo dos testes

Assegurar a qualidade do sistema, garantindo sua funcionalidade por meio da execução de testes unitários, de integração e funcionais.

## Escopo dos Testes

- Funcionalidades CRUD
- Testes de integracao entre módulos (banco de dados e backend)
- Testes de excecoes

## Itens a serem testados

| Modulo      | Descricao |
| ----------- | ----------- |
| Controladores      |  Módulo responsável por integrar modelos, repositórios e serviços.      |
| Repositorios   | Módulo responsável pela conexão com o banco de dados e execução das operações CRUD.        |
| Modelos   | Responsável por definir a estrutura dos dados a serem transferidos entre o backend e o frontend. |

## Estrategia de Testes

- Nivel de Testes: Unitario -> Integracao -> Funcionais
- Abordagem: Manual utilizando pytest
- Ambiente: Linux para servidor e firefox como client

## Criterios de Aceitacao

- 80% de cobertura de testes
- Nenhum Runtime Error em producao

## Cronograma

| Etapa      | Data de inicio | Data de fim |
| ----------- | ----------- | ---------- |
| Planejamento      |    27/10/2025    | 28/10/2025 |
| Criacao de testes unitarios   |  28/10/2025    | 30/10/2025 |
| Criacao de testes de integracao   | 03/11/2025 | 06/11/205 |
| Criacao de testes de funcionais   | 07/11/2025 | 09/11/205 |