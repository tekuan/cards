# CRUD Deck of Cards

Este projeto implementa operações básicas (CRUD) com um baralho de cartas utilizando a API Deck of Cards.

## Instalação

Para instalar as dependências do projeto, utilize o comando na pasta do projeto:

```bash
pip install -r requirements.txt
```

## Migrações

Antes de executar o script principal, é necessário aplicar as migrações que configuram o ambiente de banco de dados SQLite3. Utilize o seguinte comando para isso:

```bash
python migrate.py
```

## Script Principal

Para a execução do script principal, dentro da pasta app:

```bash
python main.py
```

### Testes

Os testes foram implementados usando o pytest. Para executar os testes, utilize:

```bash
python -m pytest
```