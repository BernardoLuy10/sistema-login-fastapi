from database import buscar_usuario_para_autenticacao
from security import verificar_senha

email_informado = "hash@gmail.combr"
senha_informada = "senha123"

usuario = buscar_usuario_para_autenticacao(email_informado)

if usuario is None:
    print("E-mail ou senha inválidos.")
else:
    senha_valida = verificar_senha(senha_informada, usuario['senha_hash'])
    if senha_valida:
        print(f"Senha válida para o usuário {usuario['nome']}.")
    else:
        print("E-mail ou senha inválidos.")
