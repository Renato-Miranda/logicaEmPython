# Sintaxe de Classe:
class Carros:
    pass 
#Criando objetos (instâncias) da classe carro:
meu_carro = Carros()
seu_carro = Carros()
# Exemplo com Atributos e Métodos:
class Carro:
    def __init__(self, marca, modelo, ano):
        self.marca = marca     # Atributo de instancia
        self.modelo = modelo   # Atributo de instancia
        self.ano = ano         # Atributo de instancia
        self.velocidade = 0    # Atributo de instancia
        
    def acelerar(self, incremento):
        self.velocidade += incremento
        print(f"O carro está agora a {self.velocidade} km/h.")
    
    def frear(self, decremento):
        self.velocidade -= decremento
        if self.velocidade < 0:
            self.velocidade = 0
        print(f"O carro está agora a {self.velocidade} km/h.")
# Atributos: São como as caracteristicas do carro
# Métodos: São as ações que o carro pode realizar

## Criando e usando Objetos ##
#Criando Objetos:
carro1 = Carro("Toyota", "Corolla", 2020)
carro2 = Carro("Honda", "Civic", 2018)

#Usando métodos:
carro1.acelerar(100)
carro2.acelerar(50)
carro1.frear(80)

# ------------------ EXEMPLOS COM ANALOGIAS DO MUNDO REAL --------------------------------
#1. Classe Pessoa:
class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade
        
    def apresentar(self):
        print(f"Olá meu nome é {self.nome} e tenho {self.idade} anos.")
    
    def aniversario(self):
        self.idade += 1 
        print(f"Feliz aniversário, {self.nome}! Agora você tem {self.idade} anos.")
        
joao = Pessoa("João", 28)
maria = Pessoa("Maria", 25)

joao.apresentar()
maria.apresentar()

joao.aniversario()