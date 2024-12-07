'''Introdução a Testes Unitários
O Que São Testes Unitários?
Testes unitários são pequenos testes que verificam se partes específicas do seu código
(unidades) estão funcionando corretamente. Eles ajudam a garantir que cada componente
individual do seu programa opere conforme o esperado.'''

''' Como Escrever Testes Unitários em Python
Em Python, a biblioteca padrão unittest facilita a criação e execução de testes unitários.
Exemplo Básico:'''




import unittest
def somar(a, b):
    return a + b


class TestSomar(unittest.TestCase):
    def test_somar_positivos(self):
        self.assertEqual(somar(2, 3), 5)

    def test_somar_negativos(self):
        self.assertEqual(somar(-1, -1), -2)

    def test_somar_zero(self):
        self.assertEqual(somar(0, 5), 5)


if __name__ == '__main__':
    unittest.main()
