numero=int(input("Digite se um numero para ver se ele é primo ou não\n"))
#Essa variavel é um operador para contar a ocorrência das duas condições de quando um numero é primo
validade=0

for i in range(1,numero+1):
    if numero%i==0:
        validade+=1

#Como o numero só pode se dividir por 1 e ele mesmo, quando houver essas duas condições o contador validade sera  igual a 2
if(validade==2) : print("é primo\n")
else : print("Não é primo")