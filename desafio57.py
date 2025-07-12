sexo = str(input('Informe seu sexo [M/F]: ')).strip().upper()

while sexo not in 'MF':
    sexo = str(input('Dados inválidos. Por favor, informe seu sexo [M/F]: ')).strip().upper()
print(f'Sexo {sexo} registrado com sucesso!')

# outra alternativa
'''
 
sexo = str(input('Informe seu sexo [M/F]: ')).strip().upper()

while sexo != 'M' and sexo != 'F':
    sexo = str(input('Dados inválidos. Informe seu sexo [M/F]: ')).strip().upper()
print(f'Sexo {sexo} registrado com sucesso!')
'''

