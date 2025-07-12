media = cont = soma = maior = menor = 0
continua = 'S'

while continua != 'N':
    n = int(input('Digite um número : '))
    cont += 1
    soma += n
    if cont == 1:
        maior = menor = n
    else:
        if n > maior:
            maior = n
        if n < menor:
            menor = n
    continua = str(input('Deseja continuar ? [S/N] ')).strip().upper()[0]
media = soma/cont
print(f'Você digitou {cont} número e a média foi {media:.2f}.')
print(f'O maior valor digitado foi {maior} e o menor foi {menor}.')
print('Fim do programa!')