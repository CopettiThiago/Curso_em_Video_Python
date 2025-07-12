r1 = float(input('Informe o comprimento da primeira reta: '))
r2 = float(input('Informe o comprimento da segunda reta: ' ))
r3 = float(input('Informe o comprimento da terceira reta: '))

if r1 + r2 > r3 and r1 + r3 > r2 and r2 + r3 > r1:
    print('As retas podem formar um triângulo')
    if r1 == r2 == r3:
        print('O triângulo é equilátero')
    elif r1 != r2 != r3 != r1:
        print('O triângulo é escaleno')
    else:
        print('O triângulo é isósceles')
else:
    print('As retas não podem formar um triângulo')