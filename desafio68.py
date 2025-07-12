from random import randint
print('=-' * 12)
print('VAMOS JOGAR PAR OU IMPAR')
print('=-' * 12)
v = d = 0
while True:
    pc = randint(0, 10)
    print('-' * 30)
    n = int(input('Diga um valor: '))
    opcao = str(input('PAR OU IMPAR [P/I] : ')).strip().upper()[0]
    print('-' * 30)
    while opcao not in 'PI':
        print('Opção Invalida. Tente novamente.')
        print('-' * 30)
        n = int(input('Diga um valor: '))
        opcao = str(input('PAR OU IMPAR [P/I] : ')).strip().upper()[0]
        print('-' * 30)

    soma = pc + n
    if opcao =='P':
        if soma % 2 == 0:
            print(f'Você jogou {n} e o computador {pc}. Total de {soma} deu PAR')
            v += 1
            print('VOCÊ VENCEU... PARABÉNNSSSSS')
        else:
            print(f'Você jogou {n} e o computador {pc}. Total de {soma} deu ÍMPAR')
            d += 1
            print('VOCÊ PERDEU... GAME OVER...')
    elif opcao == 'I':
        if soma % 2 == 0:
            print(f'Você jogou {n} e o computador {pc}. Total de {soma} deu PAR')
            d += 1
            print('VOCÊ PERDEU... GAME OVER...')
        else:
            print(f'Você jogou {n} e o computador {pc}. Total de {soma} deu ÍMPAR')
            v += 1
            print('VOCÊ VENCEU... PARABÉNNSSSSS')
    print('+-' * 20)
    continua = str(input('Deseja jogar novamente [S/N] :')).strip().upper()[0]
    if continua != 'S':
        break
print('=-' * 12)
print('FIM DO JOGO')
print(f'Você venceu {v} rodada(s) e o computador venceu {d} rodada(s)')

'''
Solução Guanabara
from random import randint
v = 0
while True:
    jogador = int(input('Diga um valor: '))
    computador = randint(0, 10)
    total = jogador + computador
    tipo = ' '
    while tipo not in 'PI':
        tipo = str(input('Par ou Ímpar? [P/I] ')).strip().upper()[0]
    print(f'Você jogou {jogador} e o computador {computador}. Total de {total} ', end='')
    print('DEU PAR' if total % 2 == 0 else 'DEU ÍMPAR')
    if tipo == 'P':
        if total % 2 == 0:
            print('Você VENCEU!')
            v += 1
        else:
            print('Você PERDEU!')
            break
    elif tipo == 'I':
        if total % 2 == 1:
            print('Você VENCEU!')
            v += 1
        else:
            print('Você PERDEU!')
            break
    print('Vamos jogar novamente...')
print(f'GAME OVER! Você venceu {v} vez(es).')





'''