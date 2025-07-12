print('Calculando PA')
print('-='* 10)
primeiro = int(input('Informe o primeiro termo: '))
razao = int(input('Informe a razão: '))
termo = primeiro
cont = 1
total = 0
mais = 10
while mais != 0:
    total = total + mais
    while cont <= total:
        print(f'{termo} -> ', end= '')
        termo += razao
        cont += 1
    print('PAUSA')
    mais = int(input('Quantos termos você quer mostras a mais ? '))
print(f'Progressão finalizada com {total} termos mostrados')
print('FIM')