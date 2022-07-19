pessoa=dict()
turma=list()
velhos=[]
total=mlv=0
while True:
    pessoa.clear()
    pessoa["idade"]=int(input())
    velhos.append(pessoa["idade"])
    if pessoa["idade"]==-1:break
    parametros=input()
    chaves=parametros.split()
    pessoa["sexo"]=chaves[0]
    pessoa["cabelo"]=chaves[1]
    pessoa["olho"]=chaves[2]
    total+=1
    if pessoa["sexo"]=='m' and pessoa["olho"]=='v' and pessoa["cabelo"]=='l' and pessoa["idade"]>=18 and pessoa["idade"]=<35:
        mlv+=1
    turma.append(pessoa.copy())
p=mlv/total
print(f"Mais velho: {max(velhos)}")
print(f"Mulheres com olhos verdes, loiras com 18 a 35 anos: {p:.2%}")
