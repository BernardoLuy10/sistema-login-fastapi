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

def buscar_ultimo_codigo_verificacao(
        usuario_id: int,
        tipo: str,
):
    with conectar_banco() as conexao:
        cursor = conexao.cursor()
        cursor.execute(
            """
            SELECT
                id,
                usuario_id,
                codigo_hash,
                tipo,
                expira_em,
                utilizado,
                tentativas,
                criado_em
            FROM codigos_verificacao
            WHERE usuario_id = ?
                AND tipo = ?
            ORDER BY id DESC
            LIMIT 1
            """,
            (usuario_id, tipo)
        )
        return cursor.fetchone()
    
def incrementar_tentativas(codigo_id: int) -> None:
    with conectar_banco() as conexao:
        cursor = conexao.cursor()
        cursor.execute(
            """
            UPDATE codigos_verificacao
            SET tentativas = tentativas + 1
            WHERE id = ?
            """,
            (codigo_id,),
        )
        conexao.commit()

def marcar_codigo_como_utilizado(codigo_id: int) -> None:
    with conectar_banco() as conexao:
        cursor = conexao.cursor()
        cursor.execute(
            """
            UPDATE codigos_verificacao
            SET utilizado = 1
            WHERE id = ?
            """,
            (codigo_id,),
        )
        conexao.commit()