#1
nome = "arthur"
print(nome[0])
'''
#2
print(nome[-1])

#3
print(nome[2])

#4
print(nome[-2])

#5
print(nome[0])
print(nome[1])
print(nome[2])
print(nome[3])
print(nome[4])
print(nome[5])

#6
print("Letra 'a' está presente? ")
print("a" in nome)

#7
print("Letra 'x' está presente? ")
print("x" in nome)

#8
print("'art' está presente? ")
print("art" in nome)

#9
print("'tes' está presente? ")
print("tes" in nome)

#10
letra = input("Insira uma letra: ")
print(letra in nome)

#11
print("z não está presente? ")
print("z" not in nome)

#12
print("g não está presente? ")
print("g" not in nome)

#13
print("'ano' está presente?")
print("ano" in nome)

#14
print("'abc' não está presente?")
print('abc' not in nome)

#15
letra = input("Digite uma letra: ")
print(letra not in nome)

#16
print(nome[0:4])

#17
print(nome[-3:])

#18
print(nome[2:6])

#19
print(nome[::-1])

#20 - Exibir apenas posições pares
print("Posições pares: ")
for i in range(len(nome)):
    if i %2 == 0:
        print(nome[i])

#21 - quantas letras 'r'
count_r = 0
for i in range(len(nome)):
    if nome[i] == 'r':
        count_r += 1
print(f"Quantidade de 'r': {count_r}")

#22
letra = input("Infome qual letra buscar: ")
indice = "não encontrado"
for i in range(len(nome)):
    if nome[i] == letra:
        indice = i
        break
print(f"Indice: {indice}")

#23
if nome[0] == 'a' and nome[1] == 'r' and nome[2] =='t':
    print(f"'art' aparece no inicio de {nome}")
else:
    print(f"'art' não aparece no inicio de {nome}")

#24
if nome[-1] == 'r' and nome[-2] == 'u' and nome[-3] == 'h':
    print(f"nome '{nome}' termina com 'hur'")
else:
    print(f"nome '{nome}' não termina com 'hur'") 

#25
for indice, valor in enumerate(nome):
    print(indice, valor)

#26
palavra = input("Informe uma string a ser buscada: ")

if palavra in nome:
    print(f"String {palavra} está dentro de nome {nome}")
else:
    print(f"String {palavra} não está dentro de {nome}")
'''
#27
vogais = ['a', 'e', 'i', 'o', 'u']
print("Vogais: ")
for letra in nome:
    if letra in vogais:
        print(letra)

#28
print("Consoantes: ")
for letra in nome:
    if letra not in vogais:
        print(letra)
    
#29
letra = input("Informe uma letra: ")
count_letra = 0
for i in nome:
    if i == letra:
        count_letra += 1

if count_letra > 1:
    print(f"Existem {count_letra} letras '{letra}' no nome {nome}")
else:
    print(f"São 1 ou menos letras {letra} no nome {nome}")

#30 - Palíndromo
# Ex: arara [a, r, a, r, a]
# comparar nome[0] com nome[-1], [1] == [-2] etc..
if len(nome) %2 == 0: # Não é palíndromo se quantidade de letras é par
    print("Não é palíndromo") 
else:
    index_meio = len(nome) // 2 #  Ex: letra "a" no meio de arara
