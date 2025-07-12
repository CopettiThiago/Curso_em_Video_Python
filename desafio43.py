peso = float(input('Informe seu peso: '))
altura = float(input('Informe sua altura: '))

imc = peso / (altura * 2)

if imc < 18.5 :
    print(f'Seu IMC é {imc:.2f} e você está abaixo do peso.')
elif imc >=18.5 and imc < 25:
    print(f'Seu IMC é {imc:.2f} e você está no peso ideal')
elif imc >= 25 and imc < 30:
    print(f'Seu IMC é {imc:.2f} e você está com sobrepedo')
elif imc >=30 and imc <= 40 :
    print(f'Seu IMC é {imc:.2f} e você está com obesidade')
else:
    print(f'Seu IMC é {imc:.2f} e você está com obesidade mórbida')

# solução simplificada
# if imc < 18.5:
#     situacao = 'abaixo do peso'
# elif imc < 25:
#     situacao = 'no peso ideal'
# elif imc < 30:
#     situacao = 'com sobrepeso'
# elif imc < 40:
#     situacao = 'com obesidade'
# else:
#     situacao = 'com obesidade mórbida'
# print(f'Seu IMC é {imc:.2f} e você está {situacao}.')

# solução simplificada
'''
peso = float(input('Informe seu peso: '))
altura = float(input('Informe sua altura: '))

imc = peso / (altura * 2)

if imc < 18.5 :
    print(f'Seu IMC é {imc:.2f} e você está abaixo do peso.')
elif 18.5 <= imc < 25:
    print(f'Seu IMC é {imc:.2f} e você está no peso ideal')
elif 25 <= imc < 30:
    print(f'Seu IMC é {imc:.2f} e você está com sobrepeso')
elif 30 <= imc <= 40 :
    print(f'Seu IMC é {imc:.2f} e você está com obesidade')
else:
    print(f'Seu IMC é {imc:.2f} e você está com obesidade mórbida')
'''