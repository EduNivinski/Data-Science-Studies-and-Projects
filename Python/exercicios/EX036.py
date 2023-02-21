# Escreva um programa para aprovar um empréstimo bancpario para compra de uma casa. Pergunte o valor da casa
# o salario do comprador e enquantos anos ele vai pagar. A prestação mensal não pode exceder 30% do salários, ou
# se não o empréstimo será negado!

casa = float(input('Valor da casa: '))
salario = float(input('Salário do comprador: '))
anos = int(input('Quantos anos de financiamento? '))
finan = casa/(anos*12)

print(f'Para pagar uma casa de R${casa:.0f} em {anos:.0f} anos a prestação será de R${finan:.2f}')

if finan > 0.3*salario:
    print('Empréstimo NEGADO')
else:
    print('Empréstimo APROVADO')