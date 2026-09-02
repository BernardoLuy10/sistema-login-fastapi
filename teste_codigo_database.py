from datetime import datetime, timedelta, timezone

from app.core.security import (
    gerar_codigo_verificacao, 
    gerar_hash_codigo,
    verificar_codigo,
)
from app.database import conectar_banco
from app.models.codigo_verificacao_model import(buscar_ultimo_codigo_nao_utilizado, inserir_codigo_verificacao)

with conectar_banco() as conexao:
    usuario = conexao.execute(
        """
        SELECT id 
        FROM usuarios
        ORDER BY id
        LIMIT 1
        """
    ).fetchone()

assert usuario is not None, "Cadastre pelo menos um usuário antes do teste"

codigo = gerar_codigo_verificacao()
codigo_hash = gerar_hash_codigo(codigo)

expira_em =(
    datetime.now(timezone.utc) + timedelta(minutes=10)
).isoformat()

codigo_id = inserir_codigo_verificacao(
    usuario_id=usuario["id"],
    codigo_hash=codigo_hash,
    tipo="confirmacao_email",
    expira_em=expira_em,
)

registro = buscar_ultimo_codigo_nao_utilizado(
    usuario_id=usuario["id"],
    tipo="confirmacao_email",
)

assert registro is not None
assert registro["id"] == codigo_id

assert registro is not None
assert registro["usuario_id"] == usuario["id"]
assert registro["tipo"] == "confirmacao_email"
assert registro["expira_em"] == expira_em
assert registro["utilizado"] == 0
assert registro["tentativas"] == 0
assert verificar_codigo(codigo, registro["codigo_hash"])

print(f"Código original: {codigo}")
print(f"ID do registro: {codigo_id}")
print(f"Codigo armazenado e validado com sucesso.")

