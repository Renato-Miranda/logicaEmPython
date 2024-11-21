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