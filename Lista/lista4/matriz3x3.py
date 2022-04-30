matriz=[[],[],[]]

for l in range(3):
    for c in range(3):
        matriz[l].append(int(input(f"Digite um  numero para a posicao [{l},{c}] : ")))
for l in range(3):
    for c in range(3):
        print(matriz[l][c], end="")
    print()
