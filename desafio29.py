velocidade = int(input('Informe a velocidade do carro :'))

if velocidade > 80:
    print('Você foi multado por excesso de valocidade')
    multa = (velocidade - 80) * 7
    print(f'Você será multado em R$ {multa:.2f} pois excedeu em {velocidade - 80} km/h o limite de velocidade')
else:
    print(f'Você passou a {velocidade} km/h, então esta no limite de velocidade da via')