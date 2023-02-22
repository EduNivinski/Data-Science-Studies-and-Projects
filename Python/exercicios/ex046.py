# montar uma contagem regressiva de 10 segundos e aviso de fogos no final

from time import sleep

for c in range(10,0,-1):
    print(f'{c}')
    sleep(1)

print('BUM! BUM! BUM!')
