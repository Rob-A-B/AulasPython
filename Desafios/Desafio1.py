import math
print("Digite uma equação de segundo grau do tipo ax²+bx+c\n")
a = int(input("Digite a\n"))
if(a!=0):
    b= int(input("Digite b\n"))
    c= int(input("Digite c\n"))
    delta = 0
    delta = (b*b) - 4*a*c
    if delta<0: print("Não possui raizes reais")
    elif delta>=0:
        x=(-b+math.sqrt(delta))/(2*a)
        if  delta==0:
            print("x1= ",x)
        else:
            x=(-b -math.sqrt(delta))/(2*a)
            print("x2= ",x)