numero=[]
maior=[]
menor=[]
igual=[]
for i in range(5):
    print("insira o numero ", i, " \n")
    numero.append(int(input()))
    if i>0:
        if numero[i]>numero[0]:
            maior.append(numero[i])
        elif numero[i]<numero[0]:
            menor.append(numero[i])
        else:
            igual.append(numero[i])
print("Os maiores : ", maior)
print("OS menores : ",menor)
print("Os iguais sao : ",igual)