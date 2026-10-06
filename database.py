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
        WHERE status = ?
    """, (status,))

    chamados = cursor.fetchall()

    conexao.close()
    return chamados

#print("Chamados abertos:")

#for chamado in buscar_por_status("Aberto"):
#    print(chamado)
    
 
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



