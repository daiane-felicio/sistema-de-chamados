import json

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
    
    novo_chamado = Chamado(codigo, categoria, prioridade, descricao, status)
    chamados.append(novo_chamado)
    print(f"Chamado {codigo} adicionado com sucesso.")


def atualizar_status_por_codigo(chamados, codigo, novo_status):
    chamado = buscar_chamado(chamados, codigo)
    if chamado:
        chamado.atualizar_status(novo_status)
    else:
        print(f"Chamado com código {codigo} não encontrado.")
        


def remover_chamado(chamados, codigo):
    chamado = buscar_chamado(chamados, codigo)
    if chamado:
        chamados.remove(chamado)
        print(f"Chamado {codigo} removido com sucesso.")
    else:
        print(f"Chamado com código {codigo} não encontrado.")

def salvar_chamados(chamados):
    dados = [chamado.para_dict() for chamado in chamados]
    with open("dados.json", "w", encoding="utf-8") as arquivo:
        json.dump(dados, arquivo, ensure_ascii=False, indent=4)
        

def carregar_chamados():
    with open("dados.json", "r", encoding="utf-8") as arquivo:
        dados = json.load(arquivo)
        chamados_carregados = []
        for item in dados:
            chamado = Chamado(
                item["codigo"],
                item["categoria"],
                item["prioridade"],
                item["descricao"],
                item["status"]
            )
            
            chamados_carregados.append(chamado)
        return chamados_carregados
  
  
chamados = carregar_chamados()          

while True:
    print("\n--- Sistema de Chamados ---")
    print("1 - Listar chamados")
    print("2 - Buscar chamado")
    print("3 - Adicionar chamado")
    print("4 - Atualizar status")
    print("5 - Remover chamado")
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
        salvar_chamados(chamados)    
        
    elif opcao == "4":
        codigo = input("Digite o código do chamado: ")
        novo_status = input("Digite o novo status do chamado: ")
        atualizar_status_por_codigo(chamados, codigo, novo_status)
        salvar_chamados(chamados)
        
    elif opcao == "5":
        codigo = input("Digite o código do chamado:")
        remover_chamado(chamados, codigo)
        salvar_chamados(chamados)

    else:
        print("Opção inválida. Tente novamente.")
        

salvar_chamados(chamados)


    
    