from fastapi import FastAPI
from app.views.usuario_view import router as usuario_router




"""FastAPI é a classe principal da biblioteca.
app = FastAPI() cria uma instância da aplicação.
@app.get("/") associa uma requisição GET / à função seguinte.
O @app.get() é um decorador. Ele registra a função como responsável por determinada rota.
http://127.0.0.1:8000/docs
"""
app = FastAPI()

app.include_router(usuario_router) #Inclui o roteador de usuários na aplicação FastAPI, permitindo que as rotas definidas em usuario_view.py sejam acessíveis.

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


