class Carro:
    def __init__(self, estado):
        self.estado = estado
    
    def mostrar_estado(self):
        print("O estado do carro é", self.estado)
    
carro1 = Carro("Novo")
carro2 = Carro("Usado")

carro1.mostrar_estado()
carro2.mostrar_estado()

#2
class Motor:
    def __init__(self):
        self.ligado = False
    
    def ligar(self):
        self.ligado = True
    
    def mostrar_motor(self):
        print("O motor está ligado!") if self.ligado else print("O motor está desligado!")


motor = Motor()
motor.mostrar_motor()
motor.ligar()
motor.mostrar_motor()

#3
class Banco:
    def __init__(self):
        self.clientes = []
    
    def adicionar_cliente(self, nome):
        self.clientes.append(nome)
    
    def mostrar_clientes(self):
        for cliente in self.clientes:
            print(cliente)

banco = Banco()
banco.adicionar_cliente("Arthur Salviano")
banco.adicionar_cliente("Joaquim Barbosa")
banco.adicionar_cliente("Julio Silva")

print("Clientes: ")
banco.mostrar_clientes()

#4
class Produto:
    def __init__(self, nome, preco):
        self.nome = nome
        self.preco = preco

    def aplicar_desconto(self, desconto):
        preco_antigo = self.preco
        self.preco = self.preco - (self.preco * desconto / 100)

        print(self.nome)
        print(f"{preco_antigo:.2f} ---> {self.preco:.2f}")

produto1 = Produto("Biscoito Maria", 3.50)
produto2 = Produto("Arroz Parbolizado", 3.20)

produto1.aplicar_desconto(10)
produto2.aplicar_desconto(20)
'''Saída:
    Biscoito Maria
    3.50 ---> 3.15
    Arroz Parbolizado
    3.20 ---> 2.56
'''

#5
class Pessoa:
    def __init__(self, nome):
        self.nome = nome
        print("Pessoa criada:", self.nome)

p1 = Pessoa("Arthur")
p2 = Pessoa("Lucio")


#6
def soma(a, b):
    return a + b

print(soma(5, 13))

def soma_pares(lista):
    soma = 0

    for num in lista:
        if num %2 == 0:
            soma += num

    return soma

print("Soma de pares: ", soma_pares([5, 8, 6, 4, 1]))