# crie um jogo de adivinhação, onde o computador escolhe u, número de 0 a 10 e você
# tem que adivinhar, mas recebe palpites

from time import sleep
from random import randint

print('Sou seu computador...')
sleep(0.5)
print('Acabei de pensar em um número de 0 a 10... Você consegue adivinhar qual foi?')

palpite = 0
numero = randint(1, 10)
chances = 0

while palpite != numero:
    palpite = int(input('Qual é o seu palpite? '))
    if palpite > numero:
        print('Quase! Mas na verdade meu número é MENOR!')
    if palpite < numero:
        print('Quase! Mas na verdade meu número é MAIOR!')
    chances += 1
print(f'Parabéns! Você acertou com {chances} chances!')