ext = ('zero', 'um', 'dois', 'três', 'quatro', 'cinco',
          'seis', 'sete', 'oito', 'nove', 'dez', 'onze', 'doze',
          'treze', 'quatorze', 'quinze', 'dezesseis', 'dezesete',
          'dezoito', 'dezenove', 'vinte')

while True:
    while True:
        num = int(input('Digite um número entre 0 e 20: '))
        if 0 <= num <= 20:
            break
        print('Tente novamente.', end=' ')
    print(f'O número {num} por extenso é {ext[num]}')
    continua = str(input('Deseja continuar ? [S/N] : ')).upper().strip()
    if continua == 'N':
        break
print('Fim do programa!')