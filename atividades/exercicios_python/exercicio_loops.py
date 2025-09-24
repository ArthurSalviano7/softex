'''
#1) 1 até 10
num = 1
while num <= 10:
    print(num)
    num = num + 1

#2) 10 até 1
num = 10
while num >= 1:
    print(num)
    num -= 1

#3) 0 até 20 somente par
num = 0
while num <= 20:
    if num %2 == 0:
        print(num)
    num += 1

#4) 0 até 20 somente ímpar
num = 0
while num <= 20:
    if num %2 != 0:
        print(num)
    num += 1

#5) 1 até num
n = int(input("Insira um número: "))
num = 1
while num <= n:
    print(num)
    num += 1

#6) 5 vezes palavra
palavra = input("Insira um texto: ")
i = 1
while i <= 5:
    print(palavra)
    i += 1

#7 tabuada 2
i = 1
while i <= 10:
    print(f"2 x {i} = {i * 2}")
    i += 1

#8 tabuada n
n = int(input("Insira um número"))
i = 1
while i <= 10:
    print(f"{n} x {i} = {n * i}")
    i += 1

#9 
i = 1
while i <= 5:
    nome = input("Insira um nome: ")
    print(nome)
    i += 1

'''
#10
numero = 0
i = 1
while i <= 5:
    entrada = int(input("Insira um número: "))
    numero += entrada
    i += 1
print("Soma: ", numero)

#11
i = 0
while i <= 50:
    print(i)
    i += 5

#12
n = int(input("Insira um número: "))
num = 0
while num <= n:
    print(num)
    num += 1

#13
