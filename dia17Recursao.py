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
