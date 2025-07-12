print('Calculando PA')
print('-='* 10)
primeiro = int(input('Informe o primeiro termo: '))
razao = int(input('Informe a razão: '))

decimo = primeiro + (10 -1)*razao

while primeiro <= decimo:
    print(primeiro, end=' -> ')
    primeiro += razao
print('Fim')

# solução sem formula
# print('Calculando PA')
# print('-='* 10)
# primeiro = int(input('Informe o primeiro termo: '))
# razao = int(input('Informe a razão: '))
# termo = primeiro
# cont = 1
#while cont <= 10:
#   print(f'{termo}', end='')
#   termo += razao
#   cont += 1
#print('FIM')