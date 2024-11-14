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
def somar(a, b):
    return a + b

def subitrair(a, b):
    return a - b

def multiplicar(a, b):
    return a * b

def dividir(a, b):
    if b != 0:
        return a / b
    else:
        return "Erro: Divisão por zero!"

numero1 = float(input("Digite o primeiro número: "))
numero2 = float(input("Digite o segundo número: "))
operacao = input("Escolha a operação (+, -, *, /): ")

if operacao == '+':
    resultado = somar(numero1, numero2)
elif operacao == '-':
    resultado = subitrair(numero1, numero2)
elif operacao == '*':
    resultado = multiplicar(numero1, numero2)
elif operacao == '/':
    resultado = dividir(numero1, numero2)
else:
    resultado = ("Operação inválida!")

print("Resultado: ",  resultado)



