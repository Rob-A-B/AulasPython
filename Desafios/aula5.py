
valor_Produto=float(input("Digite o valor do produto"))
total=valor_Produto
while(valor_Produto!=0):
    valor_Produto=float(input("Digite o novo produto"))
    if (valor_Produto)>0.0:
            total+=valor_Produto
    else :
        print("Invalido!")

print("O total é : ",total)

