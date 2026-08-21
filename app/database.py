import sqlite3


NOME_BANCO = "sistema_login.db"


def conectar_banco():
    conexao = sqlite3.connect(NOME_BANCO)

    # Permite acessar os valores retornados pelo nome da coluna.
    conexao.row_factory = sqlite3.Row

    # Ativa a validação dos relacionamentos entre tabelas.
    conexao.execute("PRAGMA foreign_keys = ON")

    return conexao


def criar_tabelas():
    with conectar_banco() as conexao:
        cursor = conexao.cursor()

        cursor.execute(
            """
            CREATE TABLE IF NOT EXISTS usuarios (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                nome TEXT NOT NULL,
                email TEXT UNIQUE NOT NULL,
                senha_hash TEXT NOT NULL,
                email_confirmado INTEGER NOT NULL DEFAULT 0
                    CHECK (email_confirmado IN (0, 1)),
                criado_em TEXT NOT NULL DEFAULT CURRENT_TIMESTAMP
            )
            """
        )

        cursor.execute(
            """
            CREATE TABLE IF NOT EXISTS codigos_verificacao (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                usuario_id INTEGER NOT NULL,
                codigo_hash TEXT NOT NULL,
                tipo TEXT NOT NULL CHECK (
                    tipo IN ('confirmacao_email', 'recuperacao_senha')
                ),
                expira_em TEXT NOT NULL,
                utilizado INTEGER NOT NULL DEFAULT 0
                    CHECK (utilizado IN (0, 1)),
                tentativas INTEGER NOT NULL DEFAULT 0
                    CHECK (tentativas >= 0),
                criado_em TEXT NOT NULL DEFAULT CURRENT_TIMESTAMP,
                FOREIGN KEY (usuario_id)
                    REFERENCES usuarios(id)
                    ON DELETE CASCADE
            )
            """
        )


if __name__ == "__main__":
    criar_tabelas()
    print("Banco de dados e tabelas criados com sucesso!")