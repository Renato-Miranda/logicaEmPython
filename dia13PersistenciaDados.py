#Abrir um arquivo para leitura:
arquivo = open('diario.txt', 'r')
#lendo arquivo inteiro:
conteudo = arquivo.read()
print(conteudo)

#Lendo linhas individualmente:
linha = arquivo.readline()
while linha:
    print(linha.strip()) #strip() remove os caracteres de nova linha
    linha = arquivo.readline()

#Lendo todas as linhas em uma lista:
linhas = arquivo.readlines()
for linha in linhas:
    print(linha.strip())

# Exemplo de Escrita:
arquivo = open('saida.txt', 'w')
arquivo.write('Escrevendo uma linha no arquivo.\n')
arquivo.write('Escrevendo outra linha.\n')
arquivo.close()

# Exemplo de Anexar:
arquivo = open('saida.txt', 'a')
arquivo.write('Esta linha será adicionada ao final do arquivo.\n')
arquivo.close()

## Usando Gerenciador de Contexto with: O uso de with é como ter umafechadura automática que fecha a porta da caixa de armazenamento mesmo que algo dê errado. Ele garante que o arquivo seja fechado autimaticamente após o bloco de código, mesmo se ocorrem erros:

with open('diario.txt', 'r') as arquivo:
    conteudo = arquivo.read()
    print(conteudo)
    