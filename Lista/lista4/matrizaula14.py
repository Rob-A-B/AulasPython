lista1=[[],[],[]]
soma=[0,0,0]
soma_Impares=[]
soma_Primeira=[[],[],[]]
for i in range(3):
    for j in range(3):
        lista1[i].append(int(input(f"digite o valor {i+1} \n")))
        if lista1[i][j]%2!=0: soma_Impares.append(lista1[i][j])
        soma[j].append(lista1[i][j])
for i in range(3):
    print()
    for j in range(3):
        print(f"[{lista1[i][j]}]", end="")

print()
print(sum(soma_Impares))
print(sum(soma))
print(min(lista1[2]))
