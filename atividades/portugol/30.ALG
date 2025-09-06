Algoritmo "30"

Var
   idade: inteiro
   sexo: caractere

Inicio

   escreval("Informe sua idade: ")
   leia(idade)
   escreval("Informe seu sexo ('M' para masculino e 'F' para feminino): ")
   leia(sexo)

   se (idade >= 18) E ((sexo = "M") OU (sexo = "m")) entao
      escreval("Pode jogar no time masculino!")
   senao
      se (idade >= 18) E ((sexo = "F") OU (sexo = "f")) entao
         escreval("Pode jogar no time feminino!")
      senao
         escreval("Não pode jogar")
      fimse
   fimse


Fimalgoritmo