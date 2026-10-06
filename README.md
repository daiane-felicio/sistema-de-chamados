# Sistema de Chamados

Projeto desenvolvido em Python para simular um sistema simples de gerenciamento de chamados de suporte.

O sistema permite cadastrar, buscar, listar, atualizar e remover chamados, além de salvar os dados em arquivo JSON para manter as informações entre as execuções.

## Funcionalidades

- Listar chamados
- Buscar chamado por código
- Adicionar novos chamados
- Atualizar o status de um chamado
- Remover chamados
- Salvar os dados em arquivo JSON
- Carregar os dados automaticamente ao iniciar o sistema
- Validar prioridade e status
- Tratar erros de leitura e registros inválidos

## Tecnologias utilizadas

- Python
- JSON
- Git
- GitHub
- Visual Studio Code

## Como executar

1. Clone este repositório:
   ```bash
   git clone https://github.com/daiane-felicio/sistema-de-chamados.git

2. Acesse a pasta do projeto:
   ```bash
   cd sistema-de-chamados  

3. Execute o arquivo principal:
  
  python main.py

## Aprendizados

Durante o desenvolvimento deste projeto, pratiquei:

- criação de classes e objetos em Python
- funções para buscar, adicionar, atualizar e remover dados
- validação de entradas
- persistência de dados com JSON
- tratamento de erros com try/except
- organização e padronização de dados
- uso de Git e GitHub para versionamento do projeto

## Próximos passos

- Melhorar a organização visual do terminal
- Adicionar novos filtros de busca
- Criar relatórios simples dos chamados
- Evoluir o projeto para usar banco de dados no futuro
- Criar uma interface gráfica ou versão web


## Autora

Desenvolvido por Daiane Felicio durante os estudos de Python e desenvolvimento de projetos para portfólio.


# Sistema de Chamados

Sistema de chamados desenvolvido em Python para praticar lógica de programação, orientação a objetos, validação de dados e persistência com SQLite.

## Funcionalidades

- Listar chamados
- Buscar chamado por código
- Adicionar chamados
- Atualizar status
- Remover chamados
- Validação de prioridade e status
- Persistência de dados com SQLite

## Tecnologias

- Python
- SQLite
- Git / GitHub

## Banco de dados

Os chamados são armazenados em um banco SQLite criado automaticamente na primeira execução.

A aplicação utiliza operações CRUD:

- Create — adicionar chamados
- Read — listar e buscar chamados
- Update — atualizar status
- Delete — remover chamados

## Como executar

```bash``
python main.py

## Próximas melhorias

Autenticação de usuários
Controle de permissões
Interface gráfica ou web
Novos filtros e relatórios