#1 Lista de Convidados 

# convidados = ['Ana', 'Bruno', 'Carlos', 'Diana']

# for covidado in convidados:
#     print(f"Olá, {covidado}! Você está convidado para a festa.")

#2 Estatística de Números

# entrada = input("Digite números separados por espaço: ")
# numeros = [float(num) for num in entrada.split()]

# maior_numero = max(numeros)
# menor_numero = min(numeros)
# soma_numeros = sum(numeros)
# media_numeros = soma_numeros / len(numeros)

# print("Maior número:", maior_numero)
# print("Menor número:", menor_numero)
# print("Soma dos números:", soma_numeros)
# print("Média dos números:", media_numeros)

#3 Contagem de caracteres em uma String

# frase = input("Digite uma frase: ").lower()
# letras = {}

# for caractere in frase:
#     if caractere.isalpha():
#         if caractere in letras:
#             letras[caractere] += 1
#         else:
#             letras[caractere] = 1

# for letra, contagem in letras.items():
#     print(f"A letra '{letra}' aparece {contagem} vez(es)")

#4 Ordenando uma Lista

# entrada = input("Digite números separados por espaço: ")
# numeros = [float(num) for num in entrada.split()]

# #ordem crescente
# numeros_crescente = sorted(numeros)
# print("Números em ordem crescente:", numeros_crescente)

# #ordem decrescente

# numeros_decrescente = sorted(numeros, reverse=True)
# print("Números decrescente:", numeros_decrescente)

#5 Trabalhando com tuplas

# meses = ("Janeiro", "Fevereiro", "Março", "Abril", "Maio", "Junho",
# "Julho", "Agosto", "Setembro", "Outubro", "Novembro",
# "Dezembro")

# numero_mes = int(input("Digite um número entre 1 e 12: "))

# if 1 <= numero_mes <= 12:
#     print(f"O mês correspondente é {meses[numero_mes - 1]}.")
# else:
#     print("Números inválido. por favor, digite um número entre 1 e 12.")

## Desafios Extras
#1 Lista de Tarefas

tarefas = []

while True:
    print("\nMenu de Tarefas:")
    print("1. Adicionar tarefa")
    print("2. Remover tarefa")
    print("3. Listar tarefas")
    print("4. Sair")

    opcao = input("Escolhas uma opção: ")

    if opcao == "1": 
        tarefa = input("Digite a tarefa a ser adicionada: ")
        tarefas.append(tarefa)
        print("Tarefa adicionada com sucesso.")
    elif opcao == "2":
        tarefa = input("Digite uma tarefa a ser removida: ")
        if tarefa in tarefas:
            tarefas.remove(tarefa)
            print("Tarefa removida com sucesso.")
        else:
            print("TArefa não encontrada")
    elif opcao == "3":
        print("\nLista de Tarefas:")
        for idx, tarefa in enumerate(tarefas, start=1):
            print(f"{idx}. {tarefa}")
    elif opcao == "4":
        print("Saindo do programa.")
        break
    else:
        print("Opção inválida. Tente novamente.")

