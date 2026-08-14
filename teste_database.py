from database import criar_tabela, inserir_usuario

criar_tabela()

usuario_id = inserir_usuario(
    nome="Kenndra",
    email="kwb@gmail.combr",
    senha_hash="hash_da_senha"
)

print(f"Usuario criado com ID: {usuario_id}")