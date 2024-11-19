# #fatiamento de string
# palavra = "Programação"
# fatia = palavra[0:7]
# print(fatia)

# #Comprimento da String
# texto = "Aprendendo Python"
# tamanho = len(texto)
# print(f"O texto em {tamanho} caracteres.")

# #Método format() - inserir valores dentro de uma string
# idade = 26 
# mensagem = "eu tenho {} anos.".format(idade)
# print(mensagem)

# #f-strings são uma versão mais simples do format(). Basta colocar um f antes das aspas e usar chaves {} para inserir as variáveis direto.
# nome = "Carlos"
# cidade = "São Paulo"
# mensagem = f"Meu nome é {nome} e moro em {cidade}."
# print(mensagem)

###Métodos Comuns de Strings###
##Trasformando maiúsculas e Minúsculas

#upper() - transforma todos os caracteres em maiúsculas.
# texto = "Bom dia"
# print(texto.upper())    

# #lower() - Todos os caracteres em minúsculas.
# print(texto.lower())

# #tittle() Coloca a primeira letra de cada palavra em maiúscula.
# print(texto.title())

# ##Removendo Espaçoes em Branco
# #strip() Remove espeços em branco no início e no fim da string.
# texto = "  Olá!  "
# print(texto.strip())

# ##Substituindo Partes da String
# #replace() - Substitui uma parte da string por outra.
# frase = "Aprender Java é divertido!"
# nova_frase = frase.replace("Java", "Python")
# print(nova_frase)

# ##Encontrando Substrings
# #find() - Encontra a posição de uma substring dentro da string.
# frase = "Onde está o Wally?"
# posição = frase.find("Wally")
# print(f"Wally está na posição {posição}")

# ##Dividindo e Juntando Strings
# #split() - Divide a string em uma lista, usando um separador.
# dados = "maçã,banana,laranja"
# lista_frutas = dados.split(",")
# print(lista_frutas)

# #join() - Junta elementos de uma lista em uma String.
# lista_palavras = ["Python", "é", "Legal"]
# frase= " ".join(lista_palavras)
# print(frase)

##### EXERCÍCIOS PRÁTICOS ####

#1. Contador de Vogais

frase = input("Digite uma frase: ").lower()
vogais = "aeiou"
contador = 0 

for letra in frase:
    if letra in vogais:
        contador += 1
print(f"A frase tem {contador} vogais.")