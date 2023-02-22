# validador de informações corretar usando while loop

r = input('Selecione o seu sexo [M|F]:   ').lower()

while r not in 'mf':
    r = input('Reposta incorreta, por favor, insira apenas as opções M ou F:  ')

print('Agora sim, cachorrão!')