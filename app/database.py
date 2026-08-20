import sqlite3
NOME_BANCO = "sistema_login.db"

def conectar_banco():
    conexao = sqlite3.connect(NOME_BANCO)
    conexao.row_factory = sqlite3.Row # Linhas retornadas como objetos do tipo Row, permitindo acesso aos dados por nome de coluna.
    return conexao

def criar_tabela():
    with conectar_banco() as conexao:
        cursor = conexao.cursor()
        #Abaixo estão as colunas do banco de dados, com suas respectivas regras de validação, 
        # email_confirmado é um campo booleano, que indica se o email do usuário foi confirmado ou não através de 0 ou 1
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS usuarios (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                nome TEXT NOT NULL,
                email TEXT UNIQUE NOT NULL,
                senha_hash TEXT NOT NULL,
                email_confirmado INTEGER NOT NULL DEFAULT 0, 
                criado_em TEXT NOT NULL DEFAULT CURRENT_TIMESTAMP
            )
            """
        )

if __name__ =="__main__":
    criar_tabela()
    print("Banco de dados criado com sucesso!")

