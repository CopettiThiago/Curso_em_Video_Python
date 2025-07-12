l1 = float(input('Informe o valor do lado 1 : '))
l2 = float(input('Informe o valor do lado 2 : '))
l3 = float(input('Informe o valor do lado 3 : '))

if l1 < l2 + l3 and l2 < l1 + l3 and l3 < l1 + l2:
    print(f'Com os lados {l1}, {l2} e {l3} podemos formar um triângulo')
    if l1 == l2 == l3 :
        print(f'Com todos os lados iguais, formamos o triângulo Equilátero')
    elif l1 == l2 or l1 ==l3 or l2 == l3 :
        print(f'Com dois lados iguais, formamos o triângulo Isósceles')
    else:
        print(f'Com todos os lados diferentes, formamos o triângulo Escaleno')
else:
    print(f'Com os lados {l1}, {l2} e {l3} não podemos formar um triângulo')
