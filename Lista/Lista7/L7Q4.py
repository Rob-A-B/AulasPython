import sys

arquivo_notas = "notas.txt"
try:
    f = open(arquivo_notas)
    alunos = f.readlines()
#Alocando os valores lidos do arquivo em listas, onde o primeiro é o nome e o resto nota
    for aluno in alunos:
        aluno = aluno.split(" ")
        nome = aluno[0]
        notas = aluno[1:]
        #Imprimir apenas os com mais de 6 notas
        if (len(notas) > 6):
            print(f"O aluno {nome} tem mais de 6 notas.")
except FileNotFoundError:
    print(f"Arquivo {arquivo_notas} não foi encontrado!")
    sys.exit()