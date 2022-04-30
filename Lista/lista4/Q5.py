lista=[[],[],[]]
requisitos=["Salario","Vale-transporte","vale alimentacao"]
for i,v in enumerate(lista):
    print("Funcionario ",i," : ")
    for k in range(3):
        v.append(int(input(f"digite o {requisitos[k]} \n")))
media=total_Vt=0
for k in range(3):
    media+=lista[k][0]
    total_Vt+=lista[k][1]

print(lista)
print(media/3)
print(total_Vt)
