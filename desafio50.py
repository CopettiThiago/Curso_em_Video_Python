s = 0
cont = 0
for c in range(0, 6):
    n = int(input('Informe um número : '))
    if n % 2 == 0:
        s += n
        cont += 1
print(f'Você digitou {cont} números pares e a soma deles é {s}')