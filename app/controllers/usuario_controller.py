import sqlite3
from app.core.security import gerar_hash_senha
from app.models.usuario_model import inserir_usuario

class EmailJaCadastradoError(Exception):
    pass

def cadastrar_novo_usuario(nome: str, email:str, senha:str):
    nome_normalizado = nome.strip()  #Normaliza o nome do usuário, removendo espaços em branco
    email_normalizado = email.strip().lower()  #Normaliza o email do usuário, removendo espaços em branco e convertendo para minúsculas.
    senha_hash = gerar_hash_senha(senha)

    try:
        usuario_id = inserir_usuario(
            nome=nome_normalizado,
            email=email_normalizado,
            senha_hash=senha_hash
        )
    except sqlite3.IntegrityError as erro:
        raise EmailJaCadastradoError from erro  #Lança uma exceção personalizada caso o email já esteja cadastrado no banco de dados.

    return {
        "mensagem": "Usuário cadastrado com sucesso.",
        "id": usuario_id,
        "nome": nome_normalizado,
        "email": email_normalizado
    }