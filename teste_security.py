from app.core.security import gerar_hash_senha, verificar_senha

senha_teste = "senha123"
senha_hash = gerar_hash_senha(senha_teste)

print(f"Hash gerado: {senha_hash}")

senha_correta = verificar_senha("senha123", senha_hash)
senha_incorreta = verificar_senha("senhateste", senha_hash)

print(f"Senha correta: {senha_correta}")
print(f"Senha incorreta: {senha_incorreta}")
