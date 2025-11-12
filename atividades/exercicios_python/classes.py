'''
class Pessoa:
    nome = ""
    
p1 = Pessoa()
p1.nome = "João"

p2 = Pessoa()
p2.nome = "Maria"

print(p1.nome)
print(p2.nome)

#2
class Animal:
    tipo = ""

a1 = Animal()
a1.tipo = "cachorro"

a2 = Animal()
a2.tipo = "gato"

print(a1.tipo)
print(a2.tipo)

#3
class Carro:
    estado = "novo"
    cor = ""

fusca = Carro()
ferrari = Carro()
ferrari.estado = "usado"

print(fusca.estado)
print(ferrari.estado)

#4
fusca.cor = "azul"
ferrari.cor = "vermelha"
print("Cor fusca: ", fusca.cor)
print("Cor ferrari: ", ferrari.cor)

#5
class Aluno:
    nome = ""
    nota = 7

nome = input("informe o nome do aluno: ")
nota = float(input("informe a nota do aluno: "))

aluno = Aluno()
aluno.nome = nome
aluno.nota = nota

print("Aluno: ", aluno.nome)
print("Nota: ", aluno.nota)

#6
class ContaBancaria:
    def __init__(self, saldo):
        self.saldo = saldo
    
    def mostrarSaldo(self):
        print("Saldo: ", self.saldo)

conta1 = ContaBancaria(1500)
conta2 = ContaBancaria(2600)

conta1.mostrarSaldo()
conta2.mostrarSaldo()

class Produto:
    def __init__(self, nome, preco):
        self.nome = nome
        self.preco = preco
    
    def mostrarProduto(self):
        print("Produto: ", self.nome)
        print("Preco: ", self.preco)

produto1 = Produto("TV Led 25'", 1599.99)
produto2 = Produto("Notebook Lenovo", 1949.90)

produto1.mostrarProduto()
produto2.mostrarProduto()

#7
class Computador:
    def __init__(self):
        self.ligado = False
    
    def ligar(self):
        self.ligado = True
    
    def mostrarComputador(self):
        print("Computador está", "ligado" if self.ligado else "desligado")
    
computador = Computador()
computador.mostrarComputador()
computador.ligar()
computador.mostrarComputador()    


#7
class Lampada:
    def __init__(self):
        self.acesa = False
    
    def ligar(self):
        self.acesa = True
    
    def mostrarEstado(self):
        print("Lâmpada está", "acesa" if self.acesa else "apagada")
    
lampada = Lampada()
lampada.mostrarEstado()
lampada.ligar()
lampada.mostrarEstado()    

class Funcionario:
    def __init__(self, nome, salario):
        self.nome = nome
        self.salario = salario
    
    def mostrarFuncionario(self):
        print("Nome --> Salário")
        print(self.nome, "-->", "R$", self.salario)
        
func1 = Funcionario("Joaquim da Silva", 2500)
func2 = Funcionario("Alice Mendes", 1713)

func1.mostrarFuncionario()
func2.mostrarFuncionario()

#12
class Cachorro:
    def __init__(self, nome):
        self.nome = nome
        
    def latir(self):
        print("Au Au!")

cachorro = Cachorro("Rex")
cachorro.latir()

#13
class Celular:
    def __init__(self, bateria):
        self.bateria = bateria
        
    def carregar(self):
        self.bateria += 1
    
    def completarCarga(self):
        while self.bateria < 100:
            self.carregar()
            print("Carregando...", self.bateria, "%")

celular = Celular(75)
print("Carga atual: ", celular.bateria, "%")
celular.completarCarga()

#14
class Livro:
    def __init__(self, titulo, autor):
        self.titulo = titulo
        self.autor = autor
    
    def mostrarLivro(self):
        print(self.titulo, "- escrito por", self.autor)
    
livro1 =  Livro("Contos de Terror", "Edgar Allan Poe")
livro2 = Livro("Filhos de Húrin", "J.R.R Tolkien")

livro1.mostrarLivro()
livro2.mostrarLivro()

#15
class Aluno:
    def __init__(self, nome, curso):
        self.nome = nome
        self.curso = curso
    
    def mostrarAluno(self):
        print("Aluno", self.nome, "do Curso", self.curso)

aluno1 = Aluno("Arthur Salviano", "Ciências da Computação")
aluno2 = Aluno("Juliano Campos", "Engenharia Química")

aluno1.mostrarAluno()
aluno2.mostrarAluno()

#16
class Conta:
    def __init__(self, nome):
        self.nome = nome
        self.saldo = 0
    
    def depositar(self, valor):
        self.saldo += valor
        print("Saldo atual: R$", self.saldo)
    
    def sacar(self, valor)
        if self.saldo > valor:
            self.saldo -= valor
            print("Saque de R$", valor, "efetuado!")
        else:
            print("Saldo insuficiente!")
        print("Saldo atual: R$", self.saldo)
    
    def mostrarConta(self):
        print("Titular:", self.nome, "| Saldo: R$", self.saldo)

conta = Conta("João Silva")
conta.depositar(150.90)
conta.mostrarConta()

conta.depositar(float(input("Informe o valor do deposito:")))
conta.mostrarConta()

conta.sacar(float(input("Informe o valor para sacar: ")))

#17
class Pessoa:
    def __init__(self, nome):
        self.nome = nome
    
    def falar(self):
        print("Olá, tudo bem?")
    
pessoa = Pessoa("João")
pessoa.falar()

#19
class Carro:
    def __init__(self, marca, modelo, ano):
        self.marca = marca
        self.modelo = modelo
        self.ano = ano
    
    def mostrarCarro(self):
        print("Carro da marca", self.marca, "| Modelo", self.modelo, "| Ano", self.ano)

marca = input("Informe a marca do carro: ")
modelo = input("Informe o modelo do carro: ")
ano = int(input("Informe o ano do carro: "))

carro = Carro(marca, modelo, ano)
carro.mostrarCarro()

#20
class Retangulo:
    def __init__(self, altura, largura):
        self.altura = altura
        self.largura = largura
    
    def area(self):
        area = self.altura * self.largura
        return area
    
    def mostrarRetangulo(self):
        print("A área do seu retângulo é:", self.area())

retangulo = Retangulo(10, 20)
retangulo.mostrarRetangulo()

#21
class Aluno:
    def __init__(self, nome, nota1=0, nota2=0):
        self.nome = nome
        self.nota1 = nota1
        self.nota2 = nota2
        self.media = (nota1 + nota2)/2
    
    def mostrarAluno(self):
        print(self.nome, "-", self.media)

aluno = Aluno("Arthur", 7, 8)
aluno.mostrarAluno()

#22
class Produto:
    def __init__(self, nome, preco):
        self.nome = nome
        self.preco = preco
    
    def desconto(self, porcentagem):
        self.preco = self.preco - (self.preco * (porcentagem/100))
        print("Novo preço: R$", self.preco)

p1 = Produto("Biscoito", 5.50)
p1.desconto(10)

#23
class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade
        
    def maior_de_idade(self):
        return self.idade > 18
    
pessoa = Pessoa("João", 19)

print(f"{pessoa.nome} é de maior") if pessoa.maior_de_idade else print("{pessoa.nome} é de menor")

#24
class Banco:
    def __init__(self, clientes):
        self.clientes = clientes
    
    def mostrarClientes(self):
        print("Clientes do banco: ")
        for cliente in self.clientes:
            print(cliente)
            
banco = Banco(["João", "Maria", "Lucio"])
banco.mostrarClientes()

#25
class Motor:
    def __init__(self):
        self.ligado = False
    
    def ligar_motor(self):
        self.ligado = True
        
motor = Motor()
print("O motor está ligado") if motor.ligado else print("O motor está desligado")
motor.ligar_motor()
print("O motor está ligado") if motor.ligado else print("O motor está desligado")

#26
class Casa:
    def __init__(self, cor, tamanho):
        self.cor = cor
        self.tamanho = tamanho
    
    def mostrarCasa(self):
        print(f"A casa é da cor {self.cor} e possui {self.tamanho} metros quadrados.")
        
casa1 = Casa("Amarela", 80.5)
casa1.mostrarCasa()

#27
class Pessoa:
    def __init__(self):
        print("Pessoa foi criada!")

p1 = Pessoa()
p2 = Pessoa()
'''

#28
class Carro:
    def __init__(self, estado):
        self.estado = estado
    
    def mostrarEstado(self):
        print(f"O estado atual do carro é {self.estado}")

c1 = Carro("Seminovo")
c2 = Carro("Novo")

#29
class Computador:
    def __init__(self):
        self.ligado = False
    
    def ligar(self):
        self.ligado = True
    
    
