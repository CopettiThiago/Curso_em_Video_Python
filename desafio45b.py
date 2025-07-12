from random import randint
from time import sleep
print('-=' * 15)
print('JOGO JOKENPO')
print('-=' * 15)

lista = ('pedra', 'papel', 'tesoura')
computador = randint(0, 2)

print('Sua vez de jogar')
print('[ 0 ] Pedra')
print('[ 1 ] Papel')
print('[ 2 ] Tesoura')

jogador = int(input('Informe a sua escolha : '))

print('JO')
sleep(1)
print('KEN')
sleep(1)
print('PO')
sleep(1)

print('-=' * 15)
print(f'O computador escolheu {lista[computador]}')
print(f'O jogador escolheu {lista[jogador]}')
print('-=' * 15)

if computador == 0:
    if jogador == 0:
        print('Jogo Empatado')
    elif jogador == 1:
        print('Jogador Venceu')
    elif jogador == 2:
        print('Computador Venceu')
    else:
        print('Jogada Inválida')
elif computador == 1:
    if jogador == 0:
        print('Computador Venceu')
    elif jogador == 1:
        print('Jogo Empatado')
    elif jogador == 2:
        print('Jogador Venceu')
    else:
        print('Jogada Inválida')
elif computador == 2:
    if jogador == 0:
        print('Jogador Venceu')
    elif jogador == 1:
        print('Computador Venceu')
    elif jogador == 2:
        print('Jogo Empatado')
    else:
        print('Jogada Inválida')