numero = input('Digite um número')

n1= numero[3]
n2= numero[2]
n3= numero[1]
n4= numero[0]

print(f'Unidade : ', n1)
print(f'Dezena : ', n2)
print(f'Centena : ', n3)
print(f'Milhar : ', n4)
# o desafio apresenta um erro ao digitar um número com menos de 4 dígitos

numero = input('Digite um número')

u = numero // 1 % 10
d = numero // 10 % 10
c = numero // 100 % 10
m = numero // 1000 % 10

print(f'Unidade : ', u)
print(f'Dezena : ', d)
print(f'Centena : ', c)
print(f'Milhar : ', m)