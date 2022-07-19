vetor = []
for i in range(10):
    while True:
        v = input(f"Insira o valor {i+1}: ")
        try:
            v = int(v)
            vetor.append(v)
            break
        except:
            print("Valor inválido!")


menor = []
maior = []
igual = []
for val in vetor[1:]:
    if (val < vetor[0]):
        menor.append(val)
    elif (val > vetor[0]):
        maior.append(val)
    else:
        igual.append(val)

print(f"Valores maiores: {maior}. Tamanho: {len(maior)}")
print(f"Valores menores: {menor}. Tamanho: {len(menor)}")
print(f"Valores iguais: {igual}. Tamanho: {len(igual)}")