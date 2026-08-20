from app.models.usuario_model import inserir_usuario
from app.database import criar_tabela
from app.core.security import gerar_hash_senha

criar_tabela()

senha_original = "senha123"
senha_hash = gerar_hash_senha(senha_original)

usuario_id = inserir_usuario(
    nome="user_hash",
    email="hash@gmail.combr",
    senha_hash=senha_hash
)

print(f"Usuario criado com ID: {usuario_id}")