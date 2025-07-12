# for c in range(0,6): # o último elemento não é contado
#     print('oi')     # sempre cuidar a indentação
#
# for c in range (0, 7, 2): #conta de 1 até 6 com passo 2
#     print(c)
#
# for c in range (6, 0, -1): #conta de 5 até 1 regressivamente por causa do passo -1
#     print(c)
#
# n = int(input('Digite um número : '))
#
# for c in range (0, n+1):
#     print(c)

# i = int(input('Digite o início : '))
# f = int(input('Digite o fim : '))
# p = int(input('Digite o passo : '))
#
# for c in range(i , f, p):
#     print(c)

s = 0
for c in range(0, 4):
    n = int(input('Digite um valor: '))
    s += n
print(f'A soma dos valores é {s}')

