print('Soma dos ímpares múltiplos de 3 entre 0 e 500')
s=0
t = 0
for c in range(1, 501, 2): 
    if c % 3 == 0:
        t += 1
        s += c
print(f'A soma dos {t} números ímpares é {s}')