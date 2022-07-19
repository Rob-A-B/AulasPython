import random
numeros = []

def sorteia():
    global numeros
    for _ in range(10):
        numeros.append(random.randint(0, 200))

def operacao():
    global numeros
    pares = []
    impares = []
    for i in numeros:
        if (i % 2 == 0):
            pares.append(i)
        else:
            impares.append(i)
    print(f"Soma dos impares: {sum(impares)}")
    print(f"Subtração dos pares: {0-sum(pares)}")

#A entrada é gerada pelo programa, logo não há chance de erro, não sendo necessaria seu tratamento
sorteia()
print(f"Lista sorteada: {numeros}")
operacao()