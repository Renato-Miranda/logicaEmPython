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
import sys

print("VErsão do Python:", sys.version)

## Reutilização de Código - Criar meus próprios módulos 