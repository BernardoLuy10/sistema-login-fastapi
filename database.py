import sqlite3
NOME_BANCO = "sistema_login.db"

def criar_tabela():
    with sqlite3.connect(NOME_BANCO) as conexao:
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

def inserir_usuario(nome: str, email: str, senha_hash: str):
    with sqlite3.connect(NOME_BANCO) as conexao:
        cursor = conexao.cursor()
        cursor.execute(
        
            """
            INSERT INTO usuarios (nome, email, senha_hash)
            VALUES (?, ?, ?)
            """,
            (nome, email, senha_hash) #valores a serem inseridos na tabela, dentro do comentário são as colunas onde esses dados serão inseridos 
            )
        conexao.commit()
        return cursor.lastrowid  # Retorna o ID do usuário inserido

def buscar_usuario_por_email(email: str):
    with sqlite3.connect(NOME_BANCO) as conexao: #aqui é feita a conexão com o banco de dados, utilizando o nome do banco definido na constante NOME_BANCO
        conexao.row_factory = sqlite3.Row
        cursor = conexao.cursor() #a função cursor() cria um objeto cursor que permite executar comandos SQL no banco de dados.
        cursor.execute( #Aqui executa-se a consulta SQL
            """
            SELECT id, nome, email, email_confirmado, criado_em
            FROM usuarios
            WHERE email = ?
            """,
            (email,) #Uma tupla com o valor do email a ser buscado. O uso da vírgula é necessário para criar uma tupla de um único elemento.
        )
        return cursor.fetchone()  # Retorna o usuário encontrado ou None se não existir

def listar_usuarios():
    with sqlite3.connect(NOME_BANCO) as conexao:
        conexao.row_factory = sqlite3.Row #Linhas retornadas como objetos do tipo Row, permitindo acesso aos dados por nome de coluna.
        cursor = conexao.cursor()
        cursor.execute(
            """
            SELECT id, nome, email, email_confirmado, criado_em
            FROM usuarios
            ORDER BY id
            """
        )
        return cursor.fetchall()

def buscar_usuario_para_autenticacao(email: str):#Função para buscar o usuário no banco de dados, incluindo a senha hash, para fins de autenticação.
    with sqlite3.connect(NOME_BANCO) as conexao:
        conexao.row_factory = sqlite3.Row
        cursor = conexao.cursor()
        cursor.execute(
            """
            SELECT id, nome, email, senha_hash, email_confirmado, criado_em
            FROM usuarios
            WHERE email = ?
            """,
            (email,)
        )
        return cursor.fetchone()
if __name__ =="__main__":
    criar_tabela()
    print("Banco de dados criado com sucesso!")

