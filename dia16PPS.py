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

#2 Factory Method (Método de Fábrica)
#  Definição
# OpadrãoFactoryMethoddefineumainterfaceparacriarobjetos,maspermitequeas
#  subclassesdecidamqualclasseinstanciar.Elepromoveodesacoplamentoentreacriação
#  deobjetoseousodessesobjetos.
#  Analogia
#  Penseemumafábricaqueproduzdiferentestiposdeveículos(carros,motos,caminhões).
#  Afábricaforneceummétodoparacriarveículos,mascadatipodeveículotemsuaprópria
#  implementaçãoespecífica

from abc import ABC, abstractmethod

class Veiculo(ABC):
    @abstractmethod
    def mover(self):
        pass
    
class Carro(Veiculo):
    def mover(self):
        print("O carro está se movendo.")
        
class Moto(Veiculo):
    def mover(self):
        print("A moto está se movendo.")
        
class FabricaVeiculos:
    def criar_veiculos(self, tipo):
        if tipo == "carro":
            return Carro()
        elif tipo == "moto":
            return Moto()
        else:
            raise ValueError("Tipo de veículo desconhecido.")
        
# Testando o Factory Method:
fabrica = FabricaVeiculos()
carro = fabrica.criar_veiculos("carro")
moto = fabrica.criar_veiculos("moto")

carro.mover()
moto.mover()
