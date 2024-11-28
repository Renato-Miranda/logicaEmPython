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
