altura=float(input("Digite a altura em metros\n"))
peso=float(input("Digite o peso em kg\n"))
sexo=input("Digite seu sexo 'm' para mulher ou 'h' para homem\n")


if sexo=='h':    ideal=(72.7 * altura) -58
if sexo=='m':    ideal=(62.1 * altura) - 44.7


if peso>ideal: print("Esta a cima do peso")
if peso==ideal: print("Esta no peso ideal")
if peso<ideal: print("Esta a baixo do peso ideal")