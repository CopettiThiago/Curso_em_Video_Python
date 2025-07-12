numero = int(input('Informe um número: '))
base = str(input('Converter para qual base ? \n 1- Binário \n 2 - Octal \n 3 - Hexadecimal \n Informe sua opção : '))

if base == '1':
    print(f'O número {numero} na base binária é {bin(numero)[2:]}')
elif base == '2':
    print(f'O número {numero} na base octal é {oct(numero)[2:]}')
elif base == '3':
    print(f'O número {numero} na base hexadecimal é {hex(numero)[2:]}')
else:
    print('Opção inválida! Tente novamente.')