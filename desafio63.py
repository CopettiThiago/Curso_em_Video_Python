print('-' *23)
print('Sequência de Fibonacci')
print('-' *23)

n = int(input('Quantos termos você quer mostrar? '))

cont = 3
t1 = 0
t2 = 1
print('~' * (n * 5))
print(f'{t1} -> {t2} -> ', end='')
while cont <= n:
    t3 = t1 + t2
    print(f'{t3} -> ', end='')
    t1 = t2
    t2 = t3
    cont+= 1
print('FIM')
print('~' * (n * 5))