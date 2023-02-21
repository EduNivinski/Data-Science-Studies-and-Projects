
n = int(input('Digite um número inteiro: '))
print(""" Escolha uma das bases para conversão:
[ 1 ] converter para Binário
[ 2 ] converter para OCTAL
[ 3 ] converter para HEXADECIMAL """)
c = int(input('Sua opção: '))

if c == 1:
    print(f'{n} convertido para BINÁRIO é {bin(n)}')
elif c == 2:
    print(f'{n} convertido para OCTAL é {oct(n)}')
elif c == 3:
    print(f'{n} convertido para HEXADECIMAL é {hex(n)}')
else:
    print('Você escolheu um número inexistente na base')

