funcionarios =int(input("Digite a quantidade de funcionarios\n"))

for i in range(funcionarios):
    salario=float(input("Digite o seu salario\n"))

    if salario<3000: salario=salario*1.1
    elif (salario>3000) and (salario<5000) : salario=salario*1.2
    elif salario>5000 and salario<7000 : salario=salario*1.3
    else : salario=salario*1.35

    print("O novo salario é: ",salario)