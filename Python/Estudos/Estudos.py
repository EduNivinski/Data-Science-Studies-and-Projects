#### ESTUDOS
import math

###################################################################################################
# TIPOS PRIMITIVOS
# int
# float
# bool
# str

# Identificando tipos primitivos
n1 = "Olá, Mundo"
n2 = 5
n3 = 5.4

print(f'o n1 é do tipo {type(n1)}, n2 é {type(n2)} e n3 é {type(n3)}!''\n')

# Se você pedir uma variável com valor booleano e não tiver uma variável ele devolve FALSE e
# se houver algo dentro ele devolve TRUE. Pode ser relevante em alguns projetos porque é
# praticamente um IF "curto" sobre a existência ou não de um dado. Ex:
c = bool(input("Digite um valor: "))
print(c)

#outros testes interessantes para entender a validade dos dados inputados
print(n1.isalnum()) # verificar se o valor é numérico
print(n1.isalpha()) # verificar se é alfábetico
print(n1.isalnum())  # verificar se é alfa numérico)
print(n1.isupper()) # verificar se está em letra maiúscula
# chamando a função .is o próprio python sugere outros testes

###################################################################################################

# OPERAÇÕES ARITMÉTICAS
# adição + | subtração - | multiplicação * | divisão /
# exponenciação ** | divisão inteira // | resto da divisão %

# Ordem de Procedencia para as equações e expressões aritméticas:
# 1 > () | 2 > ** | 3 > * ou / ou // ou % | 4 > + ou - |

# É possível executar raiz quadrada forçando o calculo pela divisão. Ex:
a = int(input('Digite um número para descobrir sua raiz quadrada: '))
print(f'Raiz quadrada de {a**(1/2)}')

# Organizando espaçamento de strings no resultado:
nome1 = input('Digite um nome para vê-lo organizado em determinado espaçamento: ')
print(f'Prazer te conhecer {nome1:<20}!')
print(f'Prazer te conhecer {nome1:>20}!')
print(f'Prazer te conhecer {nome1:^20}!')
print(f'Prazer te conhecer {nome1:=^20}!')
print(f'Prazer te conhecer {nome1:+^20}!')

# Para quebrar a linha use \n para manter a linha sem quebrar end=' '
# Para tirar ou adicionar casas decimais no resultado de um número float
b = float(25)
print(f'Há diferentes formas de mostras numeros flots com casas decimais: {b:.0f} | {b:.1f} | {b:.2f}')

###################################################################################################

# UTILIZANDO MÓDULOS
# Métodos são as formas de puxar funcionalidades:
# import method ou from method import função > method.function(variable). Ex:

from math import sqrt
num1 = 25
raiz = math.sqrt(num1)

# Você pode puxar bibliotecas ou métodos através de 'pip install method'
# No site oficial do Python ficam as bibliotecas disponíveis

###################################################################################################

# MANIPULANDO TEXTOS
frase = "Curso em Vídeo Python"
# Cada letra recebe um index, de 0 até o final, que no caso da frase é 20 ou 21 espaços

# FATIAMENTO > Pegar pedaços de uma string
# ex: frase[9] > 'V'       ex: frase[9:13] > 'Víde'       ex: frase[9:21:2]  pulando de 2 em 2
# ex: frase[:5] pega tudo antes do indice 5     ex: frase[5:] começa do cinco e vai até o final
# ex: frase[9::3] começa do 9, vai até o final pulando 3

# Métodos comuns
len(frase) # tamanho da frase = 21
frase.count('o') # contar quantos 'o' tem na string
frase.count('o',0,13) # contar com fatiamento incluído
frase.find("deo") # quantas vezes encontro 'deo', indicando em que posição começou, no caso na posição 11
# se a string procurada pelo find não existe, ela retorna o valor "-1"
# 'curso' in frase  #Existe a palavra na frase? resposta True or False

# Transformação de string > a lista é imutável mas pode ser transformada
frase.replace('Python', 'android')  # vai "substituir" a palavra pela segunra, inclusive criando index
frase.upper()
frase.lower()
frase.capitalize()  # joga todos os caracteres para minusculo e só o primeiro fica em maiúsculo
frase.title()  # analiza quantas palavras tem a string, pela posição dos espaços, e faz captalize em todas as words
frase.strip()  # remove todos os espaços inúteis, sobrando a frente ou atrás, da string, pode usar: rstrip ou lstrip
frase.split()  # onde tem espaço ele cria uma divisão de strings, refazendo os indices, que entram dentro de uma lista
'-'.join(frase)

###################################################################################################

# CONDIÇÕES > IF (se verdadeiro) & ELSE (se falso)
tempo = 19

if tempo <= 5:
    print('Seu carro é novo até')
else:
    print('Seu carro é meio véio')
print('FIM da avaliação do carro!')

# outra forma
print('carro novo'if tempo<=3 else 'carro velho')

# CONDIÇÕES ANINHADAS > IF , ELIF, ELSE
# ESTRUTURAS DE REPETIÇÃO > FOR and WHILE "LOOP"

###################################################################################################

# Variáveis Compostas > Tuplas (), listas [] e dicionários {}
## TUPLAS
lanche = ('hamg', 'banana', 'maça', 'pizza')
print(lanche[2])
print(lanche[-1])
print(lanche[:2])
len(lanche)
for c in lanche:
    print(c)
# tuplas são imutáveis
for position, comida in enumerate(lanche):
    print(f'a comida {comida} está na posição {position}!')   # util para usar index e elemento do index

print(sorted(lanche))    # organizaro resultado da tupla em ordem apenas para visualização
# é possivel somar os elementos de uma tupla a + tupla b por exemplo, na ordem dos elementos somados
lanche.index('maça')    # mostra a posição de index de um elemento dentro da tupla

## LISTAS
lanche = ['pizza', 'refri', 'hamb', 'banana']
# Adicionando elementos
lanche.append('sorvete')   # adicionou um elemento no final da lista e criou o index
print(lanche)
lanche.insert(1, "hotdog")    # adicionou um item no index "1" da lista > movimentou os outros elementos
lanche[3] = 'tapioca'    # altera o elemento do indice 4 para tapioca
# Deletando elementos
del lanche[3]  # apagou o elemento no index 3
lanche.pop(2)
lanche.remove('pizza')  # nesse caso você indica o nome do elemento que deseja apagar
# criar listas
lista = []
valores = list(range(4,11))
valores.sort()   # ordena os valores
valores.sort(reverse=True)    # ordena ao contrário
