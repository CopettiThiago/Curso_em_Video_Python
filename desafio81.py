lista = []

while True:
    lista.append(int(input('Digite um valor :')))
    continuar = input('Deseja continuar ? [S/N]').strip().upper()[0]
    if continuar in 'Nn':
        break
print('=-' * 30)
print(f'Você digitou {len(lista)} elementos')
lista.sort(reverse=True)
print(f'Os valores em ordem decrescente são {lista}')
if 5 in lista:
    print('O valor 5 está na lista')
else:
    print('O valor 5 não foi encontrado na lista')
    
    