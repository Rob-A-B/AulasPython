def escrever(nome):
    f=open(nome+".txt","w")

    frase = (input("Digite a frase: \n"))
    f.write(frase)

    while(frase!="SAIR"):

        frase=(input("Digite a frase: \n"))
        f.write(frase)

    f.close()
def ler(nome):
    f=open(nome,"r")
    f.close()

nome=input("escolha o nome do arquivo")

try:
    escrever(nome)
except:
    print("aceita apenas string")
