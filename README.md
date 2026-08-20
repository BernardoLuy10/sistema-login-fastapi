# Sistema de Login com FastAPI

API REST de autenticação em desenvolvimento com Python, FastAPI e SQLite. O projeto está sendo construído para estudar, passo a passo, o funcionamento de cadastro de usuários, persistência de dados, autenticação, confirmação de e-mail e recuperação de senha.

## Status do projeto

Em desenvolvimento.

## Funcionalidades implementadas

- Criação de rotas com FastAPI;
- Validação de dados com Pydantic;
- Criação do banco de dados SQLite;
- Criação da tabela de usuários;
- Cadastro de usuários integrado à API;
- Hash seguro de senhas com Argon2;
- Verificação de senhas;
- Restrição de e-mail único;
- Tratamento de e-mail duplicado;
- Consulta de usuário por e-mail;
- Listagem de usuários cadastrados;
- Organização inicial em arquitetura MVC;
- Separação das camadas Model, View, Controller, Schema e Core.

## Funcionalidades planejadas

- Confirmação de e-mail por código;
- Login e autenticação com token;
- Recuperação e alteração de senha;
- Testes automatizados.

## Tecnologias utilizadas

- Python;
- FastAPI;
- Pydantic;
- SQLite;
- Git e GitHub.

## Como executar
Crie e ative um ambiente virtual:

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1

Instale as dependências:

```powershell
python -m pip install -r requirements.txt
```

Crie as tabelas do banco:

```powershell
python -m app.database
```

Execute a API:

```powershell
fastapi dev app/main.py
```

Acesse a documentação interativa:

```text
http://127.0.0.1:8000/docs
```