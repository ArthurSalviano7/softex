import math

def soma(n1, n2):
    return n1 + n2

def quadrado(x):
    return x*x

def maior(n1, n2):
    return n1 if n1 > n2 else n2

def par(num):
    return num %2 == 0

def media(a, b, c):
    return (a + b + c) / 3

def area_retangulo(lenght, height):
    return lenght * height

def cumprimento(nome):
    return "Olá, " + nome

def dobro(num):
    return 2 * num

def resto_divisao(a, b):
    return a % b

def celsius_para_farenheit(c):
    return 1.8 * c + 32

def hipotenusa(cat1, cat2):
    return math.sqrt(cat1**2 + cat2**2)

def eh_bissexto(ano):
    return ano % 4 == 0

# fatorial 3 = 3 x 2 x 1

def fatorial(num):
    if num == 1:
        return 1
    
    return num * fatorial(num - 1)

def contador_vogais(texto):
    vogais = ['a', 'e', 'i', 'o', 'u']
    qnt = 0
    for letra in texto:
        if letra in vogais:
            qnt += 1    
    
    return qnt

def soma_lista(lista):
    return sum(lista)

def menor_elemento(lista):
    menor = lista[0]
    for num in lista:
        if num < menor:
            menor = num

    return menor

def reverso(texto):
    return texto[::-1]

def imc(peso, altura):
    return peso/(altura**2)

def contar_palavras(frase):
    lista_palavras = frase.split(' ')
    return len(lista_palavras)

def eh_primo(num): # Máximo 1000
    for i in range(2, 1000):
        if num == i:
            continue
        if num % i == 0:
            return False
    
    return True

def maior_string(lista):
    maior = lista[0]
    
    for palavra in lista:
        if len(palavra) > len(maior):
            maior = palavra
    
    return maior

def soma_pares(lista):
    soma = 0
    
    for num in lista:
        if num %2 ==0:
            soma += num
    
    return soma

def filtrar_pares(lista):
    return [x for x in lista if x%2 == 0]

def conversor_tempo(minutos):
    horas = 0
    if minutos > 60:
        horas += 1
        minutos -= 60
    
    texto = f"{horas}h{minutos}min" if horas > 0 else f"{minutos}min"
    return texto

print(maior_string(["texto1", "Computador", "ovo", "palavra", "Anticonstitucionalissimamente"]))
print(soma_pares([9, 5, 4, 6, 2, 1.5]))
print(filtrar_pares([9, 5, 4, 2, 8, 3, 1]))
print(conversor_tempo(93))