#------------ Configurando o Ambiente ---------------------
# Importar módulos Necessários:
import json
import os
from datetime import datetime
# -----------Funções para Carregar e Salvar Tarefas --------
# Função para carregar as tarefas do arquivo:
def  carregar_tarefas(tarefas):
    if os.path.exists('tarefas.json'):
        with open('tarefas.json', 'r') as arquivo:
            return json.load(arquivo)
    else:
        return []
# Função para salvar as tarefas no arquivo:
def salvar_tarefas(tarefas):
    with open('tarefas.json', 'w') as arquivo:
        json.dump(tarefas, arquivo, indent=4)
#-----------Gerar ID Único para as Tarefas -------------------
def gerar_id(tarefas):
    if tarefas:
        ultimo_id = tarefas[-1]['id']
        return ultimo_id + 1
    else:
        return 1
# -----------Função para adicionar Tarefas -------------------
def adicionar_tarefa(tarefas):
    print("\nAdicionar Nova Tarefa")
    titulo = input("Título: ")
    descricao = input("Descrição: ")
    data_input = input("Data de conclusão (dd/mm/aaaaaaaa: ")
    try:
        data_obj = datetime.strptime(data_input, '%d/%m/%Y')
        data = data_obj.strftime('%d/%m/%Y')
        if data_obj.date() < datetime.now().date():
            print("Data de conclusão não pode ser no passado.")
            return
    except ValueError:
        print("Data em formato inválido. Utilize dd/mm/aaaa")
        return
    tarefa = {
        'id': gerar_id(tarefas),
        'titulo': titulo,
        'descricao': descricao,
        'data': data,
        'concluida': False
    }
    tarefas.append(tarefa)
    salvar_tarefas(tarefas)
    print("Tarefa adcionada com sucesso!")
