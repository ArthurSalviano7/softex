#1
'''
for i in range(1,11):
    if i == 5:
        break
    print(i)

#2
for i in range(1,11):
    if i % 2 == 0:
        continue
    print(i)

#3
i = 1
while i <= 15:
    print(i)
    i += 1

#4
nomes = ["Arthur", "João", "Alice", "Luís", "Ana Maria"]
for nome in nomes:
    if nome[0] == "A" or nome[0] == "a":
        continue
    print(nome)
#5
for i in range(10, 0, -1):
    if i == 7:
        break
    print(i)
'''
#6
i = 0
while i <= 15:
    if i % 3 == 0:
        continue
    print(i)
    i += 1
#7
numeros = [1, 5, 9, 25, 6, 50, 3, 2, 4]
for num in numeros:
    print(num)
    if num == 50:
        print("Número 50 encontrado!")
        break
#8


