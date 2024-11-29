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
#----------------------Função de Listar Tarefas ----------------------------
def listar_tarefas(tarefas):
    print("\nTarefas Perdentes:")
    tarefas_pendentes = [ t for t in tarefas if not t['concluida']]
    tarefas_pendentes = sorted(tarefas_pendetes, key=lambda x: datetime.strptime(x['data'], '%d/%m/%Y'))
    for tarefa in tarefas_pendentes:
        print(f"ID: {tarefa['id']}, Título: {tarefa['titulo']}, Data: {tarefa['data']}")
        
        print("\nTarefas Concluídas:")
        tarefas_concluidas = [t for t in tarefas if t['concluida']]
        tarefas_concluidas = sorted(tarefas_concluidas, key=lambda x: datetime.strptime(x['data'], '%d/%m/%Y'))
        for tarefa in tarefas_concluidas:
            print(f"ID: {tarefa['id']}, Título: {tarefa['titulo']}, Datas: {tarefa['data']}")
#----------------------Função para marcar Tarefa como Concluída------------------
def concluir_tarefa(tarefas):
    try:
        id_tarefa = int(input("Digite o ID da tarefa s ser concluída: "))
        for tarefa in tarefas:
            if tarefa['id'] == id_tarefa:
                if tarefa['concluida']:
                    print('A tarefa já está concluída.')
                else:
                    tarefa['concluida'] = True
                    salvar_tarefas(tarefas)
                    print("Tarefa concluída com sucesso!")
                return
        print("Tarefa não encontrada.")
    except ValueError:
        print("ID inválido")
#------------------Função para Remover Tarefa ------------------------
def remover_tarefa(tarefas):
    try:
        id_tarefa = input("Digite o ID da tarefa a ser removida: ")
        for tarefa in tarefas:
            if tarefa['id'] == id_tarefa:
                tarefas.remove(tarefa)
                salvar_tarefas(tarefas)
                print("Tarefa removida com sucesso!")
                return
        print("TArefa não encontrada")
    except ValueError:
        print("ID inválido")
#--------------------Função para Pesquisar Tarefas--------------------------
def pesquisar_tarefas(tarefas):
    termo = input("Digite o termo de pesquisa: ").lower()
    resultados = [t for t in tarefas if termo in t['titulo'].lower() or termo in t['descricacoes'].lower()]
    if resultados:
        print(f"\nTaferas que contêm '{termo}': ")
        for tarefa in resultados:
            status = 'Concluída' if tarefa['concluida'] else "Pendente"
            print(f"ID: {tarefa['id']}, Título: {tarefa['titulo']}, Status: {status}, Data: {tarefa['data']}")
    else:
        print("Nenhuma tarefa encontrada com o termo específicado.")
        