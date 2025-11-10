# Sistema para lanchone

Este e um sistema desenvolvido em Flask, para a materia de Simulacao e Teste de Software, utilizando a biblioteca pytest para realizacao dos testes unitarios, integracao e funcionais.

## Instalacao

Crie um ambiente virtual

```bash
python3 -m venv venv
```

Ative o ambiente virtual

```bash
source ./venv/bin/activate
```

Instale as dependencias

```bash
pip install -r reqirements.txt
```

Inicie o servidor

```bash
python3 main.py
```

## Executando testes

Para executar apenas os testes

```bash
pytest ./tests/
```

Para executar testes e gerar relatorio 

```bash
pytest --cov=. --cov-report=html
```