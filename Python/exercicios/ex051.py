# um código que peça o primeiro termo de uma PA e sua razão e apresente a lista dos 10 primeiros termos da PA

print('='*15)
print(f'10 PRIMEIROS TERMOS DE UMA PA')
print('='*15)

n = int(input('Primeiro termo: '))
r = int(input('Razão: '))

for c in range(1,11):
    print(f'{n} > ', end='')
    n += r

print('ACABOU')