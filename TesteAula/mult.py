def multiplicacao(num,multiplicador):
	resp=num*multiplicador
	return resp


multiplicador = int(input())
resp = 0
for num in range(11):
	resp=multiplicacao(num,multiplicador)
	print('{} x {} = {}'.format(num, multiplicador, resp))
