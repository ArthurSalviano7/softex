#1
'''
num = float(input("Informe um número: "))
if num > 10:
    print("Número maior que 10")
else:
    print("Número menor ou igual a 10")
    
#2
num = float(input("Informe um número: "))
if num >= 0:
    print("Número positivo!")
else:
    print("Número negativo!")

#3
num = float(input("Informe um número: "))
if num %2 == 0:
    print("Número é Par")
else:
    print("Número é Ímpar")
    
#4
idade = int(input("Informe sua idade: "))
if idade >= 18:
    print("Maior de idade!")
else:
    print("Menor de idade!")

#5
senha_correta = "2324"
senha = input("Informe uma senha: ")
if senha == senha_correta:
    print("Senha correta, acesso liberado!")
else:
    print("Senha incorreta, acesso negado!")

#6
num1 = float(input("Informe um número: "))
num2 = float(input("Informe outro número: "))
if num1 > num2:
    print(f"O maior número é {num1}")
else:
    print(f"O maior número é {num2}")

#7
num1 = float(input("Informe um número: "))
num2 = float(input("Informe outro número: "))
num3 = float(input("Informe outro número: "))

if num1 > num2 and num1 > num3:
    print(f"O maior número é {num1}")
elif num2 > num3 and num2 > num1:
    print(f"O maior número é {num2}")
elif num3 > num1 and num3 > num2:
    print(f"O maior número é {num3}")

#8 
nota = float(input("Informe a nota do aluno: "))
if nota >= 7:
    print("Aluno aprovado!")
elif nota < 4:
    print("Aluno reprovado!")
else:
    print("Aluno em recuperação!")
    
#9
idade = int(input("Informe sua idade"))
if idade < 12:
    print("Criança!")
elif idade < 18:
    print("Adolescente!")
elif idade < 60:
    print("Adulto!")
else:
    print("Idoso!")
    
#10
temp =  float(input("Informa a temperatura em ºC"))
if temp <= 20:
    print("Frio")
elif temp > 20 and temp <= 40:
    print("Quente")
else:
    print("Muito Quente!")
    
#11
hora = int(input("Digite a hora que suas aulas começam: "))
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
num = int(input("Infome um número: "))
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
letra = input("Digite uma letra: ")
if letra == "a" or letra == "e" or letra == "i" or letra == "o" or letra == "u":
    print("Vogal")
else:
    print("Consoante") 

#16
num1 = int(input("Digite número 1:"))
num2 = int(input("Digite número 2: "))
if num1 < num2:
    print("o menor é ", num1)
else:
    print("o menor é ", num2)
'''
n1 = int(input("Informe o tamanho do lado 1:"))
n2 = int(input("Informe o tamanho do lado 2:"))
n3 = int(input("Informe o tamanho do lado 3:"))

if n1 == n2 == n3:
    print("Triângulo Equilátero!")
elif n1 != n2 != n3:
    print("Triângulo Escaleno")
else:
    print("Triângulo isóceles")

