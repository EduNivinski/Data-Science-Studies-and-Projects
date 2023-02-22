# calcule a soma entre todos os numeros impares que são multiplos de 3 e estão no intervalo de 1 até 500

soma = 0
for n in range(1, 500):
    if n % 2 != 0:
        if n % 3 == 0:
            soma += n

print(f'A soma dos números desehados é {soma}!')