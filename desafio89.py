lista = []
temp = []
while True:
    media = 0
    temp.append(str(input('Nome : ')))
    temp.append(float(input('Nota 1 :')))
    temp.append(float(input('Nota 2 :')))
    media = (temp[1] + temp[2]) / 2
    temp.append(media)
    
    lista.append(temp[:])
    temp.clear()
    continuar = input('Deseja continuar ? [S/N] : ').strip().upper()[0]
    if continuar != 'S':
        break

print('=-'*10)
print('RESULTADO FINAL'.center(20))
print('=-'*10)
print('Nº  NOME       MÉDIA')
print('-'* 20)

for i in enumerate(lista):
    print(f'{i} {lista[i][0]}  {lista[i][3]:.2f}')


print(temp)
print(lista)