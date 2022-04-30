matriz=[[],[],[]]
soma =0

for a in range(3):
    for n in range(4):
        matriz[a].append(float(input(f"Digite a nota {n} do aluno {a} : ")))
        soma+=matriz[a][n]
media = soma/12

print(f"A media da turma é : {media}")

