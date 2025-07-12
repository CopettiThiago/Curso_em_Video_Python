from random import randint

print('-=' * 20)
print('Jogo da adivinhação')
print('-=' * 20)

numero = int(input('Informe um número : '))
aleatorio = randint(0, 10)

cont = 1
while numero != aleatorio:
    cont += 1
    if numero < aleatorio:
        print('Você errou, o número é maior')
    else:
        print('Você errou, o número é menor')
    
    numero = int(input('Informe um número : '))
print(f'Você acertou, era o número {aleatorio} e foram necessárias {cont} tentativas')

#outra alternativa
# from random import randint
#computador = randint(0, 10)
# print('Vou pensar em um número entre 0 e 10. Tente adivinhar...')
#acertou = False
#palpites = 0
#while not acertou:
#   jogador = int(input('Em que número eu pensei? '))
#   palpites += 1
#   if jogador == computador:
#      acertou = True
#   else:
#      if jogador < computador:
#         print('Mais... Tente mais uma vez.')
#      elif jogador > computador:
#         print('Menos... Tente mais uma vez.')
#print(f'Eu pensei no número {computador} e você acertou com {cont} tentativas.')
