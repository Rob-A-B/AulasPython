import wsgiref.validate
from datetime import datetime


f = open("ultimo_tempo.txt", "r")
antes_str=f.read()
antes_int=int(antes_str)
f.close()
now=datetime.now()
agora_int=now.minute
diferenca=agora_int-antes_int
agora_str=str(agora_int)
f = open("ultimo_tempo.txt", "w")
f.write(agora_str)
f.close()
print(diferenca)
