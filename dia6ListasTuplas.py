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

entrada = input("Digite números separados por espaço: ")
numeros = [float(num) for num in entrada.split()]

#ordem crescente
numeros_crescente = sorted(numeros)
print("Números em ordem crescente:", numeros_crescente)

#ordem decrescente

numeros_decrescente = sorted(numeros, reverse=True)
print("Números decrescente:", numeros_decrescente)