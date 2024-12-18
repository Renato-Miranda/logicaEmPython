#importar módulo math para cálculos complexos
#import math

# numero = float(input("Digite um número para descobrir a raiz quadrada: "))
# raiz_quadrada = math.sqrt(numero)
# print(f"A raiz quadrada de {numero} é {raiz_quadrada}")

#Importando funções específicas
# from math import sqrt, pi
# print(f"O valor de pi é {pi}")
# print(f"A raiz quadrada de 25 é {sqrt(25)}")

#Usando Alias (Apelidos)
# import math as m

# print(f"Cosseno de 0 é {m.cos(0)}")

## Usando Bibliotecas padrão do Python ##
# Módulo Random 
# import random

# #simula o lançamento de um dado de 6 lados
# dado = random.randint(1,6)
# print(f"O resultado do dado é: {dado}")

# Módulo datetime - datas e horas
# from datetime import datetime

# agora = datetime.now()
# print(f"Data e hora atuais: {agora}")

#Módulo os - interagir com sistema operacional
# import os

# # Listando arquivos no diretório atual
# arquivos = os.listdir(".")
# print("Arquivos no diretório atual: {arquivos}")

#Módulo sys - saber mais sobre o sistema o programa está rodando.
# import sys

# print("VErsão do Python:", sys.version)

## Reutilização de Código - Criar meus próprios módulos 

## Exercícios Práticos
#1. Criando um módulo de conversão de temperaturas

# import conversoes

# temperatura_c = float(input("Digite a temperatura em Calsius: "))
# temperatura_f = conversoes.celcius_para_farrenheit(temperatura_c)
# temperatura_k = conversoes.celcius_para_kelvin(temperatura_c)

# print(f"{temperatura_c}°C equivale a {temperatura_f}°F e {temperatura_k}°K")

#2. Jogo de adivinhação usando o módulo random
# import random

# def jogo_adivinhacao():
#     numero_secreto = random.randint(1, 100)
#     tentativas = 0

#     print("Bem-vindo ao Jogo de Adivinhação!")
#     print("Tente adivinhar o número entre 1 e 100.")

#     while True:
#         palpite = int(input("Digite seu palpite: "))
#         tentativas += 1

#         if palpite == numero_secreto:
#             print(f"Parabéns! Você acertou em {tentativas} tentativas.")
#             break
#         elif palpite < numero_secreto:
#             print("Muito baixo! tente novamente.")
#         else:
#             print("Muito alto! Tente novamente.")

# jogo_adivinhacao()

import requests

resposta = requests.get('https://api.github.com')
print(f"Status da resposta: {resposta.status_code}")