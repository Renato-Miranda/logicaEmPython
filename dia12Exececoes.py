#exemplo prático: Tentando abrir um arquivo que pode não existir.
try:
    arquivo = open('dados.text', 'r')
    conteudo = arquivo.read()
except FileNotFoundError:
    print("Erro: O arquivo 'dados.txt' não foi encontrado maninho! Sowwy:(")
else:
    print("Arquivo lido com sucesso!")
    print(conteudo)
finally:
    print("Operação de leitura de arquivo finalizada!")

### Lidando com erros de formar segura: ##
#Capturando exceções Espercíficas: 
try:
    numero = int(input("Digite um número inteiro: "))
    resultado = 100 / numero
except ValueError:
    print("Erro: Entrada inválida. Por favor, digite um número inteiro.") 
except ZeroDivisionError:
    print("Erro: Divisão por zero não é permitida.")
else:
    print(f"O Resultado é: {resultado}")
finally:
    print("Operação de divisão finalizada.")
