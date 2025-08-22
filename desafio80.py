lista = []

for i in range(0,11):
    numero = int(input('Digite um valor : '))
    if i == 0 or numero > lista[-1]:
        lista.append(numero)
    else:
        pos = 0
        while pos < len(lista):
            if numero <= lista[pos]:
                lista.insert(pos, numero)
                break
            pos += 1
print('=-' * 30)
print(f'Os valores digitados foram {lista}')
