matriz=[[],[],[]]
regiao=5
trimestre=4
soma=0
for i in range(regiao):
    for j in range(trimestre) :
        matriz.append(int(input("bote a quantidade de vendas\n")))
        soma+=matriz[i][j]
print("houve uma venda de : " , soma)