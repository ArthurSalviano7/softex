Algoritmo "25"

Var
senha1, senha2: caractere

Inicio

escreval("Informe a primeira senha: ")
leia(senha1)
escreval("Informe a segunda senha: ")
leia(senha2)

se (senha1 = "1234") E (senha2 = "1234") entao
   escreval("As senhas estão corretas, acesso permitido!")
senao
   escreval("Pelo menos uma senha está incorreta, acesso negado!")
fimse

Fimalgoritmo