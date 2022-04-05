pedido=input("deseja realizar um pedido? [S] ou [N]\n")
soma=almoco=rodizio=sobremesa=agua=0
while pedido=='S':
    codigo=input("Digite o codigo do produto desejado\n")
    if codigo =='1':
        almoco+=1
    if codigo == '2':
        rodizio+=1
    if codigo =='3':
        sobremesa+=1
    if codigo=='4' :
        agua+=1
    pedido = input("deseja realizar um NOVO pedido? [S] ou [N]\n")
if pedido=='N':
    preco1=15.00
    preco2=39.90
    preco3=5.5
    preco4=2.00
    conta=(almoco*preco1) + (rodizio*preco2) + (sobremesa*preco3) + (agua*preco4)
    if(conta!=0):
        pagamento=input("Debito ou crédito? Digite [D] ou [C]")
        if pagamento=='D':
            conta=conta*0.9
        print(conta)
