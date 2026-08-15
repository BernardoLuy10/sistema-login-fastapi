from fastapi import FastAPI
from pydantic import BaseModel, ConfigDict, EmailStr, Field
import sqlite3
from fastapi import FastAPI, HTTPException, status
from database import inserir_usuario
from security import gerar_hash_senha



"""FastAPI é a classe principal da biblioteca.
app = FastAPI() cria uma instância da aplicação.
@app.get("/") associa uma requisição GET / à função seguinte.
O @app.get() é um decorador. Ele registra a função como responsável por determinada rota.
http://127.0.0.1:8000/docs
"""
app = FastAPI()

class CadastroUsuario(BaseModel):
    model_config = ConfigDict(extra="forbid") #Regra de validação para impedir que campos extras sejam enviados na requisição.
    nome: str = Field(min_length = 3, max_length = 50) #Regra de validação para o campo nome, que deve ter no mínimo 3 e no máximo 50 caracteres.
    email: EmailStr #Regra de validação para o campo email, que deve ser um email válido.
    senha: str = Field(min_length = 4, max_length = 12) #Regra de validação para o campo senha, que deve ter no mínimo 4 e no máximo 12 caracteres.

@app.post("/usuarios", status_code=status.HTTP_201_CREATED)
def cadastrar_usuario(usuario: CadastroUsuario):
    nome = usuario.nome.strip() #Remove espaços em branco no início e no final do nome.
    email = str(usuario.email).strip().lower()
    senha_hash = gerar_hash_senha(usuario.senha) #Gera o hash da senha informada.

    try:
        usuario_id = inserir_usuario(
            nome=nome,
            email=email,
            senha_hash=senha_hash
        )
    except sqlite3.IntegrityError:
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT,
            detail="E-mail já cadastrado."
        )
    return{
        "mensagem": "Usuário cadastrado com sucesso.",
        "id": usuario_id,
        "nome": nome,
        "email": email
    }

@app.get("/")
def inicio():
    return {"mensagem": "Sistema de login em desenvolvimento"}

@app.get("/status")
def get_status():
    status = "Online"
    return {"Sistema": status}

@app.get("/saudacao/{nome}")
def get_saudacao(nome: str):
    return {"mensagem": f"Olá, {nome}"}

@app.get("/soma")
def get_soma(a:int, b:int):
    return {"resultado": a+b}


