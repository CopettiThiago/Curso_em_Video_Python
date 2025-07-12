
maior18 = thomens = mulher20 = 0
while True:
    print('-' * 22)
    print('Cadastre uma pessoa : ')
    print('-' * 22)
    idade = int(input('Idade : '))
    sexo = ' '
    while sexo not in 'MF':
        sexo = str(input('Sexo [M/F] : ')).strip().upper()[0]
    print('-' * 22)
    if idade >= 18:
        maior18 += 1
    if sexo == 'M':
        thomens += 1
    if sexo =='F' and idade < 20:
        mulher20 += 1
    continua = ' '
    while continua not in 'SN':
        continua = str(input('Deseja continuar ? [S/N] : ')).strip().upper()[0]
    if continua == 'N':
        break

print(f'Total de pessoas com mais de 18 anos {maior18}')
print(f'Ao todo temos {thomens} homem(s) cadastrados')
print(f'E temos {mulher20} mulhere(s) com menos de 20 anos')
print('-=' * 30)
print('Muito obrigado por participar do nosso cadastro!')