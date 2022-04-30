matriz=[[],[],[]]
soma_Salarial=soma_Diagonal=0
media_Salarial=1.0
for p in range(3):
    if p==0: print("DESENVOLVEDOR DE JAVA: ")
    if p==1: print("ARQUITETO DE SOFTWARE: ")
    if p==2: print("CIENTISTA DE DADOS: ")

    for r in range(3):
        if r==0:    print("Insira o valor do salario medio")
        if r==1:    print("Insira o tempo minimo de experiencia em anos")
        if r==2:    print("Insira o valor da hora")
        matriz[p].append(float(input()))


#imprimindo a matriz
for p in range(3):
    print() # pular linha a cada 3 valores, separando em coluna e linha
    for r in range(3):
        print(f"[{matriz[p][r]}]", end="")              #letra a)
        if r==0:    soma_Salarial+=matriz[p][0]         #letra b) parte 1
        if p == r:    soma_Diagonal += matriz[p][r]     # letra c)


media_Salarial=(soma_Salarial/3) # letra b) parte 2

print()
print("A media salarial é : ",media_Salarial)
print(f"A soma da diagonal é :{soma_Diagonal}")