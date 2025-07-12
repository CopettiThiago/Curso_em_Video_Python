n = int(input('Digite um número [999 para sair] : '))
soma = 0
cont = 0
while n != 999:
    soma += n
    cont += 1
    n = int(input('Digite um número [999 para sair] : '))

print(f'Você digitou {cont} e a soma entre eles foi {soma}.')