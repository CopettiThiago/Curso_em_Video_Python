import random

print('-' * 20)
print('Jogo Jokenpo')
print('-' * 20)

jogador = str(input('Você escolhe pedra, papel ou tesoura ? : ')).lower()
maquina = random.choice(['pedra', 'papel', 'tesoura'])

if maquina == 'pedra' and jogador == 'pedra' or maquina == 'papel' and jogador == 'papel' or maquina == 'tesoura' and jogador == 'tesoura':
    print(f'O computador escolheu {maquina} e você escolheu {jogador}, portanto, Jogo empatado')
elif maquina == 'pedra' and jogador == 'tesoura':
    print(f'Você perdeu, pois o computador escolheu {maquina} e você escolheu {jogador}')
elif maquina == 'pedra' and jogador == 'papel':
    print(f'Você ganhou, pois o computador escolheu {maquina} e você escolheu {jogador}')
elif maquina == 'papel' and jogador == 'pedra':
    print(f'Você perdeu, pois o computador escolheu {maquina} e você escolheu {jogador}')
elif maquina == 'papel' and jogador == 'tesoura':
    print(f'Você ganhou, pois o computador escolheu {maquina} e você escolheu {jogador}')
elif maquina == 'tesoura' and jogador == 'pedra':
    print(f'Você ganhou, pois o computador escolheu {maquina} e você escolheu {jogador}')
elif maquina == 'tesoura' and jogador == 'papel':
    print(f'Você perdeu, pois o computador escolheu {maquina} e você escolheu {jogador}')
