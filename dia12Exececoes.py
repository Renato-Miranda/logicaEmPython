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
# def calculadora():
#     try:
#         num1 = float(input("Digite o primeiro número: "))
#         operador = input("Digite o operador (+, -, *, /): ")
#         num2 = float(input("Digite o segundo número: "))
        
#         if operador == '+':
#             resultado = num1 + num2
#         elif operador == '-':
#             resultado = num1 - num2
#         elif operador == '*':
#             resultado = num1 * num2
#         elif operador == '/':
#             resultado = num1 / num2
#         else:
#             raise ValueError("Operador inválido.")
        
#     except ValueError as ve:
#         print(f"Erro de valor: {ve}")
#     except ZeroDivisionError:
#         print("Erro: Divisão por zero.")
#     else:
#         print(f"O resultado é: {resultado}")
        
# calculadora()

#2. Acesso a arquivos com tratamento de exceções.
# def ler_arquivo(nome_arquivo):
#     try:
#         with open(nome_arquivo, 'r') as arquivo:
#             conteudo = arquivo.read()
#             print(conteudo)
#     except FileNotFoundError:
#         print("Erro: O arquivo não foi encontrado.")
#     except PermissionError: 
#         print("Erro: Permissão negada para ler o arquivo.")
#     except Exception as e:
#         print(f"Ocorreu um erro inesperado: {e}")

# ler_arquivo('dados.txt')

#3. Conversão de dados com tratamento de exceções:
# def obter_idade():
#     while True:
#         try:
#             idade = int(input("Digite sua idade: "))
#             if idade < 0:
#                 raise ValueError("A idade não pode ser negativa")
#             return idade
#         except ValueError as ve:
#             print(f"Erro: {ve}")

# idade_usuario = obter_idade()
# print(f"Sua idade é: {idade_usuario}")

### Exercícios Extras ###
#1. Divisão Segura:
# def divisao_segura():
#     try:
#         numerador = float(input("Digite o numerador: "))
#         denominador = float(input("Digite o denominador: "))
#         resultado = numerador / denominador
#     except ValueError:
#         print("Erro: Por favor, insira números válidos")
#     except ZeroDivisionError:
#         print("Erro: divisão por zero não é permitida.")
#     else:
#         print(f"O resultado da divisão é: {resultado}")

# divisao_segura()

#2. Abertura de arquivo com verificação:
# def ler_arquivo_usuario():
#     nome_arquivo = input("Digite o nome do arquivo: ")
#     try:
#         with open(nome_arquivo, "r") as arquivo:
#             conteudo = arquivo.read()
#             print(conteudo)
#     except FileNotFoundError:
#         print("Erro: arquivo não existe.")
#     except PermissionError:
#         print("Erro: Sem permissão para ler o arquivo")
#     except Exception as e:
#         print(f"Ocorreu um erro: {e}")
        
# ler_arquivo_usuario()

#3. Conversão de temperatura com validação
# def celcius_para_fahrenheit():
#     try:
#         celcius = float(input("Digite a temperatura em Celcius: "))
#         fahrenheit = celcius * 9 / 5 + 32
#     except ValueError:
#         print("Erro: Por favor, insira um valor numérico.")
#     else:
#         print(f"A temperatura em Fahrenheit é: {fahrenheit:.2f}°F")
        
# celcius_para_fahrenheit()

#4. Sistema de Login Simples:
# class UsuarioNaoEncontradoError(Exception):
#     pass

# class SenhaIncorretaError(Exception):
#     pass

# usuarios = {
#     'admin': '1234',
#     'Usuario1': 'senha1'
# }

# def login():
#     try:
#         nome_usuario = input("Nome do usuário: ")
#         senha = input("Senha:  ")
        
#         if nome_usuario not in usuarios:
#             raise UsuarioNaoEncontradoError("Usuário não encontrado!")
#         elif usuarios[nome_usuario] != senha:
#             raise SenhaIncorretaError("Senha incorreta.")
#     except UsuarioNaoEncontradoError as e:
#         print(f"Erro: {e}")
#     except SenhaIncorretaError as e:
#         print(f"Erro: {e}")
#     else:
#         print("Login realizado com sucesso.")
        
# login()