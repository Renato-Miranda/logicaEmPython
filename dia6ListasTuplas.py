#1 Lista de Convidados 

# convidados = ['Ana', 'Bruno', 'Carlos', 'Diana']

# for covidado in convidados:
#     print(f"Olá, {covidado}! Você está convidado para a festa.")

#2 Estatística de Números

entrada = input("Digite números separados por espaço: ")
numeros = [float(num) for num in entrada.split()]

maior_numero = max(numeros)
menor_numero = min(numeros)
soma_numeros = sum(numeros)
media_numeros = soma_numeros / len(numeros)

print("Maior número:", maior_numero)
print("Menor número:", menor_numero)
print("Soma dos números:", soma_numeros)
print("Média dos números:", media_numeros)
