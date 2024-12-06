#  O Queé Recursão?
#  A recursão é uma técnica de programação onde uma função chama a si mesma para
#  resolver um problema. É como uma matriosca russa, onde cada boneco contém outro
#  boneco dentro dele. Na programação, cada chamada recursiva resolve uma parte menor do
#  problema até que se atinja a solução final.

# Exemplo Simples:
def contar_regressivamente(n):
    if n <= 0:
        print("Fim")
    else:
        print(n)
        contar_regressivamente(n - 1)


contar_regressivamente(5)

# ----------------- EXEMPLOS DE ALGORITIMOS RECURSIVOS ----------------
# 1. FATORIAL:


def fatorial(n):
    if n == 0:
        return 1  # Caso base
    else:
        return n * fatorial(n - 1)  # Caso recursivo


# Exemplo de uso:
print(fatorial(5))

# 2 Sequência Fibonacci:


def fibonnacci(n):
    if n <= 0:
        return 0  # Caso base
    elif n == 1:
        return 1  # Caso base
    else:
        return fibonnacci(n-1) + fibonnacci(n - 2)  # Caso Recursivo


print(fibonnacci(7))

# 3. Pesquisa Binária:


def pesquisar_binaria(lista, alvo, inicio=0, fim=None):
    if fim is None:
        fim = len(lista) - 1

    if inicio > fim:
        return -1  # Elemento não encontrado

    meio = (inicio + fim) // 2

    if lista[meio] == alvo:
        return meio
    elif lista[meio] < alvo:
        return pesquisar_binaria(lista, alvo, meio + 1, fim)
    else:
        return pesquisar_binaria(lista, alvo, inicio, meio - 1)


# exemplo de uso:
lista = [1, 3, 5, 7, 9, 11]
print(pesquisar_binaria(lista, 7))
print(pesquisar_binaria(lista, 4))
