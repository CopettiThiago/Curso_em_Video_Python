nome = input('Informe o nome de uma cidade : ')

if 'Santo' or 'santo'or 'SANTO' in nome[:5]:
    print(f'A cidade{nome} começa com {nome[::5]}')
else:
    print(f'A cidade {nome} não começa com Santo')



'''
if nome[:5].lower() == 'santo':
    print('A cidade começa com Santo')
else:
    print('A cidade não começa com Santo')
'''

#outra solução

cidade = str(input('Em que cidade você nasceu? ')).strip()
print(cidade[:5].upper() == 'SANTO')

#resultado apenas True ou False
