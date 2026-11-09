from datetime import datetime
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
            status TEXT NOT NULL,
            data_abertura TEXT,
            data_atualizacao TEXT,
            data_fechamento TEXT
        )
    """)

    conexao.commit()
    conexao.close()
    
    
def migrar_colunas_datas():
    conexao = conectar()
    cursor = conexao.cursor()

    cursor.execute("PRAGMA table_info(chamados)")
    colunas = {coluna[1] for coluna in cursor.fetchall()}

    if "data_abertura" not in colunas:
        cursor.execute("""
            ALTER TABLE chamados
            ADD COLUMN data_abertura TEXT
        """)

    if "data_atualizacao" not in colunas:
        cursor.execute("""
            ALTER TABLE chamados
            ADD COLUMN data_atualizacao TEXT
        """)

    if "data_fechamento" not in colunas:
        cursor.execute("""
            ALTER TABLE chamados
            ADD COLUMN data_fechamento TEXT
        """)

    conexao.commit()
    conexao.close()    
    
def adicionar_chamado(codigo, categoria, prioridade, descricao, status):
    conexao = conectar()
    cursor = conexao.cursor()

    data_hora = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    cursor.execute("""
        INSERT INTO chamados
        (
            codigo,
            categoria,
            prioridade,
            descricao,
            status,
            data_abertura,
            data_atualizacao
        )
        VALUES (?, ?, ?, ?, ?, ?, ?)
    """, (
        codigo,
        categoria,
        prioridade,
        descricao,
        status,
        data_hora,
        data_hora
    ))

    conexao.commit()
    conexao.close()    
    
    
def atualizar_status(codigo, novo_status):
    conexao = conectar()
    cursor = conexao.cursor()

    data_hora = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    if novo_status.lower() == "fechado":
        cursor.execute("""
            UPDATE chamados
            SET status = ?,
                data_atualizacao = ?,
                data_fechamento = ?
            WHERE codigo = ?
        """, (
            novo_status,
            data_hora,
            data_hora,
            codigo
        ))

    else:
        cursor.execute("""
            UPDATE chamados
            SET status = ?,
                data_atualizacao = ?,
                data_fechamento = NULL
            WHERE codigo = ?
        """, (
            novo_status,
            data_hora,
            codigo
        ))

    conexao.commit()
    conexao.close()
   
def listar_chamados():
    conexao = conectar()
    cursor = conexao.cursor()

    cursor.execute("""
       SELECT
    id,
    codigo,
    categoria,
    prioridade,
    descricao,
    status,
    data_abertura,
    data_atualizacao,
    data_fechamento
FROM chamados
    """)

    chamados = cursor.fetchall()

    conexao.close()
    return chamados
   
def buscar_por_status(status):
    conexao = conectar()
    cursor = conexao.cursor()

    cursor.execute("""
        SELECT id, codigo, categoria, prioridade, descricao, status, data_abertura, data_atualizacao, data_fechamento
        FROM chamados
        WHERE LOWER(status) = LOWER(?)
    """, (status,))

    chamados = cursor.fetchall()

    conexao.close()
    return chamados
 
    
def listar_por_prioridade():
    conexao = conectar()
    cursor = conexao.cursor()

    cursor.execute("""
        SELECT id, codigo, categoria, prioridade, descricao, status, data_abertura, data_atualizacao, data_fechamento
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
   
def listar_por_codigo(ordem="ASC"):
    conexao = conectar()
    cursor = conexao.cursor()

    if ordem == "DESC":
        consulta = """
            SELECT id, codigo, categoria, prioridade, descricao, status, data_abertura, data_atualizacao, data_fechamento
            FROM chamados
            ORDER BY codigo DESC
        """
    else:
        consulta = """
            SELECT id, codigo, categoria, prioridade, descricao, status, data_abertura, data_atualizacao, data_fechamento
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
        SELECT id, codigo, categoria, prioridade, descricao, status, data_abertura, data_atualizacao, data_fechamento
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
        SELECT id, codigo, categoria, prioridade, descricao, status, data_abertura, data_atualizacao, data_fechamento
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
        SELECT id, codigo, categoria, prioridade, descricao, status, data_abertura, data_atualizacao, data_fechamento
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
        SELECT id, codigo, categoria, prioridade, descricao, status, data_abertura, data_atualizacao, data_fechamento
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
        SELECT id, codigo, categoria, prioridade, descricao, status, data_abertura, data_atualizacao, data_fechamento
        FROM chamados
        WHERE LOWER(categoria) = LOWER(?)
        AND LOWER(prioridade) = LOWER(?)
    """, (categoria.strip(), prioridade.strip()))

    chamados = cursor.fetchall()

    conexao.close()
    return chamados


def buscar_por_descricao(termo):
    conexao = conectar()
    cursor = conexao.cursor()

    cursor.execute("""
        SELECT id, codigo, categoria, prioridade, descricao, status, data_abertura, data_atualizacao, data_fechamento
        FROM chamados
        WHERE LOWER(descricao) LIKE LOWER(?)
    """, (f"%{termo.strip()}%",))

    chamados = cursor.fetchall()

    conexao.close()
    return chamados


def buscar_por_descricao_e_status(termo,status):
    conexao = conectar()
    cursor = conexao.cursor()

    cursor.execute("""
        SELECT id, codigo, categoria, prioridade, descricao, status, data_abertura, data_atualizacao, data_fechamento
        FROM chamados
        WHERE LOWER(descricao) LIKE LOWER(?)
        AND LOWER(status) = LOWER(?)
    """, (f"%{termo.strip()}%", status.strip()))

    chamados = cursor.fetchall()

    conexao.close()
    return chamados

if __name__ == "__main__":
    criar_tabela()
    migrar_colunas_datas()

    for chamado in listar_chamados():
        print(chamado)


atualizar_status("CH005", "Fechado")


    
   

def contar_por_status(status):
    conexao = conectar()
    cursor = conexao.cursor()

    cursor.execute("""
        SELECT COUNT(*)
        FROM chamados
        WHERE LOWER(status) = LOWER(?)
    """, (status.strip(),))

    count = cursor.fetchone()[0]

    conexao.close()
    return count   

def contar_todos_por_status():
    conexao = conectar()
    cursor = conexao.cursor()

    cursor.execute("""
        SELECT status, COUNT(*)
        FROM chamados
        GROUP BY status
    """)

    resultados = cursor.fetchall()

    conexao.close()
    return resultados


def contar_todas_por_prioridade():
    conexao = conectar()
    cursor = conexao.cursor()

    cursor.execute("""
        SELECT prioridade, COUNT(*) AS quantidade
        FROM chamados
        GROUP BY prioridade
        ORDER BY quantidade DESC
    """)

    resultados = cursor.fetchall()

    conexao.close()
    return resultados

def contar_prioridade_ordenadas():
    conexao = conectar()
    cursor = conexao.cursor()

    cursor.execute("""
        SELECT prioridade, COUNT(*) AS quantidade
        FROM chamados
        GROUP BY prioridade
        ORDER BY quantidade DESC
    """)

    resultados = cursor.fetchall()

    conexao.close()
    return resultados

print(contar_prioridade_ordenadas())
