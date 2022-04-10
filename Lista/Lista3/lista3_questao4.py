#Fiz de acordo com o teorema matematico, que CADA reta deve ser MENOR que a soma dos lados do triangulo

reta1=float(input("Digite o tamanho da reta1\n"))
reta2=float(input("Digite o tamanho da reta2\n"))
reta3=float(input("Digite o tamanho da reta3\n"))

soma1=reta2+reta3
soma2=reta1+reta3
soma3=reta1+reta2

print(soma1)
print(soma2)
print(soma3)

relacao1=reta1<soma1
relacao2=reta2<soma2
relacao3=reta3<soma3

if(relacao1 and relacao2 and relacao3): print("é um triangulo\n")
else: print("Não é um triangulo")


