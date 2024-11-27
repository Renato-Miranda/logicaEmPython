# #Abrir um arquivo para leitura:
# arquivo = open('diario.txt', 'r')
# #lendo arquivo inteiro:
# conteudo = arquivo.read()
# print(conteudo)

# #Lendo linhas individualmente:
# linha = arquivo.readline()
# while linha:
#     print(linha.strip()) #strip() remove os caracteres de nova linha
#     linha = arquivo.readline()

# #Lendo todas as linhas em uma lista:
# linhas = arquivo.readlines()
# for linha in linhas:
#     print(linha.strip())

# # Exemplo de Escrita:
# arquivo = open('saida.txt', 'w')
# arquivo.write('Escrevendo uma linha no arquivo.\n')
# arquivo.write('Escrevendo outra linha.\n')
# arquivo.close()

# # Exemplo de Anexar:
# arquivo = open('saida.txt', 'a')
# arquivo.write('Esta linha será adicionada ao final do arquivo.\n')
# arquivo.close()

# ## Usando Gerenciador de Contexto with: O uso de with é como ter umafechadura automática que fecha a porta da caixa de armazenamento mesmo que algo dê errado. Ele garante que o arquivo seja fechado autimaticamente após o bloco de código, mesmo se ocorrem erros:

# with open('diario.txt', 'r') as arquivo:
#     conteudo = arquivo.read()
#     print(conteudo)

# ### Manipulação de Diferentes tipos de Arquivos ###
# ## Arquivos de Texto ##
# # Exemplo: lendo um arquivo CSV

# with open('receitas.csv', 'r') as arquivo:
#     for linha in arquivo:
#         colunas = linha.strip().split(',')
#         print(colunas)
        
# ## Arquivos Binários ##
# # Exemplo: Copiando um arquivo de imagem:

# with open('imagem.jpg' 'rb') as origem:
#     with open('copia_imagem.jpg', 'wb') as destino:
#         destino.write(origem.read())
        
# ## Arquivos JSON ##
# import json

# dados = {
#     'nome': 'João',
#     'idade': 30,
#     'cidades': ['São Paulo', 'Rio de Janeiro']
# }

# with open('dados.json', 'w') as arquivo:
#     json.dump(dados, arquivo, indent=4)
    
# # Lendo dados de um arquivo JSON
# import json

# with open('dados.json', 'r') as arquivo:
#     dados = json.load(arquivo)
#     print(dados)
    
## Escrevendo um arquivo CSV ##
# import csv

# with open('contatos.csv', 'w', newline='') as arquivo_csv:
#     escritor = csv.writer(arquivo_csv)
#     escritor.writerow(['Nome', 'Telefone', 'Email'])
#     escritor.writerow(['Ana', '9999-8888', 'ana@exemple.com'])
#     escritor.writerow(['Pedro', '9999-9999', 'pedro@example.com'])

# # Lendo um arquivo CSV:

# import csv

# with open('contatos.csv', 'r') as arquivo_csv:
#     leitor = csv.reader(arquivo_csv)
#     for linha in leitor:
#         print(linha)
        
### Exemplos Práticos ### 
#1. Contador de Palavras em uma arquivo:

# nome_arquivo = input("Digite o nome deo arquivo: ")

# try:
#     with open(nome_arquivo, 'r') as arquivo:
#         conteudo = arquivo.read()
# except FileNotFoundError:
#     print("Erro: Arquivo não encontrado.")
# else:
#     palavras = conteudo.lower().split()
#     contagem = {}
    
#     for palavra in palavras:
#         palavra = palavra.strip('.,!?";:-()')
#         if palavra in contagem:
#             contagem[palavra] += 1
#         else:
#             contagem[palavra] = 1
            
#     for palavra, quantidade in contagem.items():
#         print(f"{palavra}: {quantidade}")
        
#2. Gerenciador de Contatos:

import csv

def adicionar_contato():
    nome = input("Nome: ")
    telefone = input("Telefone: ")
    email = input("Email: ")
    
    with open('contato.csv', 'a', newline='') as arquivo_csv:
        escritor = csv.writer(arquivo_csv)
        escritor.writerow([nome, telefone, email])
    print("contato adicionado com sucesso!")
    
def listar_contatos():
    try:
        with open('contato.csv', 'r',) as arquivo_csv:
            leitor = csv.reader(arquivo_csv)
            for linha in leitor:
                print(f"Nome: {linha[0]}, telefone: {linha[1]}, email: {linha[2]}")
    except FileNotFoundError:
        print("Nenhum contato encontrado.")
        
while True:
    print("\nMenu:")
    print("1. Adicionar Contato")
    print("2. Listar Contatos")
    print("3. Sair")
    opcao = input("Escolha uma opção: ")
    
    if opcao == '1':
        adicionar_contato()
    elif opcao == '2':
        listar_contatos()   
    elif opcao == '3':
        break
    else:
        print("Opção inválida.")