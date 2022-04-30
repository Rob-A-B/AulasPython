lista1=[[],[],[]]
vetor=[]
soma1=soma0=soma2=0
for i in range(3):
    for j in range(3):
        lista1[i].append(i+j)
for i in range(3):
    print()
    for j in range(3):
        print(lista1[i][j], end="")
        if j==0: soma0+=lista1[i][j]
        if j==1: soma1+=lista1[i][j]
        if j==2: soma2+=lista1[i][j]
print()

vetor=[soma0,soma1,soma2]