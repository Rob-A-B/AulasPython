matriz=[[],[],[]]
coluna=[[],[],[]]
soma=0.0
for l in range(3):
    for c in range(3):
        matriz[l].append(int(input(f"Digite um  numero para a posicao [{l},{c}] : ")))
        soma+=matriz[l][c]
for l in range(3):
    for c in range(3):
        print(matriz[l][c], end="")
    print()


for l in range(3):
    print("a soma da coluna",l, "é igual a :", soma)