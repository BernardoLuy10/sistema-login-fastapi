from app.models.usuario_model import buscar_usuario_por_email, listar_usuarios
email_procurado = "bernardo@gmail.com.br"
usuario = buscar_usuario_por_email(email_procurado)
if usuario is not None:
    print("Usuário encontrado:")
    print(f"ID: {usuario['id']}")#Nome da coluna que é retornada pelo banco de dados, que é acessada como um dicionário.
    print(f"Nome: {usuario['nome']}")
    print(f"Email: {usuario['email']}")
    print(f"Email confirmado: {usuario['email_confirmado']}")
    print(f"Criado em: {usuario['criado_em']}")
else:
    print("Usuário não encontrado.")

print("\nLista de todos os usuários:")
usuarios = listar_usuarios()
for usuario in usuarios:
    print(dict(usuario))