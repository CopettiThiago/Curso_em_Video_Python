nome =str(input('Infoeme seu nome : ').strip())
# strip() remove os espaços no início e no final da string

print(f'Seu nomeem maiúsculo é : {nome.upper()}')
print(f'Seu nome em minúsculo é : {nome.lower()}')
print(f'Seu nome tem {len(nome)} caracteres')
print(f'Seu nome tem {len(nome) - nome.count(" ")} letras. ')
# conta quantos caracteres tem no nome, menos os espaços
print(f'Seu primeiro nome é {nome.split()[0]} e ele tem {len(nome.split()[0])} letras. ')
# conta quantos caracteres tem o primeiro nome
print(f'Seu último nome é {nome.split()[-1]} e ele tem {len(nome.split()[-1])} letras. ')
# conta quantos caracteres tem o último nome
print(f'Seu nome tem {nome.find(" ")} letras.')

#outra alternativa
'''
separa = nome.split()
print(f'Seu primeiro nome é {separa[0]} e ele tem {len(separa[0])} letras. ')
print(f'Seu último nome é {separa[-1]} e ele tem {len(separa[-1])} letras. ')
'''
