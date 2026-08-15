# Sistema de Login com FastAPI

API REST de autenticação em desenvolvimento com Python, FastAPI e SQLite. O projeto está sendo construído para estudar, passo a passo, o funcionamento de cadastro de usuários, persistência de dados, autenticação, confirmação de e-mail e recuperação de senha.

## Status do projeto

Em desenvolvimento.

## Funcionalidades implementadas

- Criação de rotas com FastAPI;
- Validação de dados com Pydantic;
- Criação do banco de dados SQLite;
- Criação da tabela de usuários;
- Cadastro de usuários diretamente no banco;
- Restrição de e-mail único;
- Consulta de usuário por e-mail;
- Listagem de usuários cadastrados.

## Funcionalidades planejadas

- Hash seguro de senhas;
- Integração da rota de cadastro com o banco;
- Tratamento de erros da API;
- Organização em arquitetura MVC;
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