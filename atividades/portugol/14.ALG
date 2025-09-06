Algoritmo "questao_14"

Var
nota_1, nota_2, nota_3, media: real
presenca: inteiro

Inicio

escreval("Qual a presença do aluno (0-100):")
leia(presenca)

escreval("Informe as três notas (uma por vez): ")
leia(nota_1, nota_2, nota_3)

media <- (nota_1 + nota_2 + nota_3)/3

se (media >= 7) e (presenca >= 75) entao
   escreval("O aluno foi aprovado!")
   escreval("Média: ", media:10:2)
senao
     escreval("O aluno foi reprovado!")
fimse

Fimalgoritmo