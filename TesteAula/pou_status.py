import os
from datetime import datetime

# epoch -> tempo em segundos desde 1/1/1970

arquivo_tempo = 'ultimo_tempo.txt'

def tempo_passado():
    if (not os.path.exists(arquivo_tempo)):
        return 0
    with open(arquivo_tempo, "r") as f:
        try:
            last_ts = int(f.read())
        except:
            return 0
    return int(datetime.now().timestamp()) - last_ts

def registrar_tempo():
    with open(arquivo_tempo, "w") as f:
        f.write(str(int(datetime.now().timestamp())))

tempo = tempo_passado()
print(f"O tempo que passou (em segundos) desde a ultima vez que vc rodou esse script é {tempo}")
print(f"O tempo que passou (em minutos) desde a ultima vez que vc rodou esse script é {tempo/60}")
print(f"O tempo que passou (em horas) desde a ultima vez que vc rodou esse script é {tempo/60/60}")
print(f"O tempo que passou (em dias) desde a ultima vez que vc rodou esse script é {tempo/60/60/24}")

print("Guardando o tempo agora...")
registrar_tempo()