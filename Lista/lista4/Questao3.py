A=[1,2,3,4,5]
B=[6,7,8,9,10]
soma_Pares=soma_Impares=0
C= A+B

for i in range(len(C)):
    if C[i]%2==0:
        soma_Pares+=C[i]
    else:
        soma_Impares+=C[i]


print(C)
print(soma_Pares)
print(soma_Impares)
print(min(C))