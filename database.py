import sqlite3

def conectar():
    conexao = sqlite3.connect("chamados.db")
    return conexao

def criar_tabela():
    conexao = conectar()
    cursor = conexao.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS chamados (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            codigo TEXT NOT NULL UNIQUE,
            categoria TEXT NOT NULL,
            prioridade TEXT NOT NULL,
            descricao TEXT NOT NULL,
            status TEXT NOT NULL
        )
    """)
def adicionar_chamado(codigo, categoria, prioridade, descricao, status):
    conexao = conectar()
    cursor = conexao.cursor()

    cursor.execute("""
        INSERT INTO chamados
        (codigo, categoria, prioridade, descricao, status)
        VALUES (?, ?, ?, ?, ?)
    """, (codigo, categoria, prioridade, descricao, status))

    conexao.commit()
    conexao.close()
   
def listar_chamados():
    conexao = conectar()
    cursor = conexao.cursor()

    cursor.execute("""
        SELECT id, codigo, categoria, prioridade, descricao, status
        FROM chamados
    """)

    chamados = cursor.fetchall()

    conexao.close()
    return chamados
   
def buscar_por_status(status):
    conexao = conectar()
    cursor = conexao.cursor()

    cursor.execute("""
        SELECT id, codigo, categoria, prioridade, descricao, status
        FROM chamados
        WHERE LOWER(status) = LOWER(?)
    """, (status,))

    chamados = cursor.fetchall()

    conexao.close()
    return chamados
 
def atualizar_status(codigo, novo_status):
    conexao = conectar()
    cursor = conexao.cursor()

    cursor.execute("""
        UPDATE chamados
        SET status = ?
        WHERE codigo = ?
    """, (novo_status, codigo))

    conexao.commit()
    conexao.close()   
    
def listar_por_prioridade():
    conexao = conectar()
    cursor = conexao.cursor()

    cursor.execute("""
        SELECT id, codigo, categoria, prioridade, descricao, status
        FROM chamados
        ORDER BY
            CASE prioridade
                WHEN 'Alta' THEN 1
                WHEN 'Média' THEN 2
                WHEN 'Baixa' THEN 3
                ELSE 4
            END
    """)

    chamados = cursor.fetchall()

    conexao.close()
    return chamados
   
def excluir_chamado(codigo):
    conexao = conectar()
    cursor = conexao.cursor()

    cursor.execute("""
        DELETE FROM chamados
        WHERE codigo = ?
    """, (codigo,))

    conexao.commit()
    conexao.close()
   
if __name__ == "__main__":
    criar_tabela()


    for chamado in listar_chamados():
        print(chamado)  


def listar_por_codigo(ordem="ASC"):
    conexao = conectar()
    cursor = conexao.cursor()

    if ordem == "DESC":
        consulta = """
            SELECT id, codigo, categoria, prioridade, descricao, status
            FROM chamados
            ORDER BY codigo DESC
        """
    else:
        consulta = """
            SELECT id, codigo, categoria, prioridade, descricao, status
            FROM chamados
            ORDER BY codigo ASC
        """

    cursor.execute(consulta)

    chamados = cursor.fetchall()

    conexao.close()
    return chamados


def buscar_por_prioridade(prioridade):
    conexao = conectar()
    cursor = conexao.cursor()

    cursor.execute("""
        SELECT id, codigo, categoria, prioridade, descricao, status
        FROM chamados
        WHERE LOWER(prioridade) = LOWER(?)
    """, (prioridade.strip(),))

    chamados = cursor.fetchall()

    conexao.close()
    return chamados


def buscar_por_status_e_prioridade(status, prioridade):
    conexao = conectar()
    cursor = conexao.cursor()

    cursor.execute("""
        SELECT id, codigo, categoria, prioridade, descricao, status
        FROM chamados
        WHERE LOWER(status) = LOWER(?)
        AND LOWER(prioridade) = LOWER(?)
    """, (status.strip(), prioridade.strip()))

    chamados = cursor.fetchall()

    conexao.close()
    return chamados


def buscar_por_status_ou_prioridade(status, prioridade):
    conexao = conectar()
    cursor = conexao.cursor()

    cursor.execute("""
        SELECT id, codigo, categoria, prioridade, descricao, status
        FROM chamados
        WHERE LOWER(status) = LOWER(?)
        OR LOWER(prioridade) = LOWER(?)
    """, (status.strip(), prioridade.strip()))

    chamados = cursor.fetchall()

    conexao.close()
    return chamados


def buscar_por_categoria(categoria):
    conexao = conectar()
    cursor = conexao.cursor()

    cursor.execute("""
        SELECT id, codigo, categoria, prioridade, descricao, status
        FROM chamados
        WHERE LOWER(categoria) = LOWER(?)
    """, (categoria.strip(),))

    chamados = cursor.fetchall()

    conexao.close()
    return chamados

def buscar_por_categoria_e_prioridade(categoria, prioridade):
    conexao = conectar()
    cursor = conexao.cursor()

    cursor.execute("""
        SELECT id, codigo, categoria, prioridade, descricao, status
        FROM chamados
        WHERE LOWER(categoria) = LOWER(?)
        AND LOWER(prioridade) = LOWER(?)
    """, (categoria.strip(), prioridade.strip()))

    chamados = cursor.fetchall()

    conexao.close()
    return chamados


