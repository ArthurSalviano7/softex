#1
'''
num = float(input("\nInforme um número: "))
if num > 10:
    print("Número maior que 10")
else:
    print("Número menor ou igual a 10")
    
#2
num = float(input("\nInforme um número: "))
if num >= 0:
    print("Número positivo!")
else:
    print("Número negativo!")

#3
num = float(input("\nInforme um número: "))
if num %2 == 0:
    print("Número é Par")
else:
    print("Número é Ímpar")
    
#4
idade = int(input("\nInforme sua idade: "))
if idade >= 18:
    print("Maior de idade!")
else:
    print("Menor de idade!")

#5
senha_correta = "2324"
senha = input("\nInforme uma senha: ")
if senha == senha_correta:
    print("Senha correta, acesso liberado!")
else:
    print("Senha incorreta, acesso negado!")

#6
num1 = float(input("\nInforme um número: "))
num2 = float(input("Informe outro número: "))
if num1 > num2:
    print(f"O maior número é {num1}")
else:
    print(f"O maior número é {num2}")

#7
num1 = float(input("\nInforme um número: "))
num2 = float(input("Informe outro número: "))
num3 = float(input("Informe outro número: "))

if num1 > num2 and num1 > num3:
    print(f"O maior número é {num1}")
elif num2 > num3 and num2 > num1:
    print(f"O maior número é {num2}")
elif num3 > num1 and num3 > num2:
    print(f"O maior número é {num3}")

#8 
nota = float(input("\nInforme a nota do aluno: "))
if nota >= 7:
    print("Aluno aprovado!")
elif nota < 4:
    print("Aluno reprovado!")
else:
    print("Aluno em recuperação!")
    
#9
idade = int(input("\nInforme sua idade"))
if idade < 12:
    print("Criança!")
elif idade < 18:
    print("Adolescente!")
elif idade < 60:
    print("Adulto!")
else:
    print("Idoso!")
    
#10
temp =  float(input("\nInforme a temperatura em ºC"))
if temp <= 20:
    print("Frio")
elif temp > 20 and temp <= 40:
    print("Quente")
else:
    print("Muito Quente!")
    
#11
hora = int(input("\nDigite a hora que suas aulas começam: "))
if hora >= 6 and hora < 12:
    print("Turno matutino!")
elif hora > 12 and hora < 17:
    print("Turno Vespertino")
else:
    print("Turno Noturno!")

#12
vel = float(input("Digite a velocidade em km/h"))
if vel <= 20:
    print("Velocidade lenta")
elif vel > 20 and vel < 40:
    print("Velocidade mediana")
else:
    print("Velocidade rápida")
    
#13
num = int(input("\nInfome um número: "))
if num < 1:
    print("Número menor que 1")
elif num > 100:
    print("Número maior que 100")
else:
    print("Número está entre 1-100")

#14
num1 = int(input("\nInforme um número:"))
num2 = int(input("Informe outro número:"))

print("Iguais") if num1 == num2 else print("Diferentes")

#15
letra = input("\nDigite uma letra: ")
if letra == "a" or letra == "e" or letra == "i" or letra == "o" or letra == "u":
    print("Vogal")
else:
    print("Consoante") 

#16
num1 = int(input("\nDigite número 1:"))
num2 = int(input("Digite número 2: "))
if num1 < num2:
    print("o menor é ", num1)
else:
    print("o menor é ", num2)
'''
#17
n1 = int(input("\nInforme o tamanho do lado 1:"))
n2 = int(input("Informe o tamanho do lado 2:"))
n3 = int(input("Informe o tamanho do lado 3:"))

if n1 == n2 == n3:
    print("Triângulo Equilátero!")
elif n1 != n2 != n3:
    print("Triângulo Escaleno")
else:
    print("Triângulo isóceles")

#18
print("\n--- Calculadora ---")
print("Escolha uma operação (1-4): ")
print("1. Adição\n2. Subtração\n3. Multiplicação\n4. Divisão")
op = int(input())
n1 = float(input("Insira um número: "))
n2 = float(input("Insira um segundo número: "))

if op == 1:
    print("Resultado: ", n1 + n2)
elif op == 2:
    print("Resultado: ", n1 - n2)
elif op == 3:
    print("Resultado: ", n1 * n2)
elif op == 4:
    print("Resultado: ", n1 / n2)
else:
    print("Operação Inválida!")

#19
ano = int(input("\nInsira o ano atual: "))
if ano %4 == 0:
    print("Ano é bissexto!")
else:
    print("Ano não é bissexto!")

#20
num = int(input("\nInsira um número: "))
if num % 3 == 0 and num % 5 == 0:
    print("Número é múltiplo de 3 e 5!")
else:
    print("Não é múltiplo de 3 e 5!")

#21
preco = float(input("\nInsira o valor do produto: "))
desc = float(input("Insira o desconto a ser aplicado (%):"))
print("O valor do produto com desconto aplicado é R$ ", preco - preco*(desc/100))

#22
salario = float(input("\nInforme o salário: "))
if salario < 1518:
    print("Salário menor que o salário-mínimo nacional!")
else:
    print("Salário maior ou igual ao salário-mínimo nacional!")

#23
idade = int(input("\nInforme sua idade: "))
if idade < 18:
    print("Não pode dirigir!")
else:
    print("Pode dirigir!")

#24
n1 = float(input("\nInforma a nota 1:"))
n2 = float(input("Informe a nota 2:"))
print("A média das notas é", (n1 + n2) / 2)

#25
hora = int(input("\nInforme a hora atual (1-24):"))
if hora >= 5 and hora < 12:
    print("Bom dia!")
elif hora >= 12 and hora < 18:
    print("Boa tarde!")
else:
    print("Boa noite!")

#26
idade = int(input("\nInforme sua idade: "))
if idade < 16:
    print("Não pode votar!")
else:
    print("Pode votar!")

#27
num = int(input("\nInsira um número: "))
if num % 2 == 0 and num % 3 == 0:
    print("Número é múltiplo de 2 e 3!")
else:
    print("Não é múltiplo de 2 e 3!")

#28
altura = float(input("\nInsira sua altura: "))
peso = int(input("Insira seu peso: "))
imc = peso / (altura**2)
print(f"\nO IMC calculado é {imc:.2f}")

#30
nome = input("Qual seu nome? ")
nota = float(input("Informe a nota da prova: "))
if nota < 4:
    print(f"O aluno {nome} foi reprovado com nota {nota}")
elif nota >= 7:
    print(f"O aluno {nome} foi aprovado com nota {nota}")
else:
    print(f"O aluno {nome} está em recuperação pois teve nota {nota}")