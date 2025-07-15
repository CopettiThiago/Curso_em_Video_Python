from random import randint
n = (randint(1, 100),randint(1, 100),randint(1, 100),
     randint(1, 100),randint(1, 100))
print(n)
print(f'O maior numero sorteado foi {max(n)}')
print(f'O menor numero sorteado foi {min(n)}')


# print('Os valores sortedos foram: ', end=' ')
# for i in n:
#     print(f'{i}', end=' ')