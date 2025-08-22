from random import randint
from time import sleep

print('JOGA NA MEGA SENA'.center(30))

lista = []
jogos = []

quant = int(input('Quantos jogos vocÊ quer que eu sorteie ? '))

print('-=' *20)
print('JOGO NA MEGA SENA'.center(30))
print('-=' *20)

total = 1

while total <= quant:
    cont=0
    while True:
        num = randint(1, 61)
        if num not in lista:
            lista.append(num)
            cont+= 1
        if cont >= 6:
            break
    lista.sort()
    jogos.append(lista[:])
    lista.clear()
    total += 1
print('-=' *3, f'Sorteando {quant} jogos'.center(30), '-='*3)
for i, l in enumerate(jogos):
    print(f'Jogo {i+1} : {l}')
    sleep(1)
print('-=' * 5, '< BOA SORTE >', '-=' *5)

# import random
# for x in range(int(input('Number of games: '))):
#     print(f'Game {x+1}: {random.sample(range(1, 60), 6)}')
    