from datetime import date
ano = int(input('Que ano quer anallisar ? Coloque 0 para o ano atual : '))
if ano == 0:
    ano = date.today().year
if ano % 4 == 0 and (ano % 100 != 0 or ano % 400 == 0):
    print(f'O ano {ano} é bissexto')
else:
    print(f'O ano {ano} não é bissexto')

# o ano é bissexto se for divisível por 4, mas não por 100, ou se for divisível por 400.