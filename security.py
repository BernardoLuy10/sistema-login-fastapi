from pwdlib import PasswordHash

gerenciador_senhas = PasswordHash.recommended()

def gerar_hash_senha(senha: str) -> str:
    return gerenciador_senhas.hash(senha)

def verificar_senha(senha: str, senha_hash: str) -> bool:
    return gerenciador_senhas.verify(senha, senha_hash)