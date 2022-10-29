# Taiiara - 16/10/2022
# Programa que lê um número X de listas e mostra quantas listas tinham somente números Y
# e quantas listas tinham somente números Z

from random import randint

cont = 0
cont0 = 0
cont1 = 0

squares = ([])

while True:
    for square in range(1, 11):
        squares.append(randint(0, 1))
    if sum(squares) == 0:
        cont0 +=1
    elif sum(squares) == 10:
        cont1 += 1
    else:
        cont += 1
    if cont0 == 10 or cont1 == 10:
        break
    squares = ([])

print('-'*100)
print(f'Foram analisadas {cont} listas, cada uma contendo 10 valores de 0 a 1')
print(f'{cont0} listas continham somente o número 0')
print(f'{cont1} listas continham somente o número 1')
print('-'*100)
print(f'{cont0/cont*100:.2f}% das listas são compostas somente de 0')
print(f'{cont1/cont*100:.2f}% das listas são compostas somente de 1')
print('-'*100)
