from datetime import date

anoatual = date.today().year
maior = 0
menor = 0
for c in range(0, 7):
    n = int(input(f'Em que ano a {c +1}ª pessoa nasceu? '))
    idade = anoatual - n
    if idade >= 18:
            maior += 1
    else:
            menor += 1
print(f'Maiores de idade: {maior}')
print(f'Menores de idade: {menor}')