from pwdlib import PasswordHash
import secrets

gerenciador_senhas = PasswordHash.recommended()

def gerar_hash_senha(senha: str) -> str:
    return gerenciador_senhas.hash(senha)

def verificar_senha(senha: str, senha_hash: str) -> bool:
    return gerenciador_senhas.verify(senha, senha_hash)

def gerar_codigo_verificacao() -> str:
    numero = secrets.randbelow(1_000_000)
    return f"{numero:06d}"

def gerar_hash_codigo(codigo: str) -> str:
    return gerenciador_senhas.hash(codigo)

def verificar_codigo(codigo: str, codigo_hash: str) -> bool:
    return gerenciador_senhas.verify(codigo, codigo_hash)