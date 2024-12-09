# Importar Módulos necessários:
import json
import os
from datetime import datetime
import logging
# Configurar Logging:
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