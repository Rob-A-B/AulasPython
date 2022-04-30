vetor = []
soma=0
cont_numero=0
for i in range(10):
    vetor.append(int(input("Digite um valor:")))
    soma+=vetor[i]

for i in range(10):
    if i==2:
        cont_numero+=1

media=soma/10
menor=min(vetor)
maior=max(vetor)
posicao=vetor.index(8)
vetor[1]=10

print(f"A soma e media dos vetores são : {soma} e {media}")
print(f"o maior e menor vetor são: {maior} e {menor}")
print(f" o numero 2 aparece {cont_numero} vezes no vetor")
print(f"a posicao do numero 8 é [{posicao}]")
print(vetor)