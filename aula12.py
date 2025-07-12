# Condições aninhadas

nome = str(input('Digite seu nome : '))

if nome == 'Thiago':
    print('Seu nome é muito bonito')
elif nome == 'Jonatan' or nome == 'Ana' or nome == 'Cris':
    print('Seu nome é comum no Brasil')
elif nome in 'Jéssica Cláudia Juliana ':
    print('Que belo nome feminino')
else:
    print('Seu nome é nem normal')

print(f'É um prazer te conhecer, {nome}')