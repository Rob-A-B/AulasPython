matriz =[[],[],[],[]]
regiao1=regiao2=regiao3=regiao4=regiao5=0.0
soma=0
regiao=[0,0,0,0]
for t in range(4):

    for r in range(5):
       # matriz[t].append(float(input(f"insira q quantidade de vendas do semestre {t+1} da região {r+1}: ")))
       matriz[t].append(r+t)
       print(f"insira q quantidade de vendas do semestre {t+1} da região {r+1}: ")
       print(r+t)
       soma+=matriz[t][r]

       #print("-----------------------\n->",regiao1,"\n-------------------")

#regiao[0]+=matriz[t][0]
#regiao[1]+=matriz[t][1]
#regiao[2]+=matriz[t][2]
#regiao[3]+=matriz[t][3]
#regiao[4]+=matriz[t][4]
print(f" o total de vendas é : {soma}")

for t in range(5):
    #print(f" na regiao {i+1} é igual a : {regiao[i]}")
    regiao1 += matriz[t][0]
    print(matriz[t][0])
    #print("-----------------------\n->", regiao1, "\n-------------------")
print("oi")