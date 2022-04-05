inicio=int(input("Digite o numero inicial"))
fim=int(input("Digite o numero final"))
cont=inicio
pares=0
while(cont<=fim) :
    if(cont%2==0) :
        pares+=cont
    cont+=1
print(pares)

