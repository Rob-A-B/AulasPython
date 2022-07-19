
nomes=list()
sobrenomes=list()
idades=list()
def pular(f):
    f.writeline()


f=open("arquivo Roberto.txt", "w")
N=int(input("Digite a qtd de pessoas"))

#Criação das 3 listas
for i in range(N):
    nomes.append(input("Digite o seu nome\n"))
    sobrenomes.append(input("Digite o sobrenome \n"))
    idades.append(input("Digite a sua idadade\n"))

#Conversao do numero para string, para poder deixar igual a saida de dados pedida
N2=str(N)
f.write(N2+ " pessoas registradas \n")
for j in range(N):
    f.write("Nome: "+nomes[j])
    f.write(" ")
    f.write(sobrenomes[j])
    f.write(" Idade:")
    f.write(idades[j])
    f.write("\n")
#Fechando modo de escrever para poder imprimir via modo de leitura
f.close()
f=open("arquivo Roberto.txt","r")
print(f.read())
f.close()