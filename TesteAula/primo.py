def verificar(n):
    print(n)
    primos=[]
    validade=0
    if(n[0] % 2 == 0) and (n[1]%2 == 0) and (n[2]% 2 == 0) and (n[3]% 2 == 0):
        print("SEM PRODUTO")

    else:
        print(n[1]*n[2]*n[0]*n[3])




num = []
frase=[]
frase=input()
numeros=frase.split()

for i in range(4):
    inteiros=int(numeros[i])
    num.append(inteiros)

print()

verificar(num)