num = (int(input('Digite um número : ')) ,
        int(input('Digite outro número : ')),
        int(input('Digite mais um número : ')),
        int(input('Digite o último número :')))
print(f'Você digitou os valores {num}')
if num.count(9) == 1:
    print('O número 9 apareceu apenas uma vez')
elif num.count(9) == 0:
    print('O número 9 não foi digitado nenhuma vez.')
else:
    print(f'O número 9 foi digitado {num.count(9)} vezes')

if 3 in num:
    print(f'O número 3 foi digitado na {num.index(3)+1}ª posição')
else:
    print('O número 3 não foi digitado')

cont=0
for i in num:
    if i % 2 == 0:
        cont+=1

if cont == 0:
    print('Não foram digitados números pares')
else:
    print('Os números pares digitados foram :', end=' ')
    for n in num:
        if n % 2 == 0:
            print(n, end=' ')


#outra solução
# valores = tuple(int(input('Digite valores '))for c in range(1, 5))
# print(f'O numero nove aparece {valores.count(9)} vezes')
# print(f'Valor 3 foi digitado pela primeira vez na {valores.index(3)+1}º posição' if 3 in valores else 'Não foi digitado valor 3')
# print('Valores pares digitados foram', end=' ')
# print({n for n in valores if n % 2 == 0}, end=' ')