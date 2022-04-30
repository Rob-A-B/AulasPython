A=[]
B=[]
C=[]
for i in range(10):
    A.append(int(input(f"insira o valor {i+1}\n")))
    if A[i]%2==0: B.append(A[i]) #letra a)
    else: C.append(A[i]) #letra b)

print(B)
print(C)