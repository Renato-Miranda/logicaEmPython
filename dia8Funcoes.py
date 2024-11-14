# def saudacao(nome, mensagem="seja bem vindo"):
#     print(f"Olá, {nome}! {mensagem}")

# saudacao("Renato", "Mestre supremo dos deprimidos!")

# #Retorno de valores
# def soma(a,b):
#     resultado = a + b 
#     return resultado

# total = soma(5, 5)
# print("O total é:", total)

# #modificar váriaveis globais dentro de funções
# contador = 0 

# def incrementador():
#     global contador
#     contador += 3

# incrementador()
# print("Contador:", contador)

#Exercícios Práticos:
#1 Calculadora com Funções 
# def somar(a, b):
#     return a + b

# def subitrair(a, b):
#     return a - b

# def multiplicar(a, b):
#     return a * b

# def dividir(a, b):
#     if b != 0:
#         return a / b
#     else:
#         return "Erro: Divisão por zero!"

# numero1 = float(input("Digite o primeiro número: "))
# numero2 = float(input("Digite o segundo número: "))
# operacao = input("Escolha a operação (+, -, *, /): ")

# if operacao == '+':
#     resultado = somar(numero1, numero2)
# elif operacao == '-':
#     resultado = subitrair(numero1, numero2)
# elif operacao == '*':
#     resultado = multiplicar(numero1, numero2)
# elif operacao == '/':
#     resultado = dividir(numero1, numero2)
# else:
#     resultado = ("Operação inválida!")

# print("Resultado: ",  resultado)

#2 Função para Verificar Número Primo

# def eh_primo(numero):
#     if numero <= 1:
#         return False
#     for i in range(2, numero):
#         if numero % i == 0:
#             return False
#     return True

# num = int(input("digite um número inteiro: "))

# if eh_primo(num):
#     print(f"{num} é um número primo.")
# else:
#     print(f"{num} não é um número primo.")

#3 Conversor de Termperaturas
def celcius_para_farrenheit(c):
    return c * 9/5 + 32

def fahrenheit_para_celcius(f):
    return (f - 32) * 5/9

def celcius_para_kelvin(c):
    return c + 273.15

def kelvin_para_celcius(k):
    return k - 273.15

temperatura = float(input("Digite a temperatura: "))
unidade = input("Digite a unidade atual (C,F,K): ").upper()
converter_para = input("Converte para (C,F,K): ").upper()

if unidade == 'C':
    if converter_para == 'F':
        resultado = celcius_para_farrenheit(temperatura)
    elif converter_para == 'K':
        resultado = celcius_para_kelvin(temperatura)
elif unidade == 'F':
    if converter_para == 'C':
        resultado = fahrenheit_para_celcius(temperatura)
    elif converter_para == 'K':
        celsius = fahrenheit_para_celcius(temperatura)
        resultado = celcius_para_kelvin(celsius)
elif unidade == 'K':
    if converter_para == 'C':
        resultado = kelvin_para_celcius(temperatura)
    elif converter_para == 'F':
        celsius = kelvin_para_celcius(temperatura)
        resultado = celcius_para_farrenheit(celsius)
else:
    resultado = "Unidade inválida."

print(f"Temperatura convertida: {resultado} {converter_para}")
