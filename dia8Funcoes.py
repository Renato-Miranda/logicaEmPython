def saudacao(nome, mensagem="seja bem vindo"):
    print(f"Olá, {nome}! {mensagem}")

saudacao("Renato", "Mestre supremo dos deprimidos!")

#Retorno de valores
def soma(a,b):
    resultado = a + b 
    return resultado

total = soma(5, 5)
print("O total é:", total)

#modificar váriaveis globais dentro de funções
contador = 0 

def incrementador():
    global contador
    contador += 3

incrementador()
print("Contador:", contador)

#Exercícios Práticos:
#1 Calculadora com Funções 