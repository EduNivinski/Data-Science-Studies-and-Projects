# escreva um progrmaa que faça o computador pensar em um numero inteiro de 0 a 5, e peça para o usuário tentar descobrir
# qual foi o numero escolhido pelo computador. O programa deverá escrever na tela se o usuário venceu ou perdeu

from random import randint
from time import sleep


print(f'{"-="*30}')
print('Vou pensar em um número de 0 a 5. Tente adivinhar')
print(f'{"-="*30}')

pal = int(input('Em que número eu pensei?'))
n = randint(1,5)

print('PROCESSANDO...')
sleep(2)

if pal == n:
    print("Parabéns! Você acertou o número!")
else:
    print(f'Ganhei! Eu pensei no {n} mas você escolheu {pal}!')