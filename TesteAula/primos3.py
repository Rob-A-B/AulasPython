def verificar(n):
    primos=[]
    validade=0

    for j in range(4):
        for k in range(n[j]):
            if n[j]%(k+1)==0:
                validade+=1

        if validade == 2:
            primos.append(n[j])
            validade=0
        else: validade=0
    produto = 1
    for l in range(len(primos)):
        produto *= primos[l]
    print(produto)




num = []
frase=[]
frase=input()
numeros=frase.split()

for i in range(4):
    inteiros=int(numeros[i])
    num.append(inteiros)


verificar(num)