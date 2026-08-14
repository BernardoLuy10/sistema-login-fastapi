from fastapi import FastAPI
from pydantic import BaseModel, ConfigDict, EmailStr, Field


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

@app.post("/usuarios")
def cadastrar_usuario(usuario: CadastroUsuario):
    return{
        "mensagem": "Dados reecebidos com sucesso",
        "nome": usuario.nome,
        "email": usuario.email
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


