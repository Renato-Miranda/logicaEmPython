# ---------------------- PADRÕES DE PROJETO BÁSICOS -------------------------------------
# 1. Singleton:
#  Definição
#  Opadrão Singleton garante que uma classe tenha apenas uma única instância e fornece
#  umponto global de acesso a ela.
#  Analogia
#  Imagine que você tem um gerente em uma empresa. Só pode haver um gerente, e todos os
#  funcionários precisam acessar esse único gerente para tomar decisões importantes

from abc import ABC, abstractmethod


class Gerente:
    _instancia = None

    def __new__(cls):
        if cls._instancia is None:
            cls._instancia = super(Gerente, cls).__new__(cls)
            return cls._instancia


# Testando so Singleton
gerente1 = Gerente()
gerente2 = Gerente()

print(gerente1 is gerente2)

# 2 Factory Method (Método de Fábrica)
#  Definição
# OpadrãoFactoryMethoddefineumainterfaceparacriarobjetos,maspermitequeas
#  subclassesdecidamqualclasseinstanciar.Elepromoveodesacoplamentoentreacriação
#  deobjetoseousodessesobjetos.
#  Analogia
#  Penseemumafábricaqueproduzdiferentestiposdeveículos(carros,motos,caminhões).
#  Afábricaforneceummétodoparacriarveículos,mascadatipodeveículotemsuaprópria
#  implementaçãoespecífica


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

# 3. Observer (Observador)
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

    def atualizar(self, mensagem):
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

# --------------------------- EXERCÍCIOS PRÁTICOS --------------------
# 1. implementando o padrão Singleton na Classe Database:


class Database:
    _instancia = None

    def __new__(cls):
        if cls._instancia is None:
            cls._instancia = super(Database, cls).__new__(cls)
            cls._instancia.conexao = "Conexão com banco de dados estabelecida."
            return cls._instancia

    def conectar(self):
        print(self.conexao)


# Testando Singleton:
db1 = Database()
db1.conectar()

# 2. Implementar o Padrão Factory Method na criação de formas Geométricas
# Definir a Classe Abstrata Forma


class Forma(ABC):
    @abstractmethod
    def desenhar(self):
        pass
# Definir as Classe Concretas:


class Circulo(Forma):
    def desenhar(self):
        print("Desenhando um círculo.")


class Quadrado(Forma):
    def desenhar(self):
        print("Desenhando um quadrado.")


class Triangulo(Forma):
    def desenhar(self):
        print("Desenhando um triangulo.")
# Definir a Classe FabricaForma:


class FabricaForma:
    def criar_forma(self, tipo):
        if tipo == 'círculo':
            return Circulo()
        elif tipo == 'quadrado':
            return Quadrado()
        elif tipo == 'triângulo':
            return Triangulo()
        else:
            return ValueError("Tipo de forma desconhecido.")


# testando o Factory Method:
fabrica = FabricaForma()

forma1 = fabrica.criar_forma("círculo")
forma1.desenhar()
