import database as db


class Chamado:
    def __init__(self, codigo, categoria, prioridade, descricao, status):
        self.codigo = codigo
        self.categoria = categoria
        self.prioridade = prioridade
        self.descricao = descricao
        self.status = status
    
    def para_dict(self):
        return {
            "codigo": self.codigo,
            "categoria": self.categoria,
            "prioridade": self.prioridade,
            "descricao": self.descricao,
            "status": self.status
        }    
    def __str__(self):
        return f"Código: {self.codigo}, Categoria: {self.categoria}, Prioridade: {self.prioridade}, Descrição: {self.descricao}, Status: {self.status}"
    
    def atualizar_status(self, novo_status):
        self.status = novo_status
        print(f"Status do chamado {self.codigo} atualizado para: {self.status}")
        

def linha_para_chamado(linha):
    id_, codigo, categoria, prioridade, descricao, status = linha

    return Chamado(
        codigo,
        categoria,
        prioridade,
        descricao,
        status
    )
    
    
def buscar_chamado(chamados,codigo):
    for chamado in chamados:
        if chamado.codigo == codigo:
            return chamado

    return None

def listar_chamados(chamados):
    for chamado in chamados:
        print(chamado)


def adicionar_chamado(chamados, codigo, categoria, prioridade, descricao, status):
    if buscar_chamado(chamados, codigo):
        print(f"Já existe um chamado com o código {codigo}.")
        return
    
    if not codigo or not categoria or not prioridade or not descricao or not status:
        print("Todos os campos são obrigatórios. Chamado não adicionado.")
        return
    
    prioridades = ["Baixa", "Média", "Alta"]

    if prioridade.lower() not in [p.lower() for p in prioridades]:
        print(f"Prioridade inválida. Escolha entre: {', '.join(prioridades)}.")
        return
    
    status_validos = ["Aberto", "Em andamento", "Resolvido", "Fechado"]
    
    if status.lower() not in [s.lower() for s in status_validos]:
        print(f"Status inválido. Escolha entre: {', '.join(status_validos)}.")
        return
    
    
    prioridade = prioridade.capitalize()
    status = status.capitalize()

    
    novo_chamado = Chamado(codigo, categoria, prioridade, descricao, status)
    
    chamados.append(novo_chamado)
    
    db.adicionar_chamado(
        codigo, 
        categoria, 
        prioridade, 
        descricao, 
        status
        
    )
    
    print(f"Chamado {codigo} adicionado com sucesso.")


def atualizar_status_por_codigo(chamados, codigo, novo_status):
    
    if not validar_status(novo_status):
        print("Status inválido. Escolha entre: Aberto, Em andamento, Resolvido, Fechado.")
        return


    novo_status = novo_status.strip().capitalize()

    chamado = buscar_chamado(chamados, codigo)

    if chamado:
        chamado.atualizar_status(novo_status)
        db.atualizar_status(codigo, novo_status)
    else:
        print(f"Chamado com código {codigo} não encontrado.")
        

def validar_status(status):
    status_validos = ["Aberto", "Em andamento", "Resolvido", "Fechado"]
    status = status.strip().capitalize()
    return status in status_validos    
    
    
def remover_chamado(chamados, codigo):
    chamado = buscar_chamado(chamados, codigo)
    if chamado:
        chamados.remove(chamado)
        db.excluir_chamado(codigo)
        print(f"Chamado {codigo} removido com sucesso.")
    else:
        print(f"Chamado com código {codigo} não encontrado.")

  
db.criar_tabela()

chamados = [
    linha_para_chamado(linha)
    for linha in db.listar_chamados()
]        

while True:
    print("\n--- Sistema de Chamados ---")
    print("1 - Listar chamados")
    print("2 - Buscar chamado")
    print("3 - Adicionar chamado")
    print("4 - Atualizar status")
    print("5 - Remover chamado")
    print("6 - Filtrar chamados por status")
    print("7 - Listar chamados por prioridade")
    print("8 - Listar chamados por código")
    print("9 - Filtrar chamados por prioridade")
    print("10 - Filtrar por status e prioridade")
    print("11 - Filtrar por status ou prioridade")
    print("0 - Sair")

    opcao = input("Escolha uma opção: ")

    if opcao == "0":
        print("Encerrando o sistema...")
        break
    
    elif opcao == "1":
        listar_chamados(chamados)    
        
    elif opcao == "2": 
        codigo = input("Digite o código do chamado: ")
        resultado = buscar_chamado(chamados, codigo)
        
        if resultado:
             print(f"Chamado encontrado: {resultado}")
        else:
            
            print("Chamado não encontrado.")
        
    elif opcao == "3":
        codigo = input("Digite o código do chamado: ")
        categoria = input("Digite a categoria do chamado: ")
        prioridade = input("Digite a prioridade do chamado: ")
        descricao = input("Digite a descrição do chamado: ")
        status = input("Digite o status do chamado: ")   
        
        adicionar_chamado(chamados, codigo, categoria, prioridade, descricao, status)
          
        
    elif opcao == "4":
        codigo = input("Digite o código do chamado: ")
        novo_status = input("Digite o novo status do chamado: ")
        atualizar_status_por_codigo(chamados, codigo, novo_status)
       
        
    elif opcao == "5":
        codigo = input("Digite o código do chamado:")
        remover_chamado(chamados, codigo)
        
  

    elif opcao == "6":
        status = input("Digite o status que deseja buscar: ")

        resultados = db.buscar_por_status(status)

        if resultados:
            for linha in resultados:
                chamado = linha_para_chamado(linha)
                print(chamado)
        else:
            print("Nenhum chamado encontrado com esse status.")


    elif opcao == "7":
        resultados = db.listar_por_prioridade()

        if resultados:
            for linha in resultados:
                chamado = linha_para_chamado(linha)
                print(chamado)
        else:
               print("Nenhum chamado cadastrado.")     
     
    elif opcao == "8":
        ordem = input("Digite ASC para crescente ou DESC para decrescente: ").upper()

        if ordem not in ["ASC", "DESC"]:
           print("Ordem inválida. Escolha entre ASC ou DESC.")
           continue
       
       
        resultados = db.listar_por_codigo(ordem)
        
  
        if resultados:
            for linha in resultados:
                chamado = linha_para_chamado(linha)
                print(chamado)
        else:
            print("Nenhum chamado cadastrado.")
            
    elif opcao == "9":
        prioridade = input("Digite a prioridade que deseja buscar: ")

        resultados = db.buscar_por_prioridade(prioridade)

        if resultados:
            for linha in resultados:
                chamado = linha_para_chamado(linha)
                print(chamado)
        else:
            print("Nenhum chamado encontrado com essa prioridade.")
            
    elif opcao == "10":
        status = input("Digite o status: ")
        prioridade = input("Digite a prioridade: ")

        resultados = db.buscar_por_status_e_prioridade(status, prioridade)

        if resultados:
            for linha in resultados:
                chamado = linha_para_chamado(linha)
                print(chamado)
        else:
            print("Nenhum chamado encontrado com esses filtros.")
            
            
    elif opcao == "11":
        status = input("Digite o status: ")
        prioridade = input("Digite a prioridade: ")

        resultados = db.buscar_por_status_ou_prioridade(status, prioridade)

        if resultados:
            for linha in resultados:
                chamado = linha_para_chamado(linha)
                print(chamado)
        else:
            print("Nenhum chamado encontrado com esses filtros.")                       
            

else:
    print("Opção inválida. Tente novamente.")
    
    