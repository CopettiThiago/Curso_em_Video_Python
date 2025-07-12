
media = 0
velho = ''
maior = 0
menor = 0
for c in range(1, 5):
    print(f'-=-=-=- Dados {c+1}ª pessoa -=-=-=-')
    nome = str(input('Informe seu nome : '))
    idade = int(input('Informe sua idade : '))
    sexo = str(input('Informe seu sexo [M/F] : ' )).upper()
    print('-=' * 20)
    media += idade
    if sexo == 'M' and idade > maior:
        maior = idade
        velho = nome
    if sexo == 'F' and idade < 21:
        menor += 1
media = media / 4

print(f'A média do grupo é de {media:.2f} anos')
print(f'O homem mais velho tem {maior} anos e se chama{velho}')
print(f'O grupo tem {menor} mulheres com menos de 21 anos')

# outra solução
# somaidade = 0
# mediaidade = 0
# maioridadehomem = 0
# nomevelho = ''
# totmulher20 = 0
# for p in range(1, 5):
#   print(f'----- {p}ª PESSOA -----')
#   nome = str(input('Nome: ')).strip()
#   idade = int(input('Idade: '))
#   sexo = str(input('Sexo [M/F]: ')).strip()
#   somaidade += idade
#   if p == 1 and sexo in 'Mm':
#     maioridadehomem = idade
#     nomevelho = nome
#   if sexo in 'Mm' and idade > maioridadehomem:
#     maioridadehomem = idade
#     nomevelho = nome
#   if sexo in 'Ff' and idade < 20:
#     totmulher20 += 1
#   mediaidade = somaidade / 4
#   print('-=' * 20)
#print(f'A média de idade do grupo é de {mediaidade:.2f} anos')
#print(f'O homem mais velho tem {maioridadehomem} anos e se chama {nomevelho}')
#print(f'O grupo tem {totmulher20} mulheres com menos de 20 anos')
#
