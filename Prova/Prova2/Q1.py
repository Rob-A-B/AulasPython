resposta=[]
suspeita=0

print("Conhece a vítima do roubo?")
resposta.append(input("responda com 's' ou 'n' \n"))
print("Esteve no local do roubo?")
resposta.append(input("responda com 's' ou 'n' \n"))
print("Mora perto da vítima?")
resposta.append(input("responda com 's' ou 'n' \n"))
print("A vítima lhe devia?")
resposta.append(input("responda com 's' ou 'n'\n"))
print("Já trabalhou com a vítima?")
resposta.append(input("responda com 's' ou 'n'\n"))

#Varrendo a lista, procurando pelas respostas positivas para acrescentar na suspeita
for i,v in enumerate(resposta):
    if v=='s': suspeita+=1


#Saida de dados
if suspeita==2: print("Suspeita")
elif suspeita==3 or suspeita==4: print("Cumplice")
elif suspeita==5: print("Ladrão")
else: print("Inocente")