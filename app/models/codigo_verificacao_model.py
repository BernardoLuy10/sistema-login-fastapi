from app.database import conectar_banco
def inserir_codigo_verificacao(
        usuario_id: int,
        codigo_hash: str,
        tipo: str,
        expira_em: str,
) -> int:
    with conectar_banco() as conexao:
        cursor = conexao.cursor() 
        cursor.execute(
            """
            INSERT INTO codigos_verificacao(
                usuario_id,
                codigo_hash,
                tipo,
                expira_em
            )
            VALUES (?, ?, ?, ?)
            """,
            (usuario_id, codigo_hash, tipo, expira_em),
        )
        conexao.commit()
        return cursor.lastrowid