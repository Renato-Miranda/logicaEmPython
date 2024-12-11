'''#----------------------- Importar Módulos necessários:-------------------------'''
import json
import os
from datetime import datetime
import logging
'''# -----------------------Configurar Logging:------------------'''
logging.basicConfig(level=logging.INFO,
                    format='%(asctime)s - %(levelname)s - %(message)s')
# Classe Livro:
class Livro:
    def __init__(self, id, titulo, autor, ano, isbn):
        self.id = id
        self.titulo = titulo
        self.autor = autor
        self.ano = ano
        self.isbn = isbn
        self.disponivel = True

    def exibir_informacoes(self):
        status = "Disponível" if self.disponivel else "Emprestado"
        print(f"ID: {self.id}, Título: {self.titulo}, Autor: {self.autor}, Ano: {self.ano}, Isbn: {self.isbn}, Status: {status}")
# Classe usuário:
class Usuario:
    def __init__(self, id, nome, email, telefone):
        self.id = id
        self.nome = nome
        self.email = email
        self.telefone = telefone
    
    def exibir_informacoes(self):
        print(f"ID: {self.id}, Nome: {self.nome}, Email: {self.email}, Telefone: {self.telefone}")
# Classe Emprestimo:
class Emprestimo:
    def __init__(self,id, usuario_id, livro_id, data_emprestimo, data_devolucao=None):
        self.id = id
        self.usuario_id = usuario_id
        self.livro_id = livro_id
        self.data_emprestimo = data_emprestimo
        self.data_devolucao = data_devolucao
        
    def exibir_informacoes(self):
        status = "Devolvido" if self.data_devolucao else "Pendente"
        print(f"ID: {self.id}, Usuário ID: {self.usuario_id}, Livro ID: {self.livro_id}, Data Emprestimo: {self.data_emprestimo}, Data Devolução: {self.data_devolucao}, Status: {status}")
'''----------------Função Para Carregar e Salvar Dados----------------'''
def carregar_dados(nome_arquivo):
    if os.path.exists(nome_arquivo):
        with open(nome_arquivo, 'r') as arquivo:
            return json.load(arquivo)
    else:
        return []

def salvar_dados(nome_arquivo, dados):
    with open(nome_arquivo, 'w') as arquivo:
        json.dump(dados, arquivo, indent=4)
'''---------------------Funções Para Gerenciamento de Livros -----------'''
def cadastrar_livro(livros):
    id = len(livros) + 1
    titulo = input("Título do Livro: ")
    autor = input("Autor: ")
    ano = input("Ano de Publicação: ")
    isbn = input("ISBN: ")
    livro = Livro(id, titulo, autor, ano, isbn)
    livros.append(livro.__dict__)
    salvar_dados('livros.json', livros)
    logging.info(f"Livro '{titulo}' cadastrado com sucesso.")
    
def listar_livros(livros):
    print("\n=== Lista de Livros ===")
    for livro_dict in livros:
        livro = Livro(**livro_dict)
        livro.exibir_informacoes()
'''---------------------Funções Para Gerenciamento de usuários--------------'''
def cadastrar_usuario(usuarios):
    id = len(usuarios) + 1
    nome = input("Nome do Usuário: ")
    email = input("Email do Usuário: ")
    telefone = input("Telefone: ")
    usuario = Usuario(id, nome, telefone)
    usuarios.append(usuario.__dict__)
    salvar_dados('usuarios.json', usuarios)
    logging.info(f"Usuário '{nome}' cadastrado com sucesso.")
    
def listar_usuarios(usuarios):
    print("\n=== Lista de Usuários ===")
    for usuario_dict in usuarios:
        usuario = Usuario(**usuario_dict)
        usuario.exibir_informacoes()
'''--------------------Funções ára Gerenciamento de Empre´stimos----------------'''
def emprestar_livro(emprestimos, livros, usuarios):
    id = len(emprestimos) + 1
    usuario_id = int(input("ID do Usuário: "))
    livro_id = int(input("ID do Livro: "))

    # Verificar se o usuário existe
    usuario_existente = any(u['id'] == usuario_id for u in usuarios)
    if not usuario_existente:
        print("Usuário não encontrado.")
        return
    
    # Verificar se o livro está disponível
    livro = next((l for l in livros if l['id'] == livro_id), None)
    if not livro:
        print("Livro não encontrado.")
        return
    if not livro['disponivel']:
        print("Livro não está diponível para empréstimo.")
        return
    
    data_emprestimo = datetime.now().strftime('%d/%m/%Y')
    emprestimo = Emprestimo(id, usuario_id, livro_id, data_emprestimo)
    emprestimos.append(emprestimo.__dict__)
    
    # Atualizar diponibilidade do livro
    livro['disponivel'] = False
    
    salvar_dados('emprestimos.json', emprestimos)
    salvar_dados('livros.json', livros)
    logging.info(f"Livro ID {livro_id} emprestado  para Usuário ID {usuario_id}")
    
def devolver_livro(emprestimos, livros):
    id_emprestimo = int(input("Id do Empréstimo: "))
    emprestimo = next((e for e in emprestimos if e['id'] == id_emprestimo), None)
    if not emprestimo:
        print("Emprestimo não encontrado.")
        return
    if not emprestimo['data_devolucao']:
        print("Livro já foi devolvido.")
        return
    
    data_devolucao = datetime.now().strftime('%d.%m.%Y')
    emprestimo['data_devolucao'] = data_devolucao
    
    # Atualizar disponibilidade do livro
    livro_id = emprestimo[livro_id]
    livro = next((l for l in livros if l['id'] == livro_id), None)
    if livro:
        livro['disponivel'] = True
        
    salvar_dados('emprestimos.json', emprestimos)
    salvar_dados('livros.json', livros)
    logging.info(f"Livro ID {livro_id} devolvido pelo Usuário ID {emprestimo['usuário_id']}")
    
def listar_emprestimos(emprestimos):
    print("\n=== Lista de Emprestimos ===")
    for emprestimo_dict in emprestimos:
        emprestimo = Emprestimo(**emprestimo_dict)
        emprestimo.exibir_informacoes()
'''-----------------------Funções de Pequisa--------------------------------'''
def pesquisar_livros(livros):
    termo = input("Digite o termo de pesquisa para livros: ").lower()
    resultados = [l  for l in livros if termo in l['titulo'].lower() or termo in l['autor'].lower()]
    if resultados:
        print(f"\n=== Resultados da Pesquisa por Livros: '{termo} ==='")
        for livro_dict in resultados:
            livro = Livro(**livro_dict)
            livro.exibir_informacoes()
    else:
        print("Nenhum livro encontrado com o termo especificado.")
        
def pesquisar_usuarios(usuarios):
    termo = input("Digite o termo de pesquisa para usuários: ").lower()
    resultados = [u for u in usuarios if termo in u['nome'].lower() or termo in u['email'].lower()]
    if resultados:
        print(f"\n=== Resultados da Pesquisa por Usuários : '{termo}' ===")
        for usuario_dict in resultados:
            usuario = Usuario(**usuario_dict)
            usuario.exibir_informacoes()
    else:
        print("Nenhum usuário encontrado com o termo especificado.")
'''----------------- Função de Relatórios ------------------------'''
def gerar_relatorio_emprestimos(emprestimos, usuarios, livros):
    print(f"\n=== Relatório de Emprestimos ===")
    for emprestimo_dict in emprestimos:
        emprestimo = Emprestimo(**emprestimo_dict)
        usuario = next((u for u in usuarios if u['id'] == emprestimo.usuario_id), None)
        livro = next((l for l in usuarios if l['id'] == emprestimo.livro_id), None)
        if usuario and livro:
            status = "Devolvido" if emprestimo.data_devolucao else "Pendente"
            print(f"Empréstimo ID: {emprestimo.id}, Usuário: {usuario['nome']}, Livro: {livro['titulo']}, Data Empréstimo: {emprestimo.data_emprestimo}, Data Devolução: {emprestimo.data_devolucao}, Status: {status}")
