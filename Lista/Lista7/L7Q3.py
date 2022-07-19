import sys

arquivo = "arquivo_ex3.txt"
while True:
    opcao = input("""Selecione uma Opção    
    1) Ler
    2) Escrever
    3) Exibir soma
    4) Sair
    """)
    if (opcao == "1" or opcao.lower() == "ler"):
        # Abre o arquivo se ela existir, se não printa um erro
        try:
            f = open(arquivo, "r")

            # Imprima o conteudo do arquivo
            print(f"O conteudo do arquivo:\n{f.read()}")
            
            # Feche o arquivo
            f.close()
        except FileNotFoundError:
            # Tratamento da exceção de arquivo não existir
            print("O arquivo não existe!")
    elif (opcao == "2" or opcao.lower() == "escrever"):
        # Abrir o arquivo, se ela não existir cria
        f = open(arquivo, "a+")
        f.seek(0)

        # Ler os valores do arquivo
        valores = f.readlines()

        # Receber o novo valor do usuário
        val = input("Insira o numero: ")
        try:
            # Tente converter para numero
            val = int(val)
        except Exception:
            print(f"Valor inválido!")
        
        # Validar que não existe nemhum numero maior no arquivo
        valido = True
        for v in valores:
            try:
                v = int(v)
            except:
                print(f"Valor {valor} não é um numero válido, ignorando!")

            # Para cada numero contido no arquivo, verificar se ela é maior que o numero dado pelo usuário
            if (val <= v):
                # Se o numero no arquivo for maior, não vamos inserir o numero novo no arquivo
                print(f"O valor {v} é maior que {val} e está contido no arquivo!")
                valido = False
                break
        
        # So insira o nuumero novo se ela for maior que todos que estão no arquivo
        if (valido):
            # insire o numero novo
            f.write(f"{val}\n")

        f.close()
    elif (opcao == "3" or opcao.lower() == "exibir soma" or opcao.lower() == "exibir"):
        # Abra o arquivo
        try:
            f = open(arquivo, "r")
            # Imprima a soma dos valores contidos no arquivo
            soma = 0
            for valor in f.readlines():
                try:
                    soma += int(valor)
                except:
                    print(f"Valor {valor} não é um numero válido, ignorando!")
            print(f"Soma dos valores no arquivo: {soma}")
            f.close()
        except FileNotFoundError:
            print("O arquivo não existe!")
    elif (opcao == "4" or opcao.lower() == "sair"):
        # Encerre o loop
        sys.exit()
    else:
        print("Opção inválida!")