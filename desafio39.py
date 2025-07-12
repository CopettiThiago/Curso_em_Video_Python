from datetime import date
anonasc = int(input('Informe seu ano de nascimento: '))
anoatual = date.today().year

idade = anoatual - anonasc

if idade < 18 :
    tempo = 18 - idade
    print(f'Você tem {idade} anos e deve se alistar daqui a {tempo} anos.')
elif idade == 18:
    print(f'Você tem {idade} anos e deve se alistar.')
elif idade > 18:
    tempo = idade - 18
    print(f'Você tem {idade} anos e deveria ter se alistado a {tempo} anos')
    print(f'Você deveria ter se alistado em {anonasc + 18}.')