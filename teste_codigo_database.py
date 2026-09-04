from datetime import datetime, timedelta, timezone
from app.services.codigo_verificacao_service import codigo_esta_expirado

from app.core.security import (
    gerar_codigo_verificacao, 
    gerar_hash_codigo,
    verificar_codigo,
)
from app.database import conectar_banco
from app.models.codigo_verificacao_model import(
    buscar_ultimo_codigo_nao_utilizado, 
    inserir_codigo_verificacao, 
    incrementar_tentativas,
    marcar_codigo_como_utilizado,
    )

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
assert registro["usuario_id"] == usuario["id"]
assert registro["tipo"] == "confirmacao_email"
assert registro["expira_em"] == expira_em
assert registro["utilizado"] == 0
assert registro["tentativas"] == 0
incrementar_tentativas(codigo_id)

registro_atualizado = buscar_ultimo_codigo_nao_utilizado(
    usuario_id=usuario["id"],
    tipo="confirmacao_email",
)

assert registro_atualizado is not None
assert registro_atualizado["id"] == codigo_id
assert registro_atualizado["tentativas"] == 1

assert verificar_codigo(codigo, registro["codigo_hash"])

assert not codigo_esta_expirado(registro["expira_em"])

data_expirada = (
    datetime.now(timezone.utc) - timedelta(minutes=10)
).isoformat()

assert codigo_esta_expirado(data_expirada)

marcar_codigo_como_utilizado(codigo_id)
with conectar_banco() as conexao:
    codigo_utilizado = conexao.execute(
        """
        SELECT utilizado
        FROM codigos_verificacao
        WHERE id = ?
        """,
        (codigo_id,),
    ).fetchone()

assert codigo_utilizado is not None
assert codigo_utilizado["utilizado"] == 1

print(f"Código original: {codigo}")
print(f"ID do registro: {codigo_id}")
print("Código armazenado e validado com sucesso.")
print("Validade do código verificada com sucesso.")
print("Tentativa incorreta registrada com sucesso.")
print("Código marcado como utilizado com sucesso.")

