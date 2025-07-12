tempo = int(input('Quantos anos tem seu carro ? '))

if tempo<= 3:
    print('Seu carro é novo')
else:
    print('Seu carro é velho')
print('---FIM---')

#condição simplificada
print('Seu carro é novo' if tempo <= 3 else 'Seu carro é velho')