from datetime import date

nasc = int(input('Informe o ano de nascimento: '))

anoatual = date.today().year
idade = anoatual - nasc

if idade <= 9:
    print(f'Você tem {idade} anos e está na categoria Mirim')
elif idade <= 14:
    print(f'Você te {idade} anos e está na categoria Infantil')
elif idade <= 19:
    print(f'Você tem {idade} anos e está na categoria Junior')
elif idade <= 25:
    print(f'Você tem {idade} anos e está na categoria Sênior')
else:
    print(f'Você tem {idade} anos e está na categoria Master')