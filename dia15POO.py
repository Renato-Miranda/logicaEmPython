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

#2. Classe Livro:
class Livro:
    def __init__(self, titulo, autor, ano):
        self.titulo = titulo
        self.autor = autor
        self.ano = ano
        
    def exibir_informacoes(self):
        print(f"Título: {self.titulo}, Autor: {self.autor}, Ano: {self.ano}")

livro1 = Livro("1984", "George Orwell", 1949)
livro2 = Livro("Dom Casmurro", "Machado de Assis", 1899)

livro1.exibir_informacoes()
livro2.exibir_informacoes()

#------------------------------- EXERCÍCIOS PRÁTICOS --------------------------------
#1. Clsse Retangulo:
class Retangulo:
    def __init__(self, largura, altura):
        self.largura = largura
        self.altura = altura
        
    def area(self):
        return self.largura * self.altura
    
    def perimetro(self):
        return 2 * (self.largura + self.altura)
    
retangulo = Retangulo(5, 3)
print(f"Áreas: {retangulo.area()}")
print(f"Perímetro: {retangulo.perimetro()}")

#2. Classe Aluno:
class Aluno:
    def __init__(self, nome):
        self.nome = nome
        self.notas = []
    
    def adicionar_nota(self, nota):
        self.notas.append(nota)
        
    def calcular_media(self):
        if self.notas:
            return sum(self.notas) / len(self.notas)
        else:
            return 0
        
aluno = Aluno("Joãozinho")
aluno.adicionar_nota(8.5)
aluno.adicionar_nota(7.0)
aluno.adicionar_nota(9.0)
media = aluno.calcular_media()
print(f"Média de {aluno.nome}: {media:.2f} ")

#3. Classe Cachorro:
class Cachorro:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade
        
    def latir(self):
        print(f"{self.nome} está latindo: Au Au!")
    
    def aniversario(self):
        self.idade += 1
        
luke = Cachorro("Luke", 2)
luke.latir()
print(f"idade: {luke.idade}")
luke.aniversario()
print(f"Nova idade: {luke.idade}")

#4. Classe Caculadora:
class Calculadora:
    def somar(self, a, b):
        return a + b
    def subtrair(self, a, b):
        return a - b
    def multiplicar(self, a, b):
        return a * b
    def dividir(self,a,b):
        if b != 0:
            return a / b
        else:
            print("Erro: divisão por zero")
            return None
        
calc = Calculadora()
print(calc.somar(5, 3))
        