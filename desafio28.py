from random import randint
from time import sleep

print('--==--' * 15)
print('Vou pensar em um numero entre 0 e 5, tente adivinhar!')
print('--==--' * 15)
numero = int(input('Digite um número entre 0 e 5 :'))
print('PROCESSANDO...')
sleep(3) # espera 3 segundos

aleatorio = randint(0, 5) # gera um numero aleatorio entre 0 e 5

if numero == aleatorio:
    print(f'Você acertou, o número era {numero}')
else:
    print(f'Você errou, o número era {aleatorio} e você escolheu {numero}')
