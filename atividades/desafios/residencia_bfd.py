#1
class Produto:
    def __init__(self, nome, preco, quantidade):
        self.nome = nome
        self.preco = preco
        self.quantidade = quantidade
    
    def valor_total_estoque(self):
        print(self.nome)
        print("Valor total em estoque: ", self.preco * self.quantidade, "\n")
        return self.preco * self.quantidade
    
produto1 = Produto("Arroz Parbolizado", 2.89, 213)
produto2 = Produto("Feijão", 5.49, 75)
produto3 = Produto("Cream Cracker", 4.50, 100)

produto1.valor_total_estoque()
produto2.valor_total_estoque()
produto3.valor_total_estoque()

#2
class ContaBancaria:
    def __init__(self, nome, saldo=0):
        self.nome = nome
        self.saldo = saldo
    
    def depositar(self, valor):
        self.saldo += valor
        print(f"Depósito de R$ {valor:.2f} efetuado com sucesso\n")
    
    def sacar(self, valor):
        if valor > self.saldo:
            print(f"Valor de saque indisponível, saldo atual é de R$ {self.saldo:.2f}")
            return False

        self.saldo -= valor
        print(f"Saque de R$ {valor:.2f} efetuado com sucesso!")
        print(f"Novo saldo: R$ {self.saldo:.2f}\n")
    
    def mostrar_saldo(self):
        print(f"Saldo disponível: R$ {self.saldo:.2f}\n")
        
c1 = ContaBancaria("João Lucas", 320)
c2 = ContaBancaria("Maria Neves")

c1.mostrar_saldo()
c1.depositar(50)
c1.sacar(400)

c2.mostrar_saldo()
c2.depositar(150.60)
c2.sacar(120.19)


#3
class Funcionario:
    def __init__(self, nome, valor_vendas=0, salario=0):
        self.nome = nome
        self.valor_vendas = valor_vendas
        self.salario = salario
    
    def mostrar_salario(self):
        print(f"Total de Vendas de {self.nome}: R$ {self.valor_vendas:.2f}")
        print(f"Salário: R$ {self.salario:.2f}")
    
class Vendedor(Funcionario):
    def __init__(self, nome, valor_vendas=0, salario=0):
        super().__init__(nome, valor_vendas, salario)
        self.salario = self.calcular_salario()
    
    def calcular_salario(self):
        return 1000 + self.valor_vendas * 0.1 # Fixo + comissão

class Gerente(Funcionario):
    def __init__(self, nome, valor_vendas=0, salario=0):
        super().__init__(nome, valor_vendas, salario)
        self.salario = self.calcular_salario()
    
    def calcular_salario(self):
        return 1000 + self.valor_vendas * 0.2

vendedor1 = Vendedor("Júnior", 7685.60)
vendedor1.mostrar_salario()

gerente = Gerente("Miguel", 6550.0)
gerente.mostrar_salario()

#4
class Carrinho:
    def __init__(self):
        self.lista_itens = []
    
    def adicionar_item(self, produto):
        self.lista_itens.append(produto)
        print(f"\n{produto.nome} adicionado ao carrinho!")
    
    def remover_item(self, nome):
        for produto in self.lista_itens:
            if produto.nome == nome:
                self.lista_itens.remove(produto)
                return f"Produto {produto.nome} removido com sucesso"
        
        return f"{produto.nome} não encontrado"
    
    def calcular_total(self):
        total = 0
        for produto in self.lista_itens:
            total += produto.preco
        
        print("Total: R$", total)
        return total
    
carrinho = Carrinho()
carrinho.adicionar_item(produto1)
carrinho.adicionar_item(produto2)
carrinho.calcular_total()
print(carrinho.remover_item(produto1.nome)) #Remover por nome
carrinho.calcular_total()

class Contato:
    def __init__(self, nome, numero):
        self.nome = nome
        self.numero = numero

class Agenda:
    def __init__(self):
        self.lista_telefonica = []
    
    def adicionar(self, contato):
        self.lista_telefonica.append(contato)
        print("Contato adicionado!")
    
    def buscar(self, nome):
        for contato in self.lista_telefonica:
            if contato.nome == nome:
                return contato.numero

        return "Contato não encontrado"

    def listar_todos(self):
        print("\nLista Telefônica:")
        for contato in self.lista_telefonica:
            print(f"{contato.nome}  -->  {contato.numero}")

contato1 = Contato("Arthur", "83987451235")
contato2 = Contato("Lucio", "83988452465")

agenda = Agenda()
agenda.adicionar(contato1)
agenda.adicionar(contato2)

agenda.listar_todos()

print(agenda.buscar("Arthur"))