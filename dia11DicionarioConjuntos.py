# Exemplo de Dicionário:
notas = {
    "Alice": 8.5,
    "Bruno": 7.0,
    "Carla": 9.0
}

# Conjuntos - Umconjunto é como uma caixa de elementos únicos. Ele não permite duplicatas e não
#  mantém uma ordem específica. Pense em um conjunto como uma coleção de objetos onde
#  a ordem não importa, apenas a presença ou ausência de elementos.

# Exemplo: Imagine que você tem uma lista de frutas, mas algumas estão repetidas

frutas = ["maçã", "banana", "laranja", "maçã", "banana"]

# Ao transformar essa lista em um conjunto, você elimina as duplicatas:

frutas_unicas = set(frutas)
print(frutas_unicas)

## Operações Básicas ##
# Criando um dicionário 
aluno = {
    "nome": "Daniel",
    "idade": 20,
    "curso": "Engenharia" 
}

#Acessando Valores
print(aluno["nome"])

## Adicionando ou Atualizando itens
# Adicionando um novo par chave-valor
aluno["nota"] = 9.5

# Atualizando um valor existente
aluno["idade"] = 21

# Removendo itens
del aluno["curso"]

# usando pop()
idade = aluno.pop("idade")
print(idade)

## Percorrendo um Dicionário

for chave, valor in aluno.items():
    print(f"{chave}: {valor}")

### Trabalhando com Conjuntos
# Criando um Conjunto

numeros = {1, 2, 3, 4, 5}

# Ou trasnformando uma lista em conjunto:

lista = [1, 2, 2, 3, 4, 4, 5]
numeros_unicos = set(lista)
print(numeros_unicos)

## Adicionando ou Removendo Elementos
# Adicionando
numeros.add(6)

# Removendo
numeros.remove(2)
print(numeros)

## Operações entre Conjuntos
#União: Combinda elementos de amabos os conjuntos.

conjunto_a = { 1, 2, 3}
conjunto_b = {3, 4 , 5}
uniao = conjunto_a.union(conjunto_b)
print(uniao)

## Interseção: Elementos comuns aos dois conjuntos.
intersecao = conjunto_a.intersection(conjunto_b)
print(intersecao)

#Diferença: Elementos presentes em um conjunto e não no outro
diferenca = conjunto_a.difference(conjunto_b)
print(diferenca)

#### Aplicações Práticas ####
## Usando Dicionários para Ocntar Ocorrências

texto = "banana maçã laranja banana maçã banana"
palavras = texto.split()

contagem = {}
for palavra in palavras:
    if palavra in contagem:
        contagem[palavra] += 1
    else:
        contagem[palavra] = 1

print(contagem)

## Usando Conjuntos para Encontrar Valores únicos

emails = ["a@exemplo.com", "b@exemplo.com", "a@exemplo.com", "c@exemplo.com"]
emails_unicos = set(emails)
print(emails_unicos)


###### EXERCÍCIOS PRÁTICOS ########
#1. Agenda Telefônica

# agenda = {}

# def adicionar_contato():
#     nome = input("Nome: ")
#     telefone = input("Telefone: ")
#     agenda[nome] = telefone
#     print("Contato adicionado com sucesso!")
    
# def buscar_contato():
#     nome = input("Nome do contato a buscar: ")
#     if nome in agenda:
#         print(f"Telefone de {nome}: {agenda[nome]}")
#     else:
#         print("Contato não encotrado.")
        
# def remover_contato():
#     nome = input("Nome do contato a remover: ")
#     if nome in agenda: 
#         del agenda[nome]
#         print("Contato removido com sucesso!")
#     else: 
#         print("contato não encontrado!")

# while True:
#     print("\n1. Adicionar contato")
#     print("2. Buscar contato")
#     print("3. Remover contato")
#     print("4. Sair")
#     opcao = input("Escolha uma opção: ")
    
#     if opcao == "1":
#         adicionar_contato()
#     elif opcao == "2":
#         buscar_contato()
#     elif opcao == "3":
#         remover_contato()
#     elif opcao == "4":
#         break
#     else: 
#         print("Opção invalida!")
        

#2. Verificação de palavras Únicas
# frase = input("Difite uma frase: ")
# palavras = frase.split()
# palavras_unicas = set(palavras)
# print("Palvras únicas:", palavras_unicas)

#3 União e interseção de Conjuntos
# numeros1 = input("Digite números separados por espaço para o primeiro conjuntos: ").split()
# numeros2 = input("Digite números separados por espaço para o segundo conjuntos: ").split()

# conjunto1 = set(numeros1)
# conjunto2 = set(numeros2)

# uniao = conjunto1.union(conjunto2)
# intersecao = conjunto1.intersection(conjunto2)

# print("União dos conjuntos:", uniao)
# print("Interseção dos conjuntos:", intersecao)

#4. Contador de Caracteres
texto = input("Digite um texte: ")

contagem = {}
for caractere in texto:
    if caractere in contagem:
        contagem[caractere] += 1
    else:
        contagem[caractere] = 1

print("Contagem de caracteres:")
for caractere, quantidade in contagem.items():
    print(f"'{caractere}' : {quantidade}")