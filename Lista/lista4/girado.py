matriz = [[],[],[]]
for i, v in enumerate (matriz):
    for k in range(3):     v.append(int(input(f"insere um valor para o {i+1} vetor\n")))

resultado = [sum(v[i] for v in matriz) for i in range(len(matriz))]
print(len(matriz))

print(resultado)