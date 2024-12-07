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
import logging
import pdb


def dividir(a, b):
    print(f"Dividindo {a} por {b}")
    resultado = a / b
    print(f"Resultado: {resultado}")
    return resultado


dividir(10, 2)
# dividir(5, 0)  # vai causar um erro.

# 3. Utilização do Debuggers
#  Ferramentas como o pdb (Python Debugger) permitem pausar a execução do código,
#  inspecionar variáveis e executar passo a passo para identificar onde ocorre o erro.
#  Exemplo de Uso do pdb:


# def somar(a, b):
#     pdb.set_trace()  # Ponto de interrupção
#     return a + b


# resultado = somar(3, 4)
# print(resultado)

'''
4. Revisão de Logs
Manter registros (logs) do que o programa está fazendo pode ajudar a identificar padrões ou
erros que ocorrem durante a execução.
Exemplo:
'''

logging.basicConfig(level=logging.DEBUG)


def multiplicar(a, b):
    logging.debug(f"Multiplicando {a} por {b}")
    return a * b


resultado = multiplicar(5, 6)
print(resultado)
