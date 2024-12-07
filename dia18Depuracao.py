#  O Que é Depuração?
#  Depuração (ou debugging) é o processo de identificar, analisar e corrigir erros ou bugs no
#  seu código. Mesmo os programadores mais experientes encontram erros, e saber como
#  depurá-los de forma eficiente é uma habilidade essencial.

# Técnicas de Depuração
#  1. Leitura Atenta do Código
#  Antes de tudo, leia seu código cuidadosamente. Às vezes, o erro está em uma linha simples
#  que passou despercebida.
#  2. Uso de Print Statements
#  Adicionar declarações print() em diferentes partes do código ajuda a verificar o fluxo de
#  execução e os valores das variáveis em tempo real.
#  Exemplo:
def dividir(a, b):
    print(f"Dividindo {a} por {b}")
    resultado = a / b
    print(f"Resultado: {resultado}")
    return resultado


dividir(10, 2)
dividir(5, 0)  # vai causar um erro.
