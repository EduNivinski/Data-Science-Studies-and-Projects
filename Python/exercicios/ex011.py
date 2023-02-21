# Faça um programa que leia a lar e alt de uma parede em metros, calcule sua area, e a quantidade
# de tinta necessaria para pinta-la, sabendo que cada litro de tinta pinta uma area de 2m²

lar = float(input('Indique a largura de sua parede: '))
alt = float(input('Indique a altura de sua parede: '))
area = lar * alt
rendimento = 2

print(f'Sua parece tem a dimensão de {lar:.0f}m x {alt:.0f}m e sua área é de {area:.0f}m².')
print(f'Para pintar essa parede é necessário {area/2:.0f} litros de tinta.')