#1 Imprimindo números de 1 a 10

# for numero in range(1, 11):
#     print(numero)

#2 Calculando a soma dos Números de 1 a N

# N = int(input("Digite um número inteiro positivo: "))
# soma = 0 

# for i in range(1, N+1):
#     soma += i 

# print("A soma dos Números de 1 a", N, "é:", soma)

#3 Tabuada de um Número

# numero = int(input("Digite um número para ver sua tabuada: "))

# for i in range(1, 11):
#     resultado = numero * i
#     print(f"{numero} x {i} = {resultado}")

#4 contando Números Pares e Impares 

# pares = 0
# impares = 0

# for numero in range(1, 25):
#     if numero % 2 == 0:
#         pares += 1
#     else:
#         impares += 1

# print("Quantidades de números pares:", pares)
# print("quantidades de números impares:", impares)

#5 Adivinhe o Número 

# import random

# numero_secreto = random.randint(1,100)
# tentativas = 0

# while True:
#     palpite = int(input("Adivinhe o número (entre 1 e 100): ")) 
#     tentativas += 1 

#     if palpite == numero_secreto:
#         print(f"Parabéns! Você acertou em {tentativas} tentativas.")
#         break
#     elif palpite < numero_secreto:
#         print("O número é maior.")
#     else:
#         print("O número é menor.")

#DESAFIOS EXTRAS 

#1 Calculando Fatorila de um Número

# N = int(input("Digite um número inteiro positivo: "))

# fatorial = 1 

# if N < 0:
#     print("Não existe fatorial de número negativo.")
# elif N == 0 or N == 1:
#     print(f"o fatorial de {N} é 1.")
# else:
#     for i in range(1, N+1):
#         fatorial *= i 
#     print(f"O fatorial de {N} é {fatorial}.")

#2 Série Fibonacci

# N = int(input("Quantos termos da série Fibonacci você quer ver? "))

# termo1 = 0
# termo2 = 1
# contador = 0 

# if N < 0:
#     print("Por favor, insira um número positivo.")
# elif N == 1:
#     print("série Fibonacci até", N, "termo:")
#     print(termo1)
# else:
#     print("série Fibonacci:")
#     while contador < N:
#         print(termo1)
#         proximo_termo = termo1 + termo2
#         termo1 = termo2
#         termo2 = proximo_termo
#         contador += 1

#3 Jogo da foca simples

palavra_secreta = "python"
letras_descobertas = ["_"] * len(palavra_secreta)
tentativas = 6

while tentativas > 0 and "_" in letras_descobertas:
    print("Palvra:", " ".join(letras_descobertas))
    letra = input("Digite uma letras: ").lower()

    if letra in palavra_secreta:
        for idx, letra_secreta in enumerate(palavra_secreta):
            if letra == letra_secreta:
                letras_descobertas[idx] = letra
        print("Boa! você acertou uma letra.")
    else:
        tentativas -= 1
        print(f"Errou! Você tem {tentativas} tentativas restantes.")

if "_" not in letras_descobertas:
    print("Parabéns! Você adivinhou a palavra", palavra_secreta)
else:
    print("Você perdeu! A palavra era:", palavra_secreta)
            