lista = []

while True:
    numero = int(input('Digite um valor : '))
    if numero not in lista:
        lista.append(numero)
        print('Valor adicionado com sucesso')
    else:
        print('Número repetido. Não será adicionado')
        
    continuar = input('Deseja continuar ? [S/I] :').strip().upper()[0]
    if continuar != 'S':
        break
    
print('=-' * 30)
lista.sort()
print(f'Você digitou os números {lista}')
        
    