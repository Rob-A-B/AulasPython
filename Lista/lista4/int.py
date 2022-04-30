lista1=[[],[],[]]
soma=[0,0,0]
for i in range(3):
    for j in range(3):
        lista1[i].append(int(input(f"digite o valor {i+1} \n")))
for i in range(3):
    print()
    for j in range(3):
        print(f"[{lista1[i][j]:6^}]", end="")
        #if j==0: soma[i]+=lista1[i][j]
       # if j==1: soma[i]+=lista1[i][j]
        #if j==2: soma[i]+=lista1[i][j]
        soma[i] += lista1[i][j]
print()

print(soma)