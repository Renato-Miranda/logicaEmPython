#exemplo prático: Tentando abrir um arquivo que pode não existir.
# try:
#     arquivo = open('dados.text', 'r')
#     conteudo = arquivo.read()
# except FileNotFoundError:
#     print("Erro: O arquivo 'dados.txt' não foi encontrado maninho! Sowwy:(")
# else:
#     print("Arquivo lido com sucesso!")
#     print(conteudo)
# finally:
#     print("Operação de leitura de arquivo finalizada!")

# ### Lidando com erros de formar segura: ##
# #Capturando exceções Espercíficas: 
# try:
#     numero = int(input("Digite um número inteiro: "))
#     resultado = 100 / numero
# except ValueError:
#     print("Erro: Entrada inválida. Por favor, digite um número inteiro.") 
# except ZeroDivisionError:
#     print("Erro: Divisão por zero não é permitida.")
# else:
#     print(f"O Resultado é: {resultado}")
# finally:
#     print("Operação de divisão finalizada.")
    
### Usando else para cod que não deva gerar exceções 
# try: 
#     numero = int(input("Digite um número inteiro: "))
#     resultado = 100 / numero
# except (ValueError, ZeroDivisionError) as e:
#     print(f"Erro: {e}")
# else:
#     print(f"O resultado da divisão é: {resultado}")

### Usando finally para limpeza de recursos 
# try: 
#     arquivo = open('dados.txt', 'r')
#     conteudo = arquivo.read()
# except FileNotFoundError:
#     print("Erro: Arquivo não encontrado.")
# else:
#     print("Arquivo lido com sucesso!")
# finally:
#     if 'arquivo' in locals():
#         arquivo.close()
#         print("Arquivo fechado.")   

### Exemplos Práticos ###
#1. Calculadora com tratamento de exceções:
def calculadora():
    try:
        num1 = float(input("Digite o primeiro número: "))
        operador = input("Digite o operador (+, -, *, /): ")
        num2 = float(input("Digite o segundo número: "))
        
        if operador == '+':
            resultado = num1 + num2
        elif operador == '-':
            resultado = num1 - num2
        elif operador == '*':
            resultado = num1 * num2
        elif operador == '/':
            resultado = num1 / num2
        else:
            raise ValueError("Operador inválido.")
        
    except ValueError as ve:
        print(f"Erro de valor: {ve}")
    except ZeroDivisionError:
        print("Erro: Divisão por zero.")
    else:
        print(f"O resultado é: {resultado}")
        
calculadora()