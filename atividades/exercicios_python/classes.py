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


