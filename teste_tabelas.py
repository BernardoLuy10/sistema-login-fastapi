from app.database import conectar_banco

with conectar_banco() as conexao:
    tabelas=conexao.execute(
        """
        SELECT name
        FROM sqlite_master
        WHERE type = 'table'
        ORDER BY name
        """
    ).fetchall()

for tabela in tabelas:
    print(tabela["name"])