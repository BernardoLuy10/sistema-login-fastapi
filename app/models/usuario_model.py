from app.database import conectar_banco

def inserir_usuario(nome: str, email: str, senha_hash: str):
    with conectar_banco() as conexao:
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
    with conectar_banco() as conexao: #aqui é feita a conexão com o banco de dados, utilizando o nome do banco definido na constante NOME_BANCO
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
    with conectar_banco() as conexao:
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
    with conectar_banco() as conexao:
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