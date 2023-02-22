# UM PROGRAMA QUE APRESENTE TODOS OS NÚMEROS PARES DE 0 A 50

pares = ()

for n in range(1, 51):
    if (n%2) == 0:
        print(f'{n}', end=' ')
print('FIM!')
