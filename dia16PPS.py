#---------------------- PADRÕES DE PROJETO BÁSICOS -------------------------------------
#1. Singleton:
#  Definição
#  Opadrão Singleton garante que uma classe tenha apenas uma única instância e fornece
#  umponto global de acesso a ela.
#  Analogia
#  Imagine que você tem um gerente em uma empresa. Só pode haver um gerente, e todos os
#  funcionários precisam acessar esse único gerente para tomar decisões importantes

class Gerente:
    _instancia = None
    
    def __new__(cls):
        if cls._instancia is None:
            cls._instancia = super(Gerente,cls).__new__(cls)
            return cls._instancia
        
# Testando so Singleton
gerente1 = Gerente()
gerente2 = Gerente()

print(gerente1 is gerente2)