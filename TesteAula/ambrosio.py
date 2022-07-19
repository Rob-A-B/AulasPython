tabela ={1:5.3,2:6.00,3:3.2,4:2.5}

cod=int(input())
qtd=int(input())

total=cod*qtd

if qtd>15 or total>=40:
    total=total*0.85
