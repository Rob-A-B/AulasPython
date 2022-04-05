numero=int(input("Digite se um numero para ver se ele é primo ou não"))
validade=0
for i in range(1,numero+1):
    if numero%i==0:
        validade+=1
if(validade<=2) : print("é primo\n")
else : print("Não é primo")