'''
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

'''

#6
class Usuario:
    def __init__(self, usuario, senha):
        self.usuario = usuario
        self.senha = senha

    def autenticar(self, usuario, senha):
        if self.usuario == usuario and self.senha == senha:
            print("Login efetuado!")
            return True
        print("Usuario ou senha incorretos!")
        return False

usuario = Usuario("Arthur33", "senha4562")

usuario.autenticar("Arthur33", "124862")
usuario.autenticar("Arthur33", "senha4562")

# 7. Classe Aluno com Média
class Aluno:
    def __init__(self, nome, nota1, nota2):
        self.nome = nome
        self.nota1 = nota1
        self.nota2 = nota2

    def calcular_media(self):
        return (self.nota1 + self.nota2) / 2

aluno = Aluno("Alisson", 8.5, 9.0)
aluno2 = Aluno("Arthur", 7.0, 6.5)

print(f"Aluno: {aluno.nome} | Média: {aluno.calcular_media()}")
print(f"Aluno: {aluno2.nome} | Média: {aluno2.calcular_media()}")

# 8. Biblioteca
class Livro:
    def __init__(self, titulo, autor):
        self.titulo = titulo
        self.autor = autor

class Biblioteca:
    def __init__(self):
        self.livros = []

    def cadastrar_livro(self, livro):
        self.livros.append(livro)

    def listar_por_autor(self, autor):
        return [l.titulo for l in self.livros if l.autor == autor]

    def buscar_por_titulo(self, titulo):
        for l in self.livros:
            if l.titulo == titulo:
                return l.titulo, l.autor
        return None

biblioteca = Biblioteca()
livro = Livro("Dom Quixote", "Miguel Cervantes")

biblioteca.cadastrar_livro(livro)
print(biblioteca.buscar_por_titulo("Dom Quixote"))

# 9. Sistema de Pedidos
class Produto:
    def __init__(self, nome, preco):
        self.nome = nome
        self.preco = preco

class ItemPedido:
    def __init__(self, produto, quantidade):
        self.produto = produto
        self.quantidade = quantidade

    def subtotal(self):
        return self.produto.preco * self.quantidade

class Pedido:
    def __init__(self):
        self.itens = []

    def adicionar_item(self, item):
        self.itens.append(item)

    def calcular_total(self):
        return sum(item.subtotal() for item in self.itens)

# 10
class Personagem:
    def __init__(self, nome, vida, dano):
        self.nome = nome
        self.vida = vida
        self.dano = dano

    def atacar(self, outro):
        outro.vida -= self.dano
        print(f"{self.nome} atacou {outro.nome}! Vida de {outro.nome}: {outro.vida}")

p1 = Personagem("Guerreiro", 100, 20)
p2 = Personagem("Mago", 80, 25)

while p1.vida > 0 and p2.vida > 0:
    p1.atacar(p2)
    if p2.vida <= 0: break
    p2.atacar(p1)

# 11. Classe Carro
class Carro:
    def __init__(self):
        self.ligado = False
        self.velocidade = 0

    def ligar(self):
        self.ligado = True
        print("Carro ligado.")

    def desligar(self):
        self.ligado = False
        self.velocidade = 0
        print("Carro desligado.")

    def acelerar(self):
        if self.ligado:
            self.velocidade += 10
            print(f"Velocidade: {self.velocidade}")

    def frear(self):
        if self.velocidade > 0:
            self.velocidade -= 10
            print(f"Velocidade: {self.velocidade}")

meu_carro = Carro()
meu_carro.ligar()
meu_carro.acelerar()
meu_carro.acelerar()
meu_carro.frear()
meu_carro.desligar()