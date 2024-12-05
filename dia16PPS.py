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

#3. Observer (Observador)
# Definição
#  OpadrãoObserverdefineumadependênciaum-para-muitosentreobjetos,demodoque
#  quandoumobjetomudadeestado, todososseusdependentessãonotificadose
#  atualizadosautomaticamente.
#  Analogia
#  Imaginequevocêestánaescolaetemumprofessorqueinformaaosalunossobre
#  alteraçõesnohoráriodasaulas.Semprequeháumamudança,oprofessornotificatodosos
#  alunos,garantindoquetodosestejamatualizados.

class Observador:
    def atualizar(self, mensagem):
        pass
    
class Aluno(Observador):
    def __init__(self, nome):
        self.nome = nome
        
    def atualizar(self,mensagem):
        print(f"{self.nome} recebeu a mensagem: {mensagem}")
        
class Professor:
    def __init__(self):
        self.observadores = []
        
    def adicionar_observador(self, observador):
        self.observadores.append(observador)
        
    def remover_observador(self, observador):
        self.observadores.remove(observador)
        
    def notificar_observadores(self, mensagem):
        for observador in self.observadores:
            observador.atualizar(mensagem)
            
# Testando O Observer:
professor = Professor()
aluno1 = Aluno("Ana")
aluno2 = Aluno("Pedro")

professor.adicionar_observador(aluno1)
professor.adicionar_observador(aluno2)

professor.notificar_observadores(" A aula será á 14h.")
