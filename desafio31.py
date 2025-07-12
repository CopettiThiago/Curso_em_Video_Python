distancia = int(input('Qual a distância da sua viagem ? '))

if distancia <= 200:
    valor = distancia * 0.50
    print(f'Para uma viagem de {distancia} km, você vai pagar R$ {valor:.2f}')
else:
    valor = distancia * 0.45
    print(f'Para uma viagem de {distancia} km, você vai pagar R$ {valor:.2f}')


#outras solução
# valor = distancia * 0.50 if distancia <= 200 else distancia * 0.45