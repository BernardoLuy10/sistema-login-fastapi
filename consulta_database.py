from database import buscar_usuario_por_email, listar_usuarios
email_procurado = "bernardo@gmail.com.br"
usuario = buscar_usuario_por_email(email_procurado)
if usuario is not None:
    print("Usuário encontrado:")
    print(f"ID: {usuario[0]}")
    print(f"Nome: {usuario[1]}")
    print(f"Email: {usuario[2]}")
    print(f"Email confirmado: {usuario[3]}")
    print(f"Criado em: {usuario[4]}")
else:
    print("Usuário não encontrado.")

print("\nLista de todos os usuários:")
usuarios = listar_usuarios()
for usuario in usuarios:
    print(usuario)