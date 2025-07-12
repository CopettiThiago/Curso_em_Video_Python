# cores no teminal
'''
\033[0;33;44m # style;text;back

style = 0 (none), 1 (bold), 4 (underline), 7 (negative)(inverted colors)
text = 30 (black), 31 (red), 32 (green), 33 (yellow), 34 (blue), 35 (purple), 36 (cyan), 37 (white)
back = 40 (black), 41 (red), 42 (green), 43 (yellow), 44 (blue), 45 (purple), 46 (cyan), 47 (white)

'''

print('\033[0;33;44mOlá, Mundo!\033[m')
print('\033[1;31;43mOlá, Mundo!\033[m')
print('\033[4;30;45mOlá, Mundo!\033[m')

a = 3
b = 5
print('Os valores são \033[32m{}\033[m e \033[31m{}\033[m!!!'.format(a, b))

nome = 'Gustavo'
cores = {'limpa': '\033[m',
         'azul': '\033[34m',
        'amarelo': '\033[33m',
        'pretoebranco': '\033[7;30m'}

print('Olá! Muito prazer em te conhecer, {}{}{}!!!'.format(cores['amarelo'], nome, cores['limpa']))