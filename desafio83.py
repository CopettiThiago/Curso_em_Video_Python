expressao = str(input('Digite uma expressão : '))

total_abre_parenteses = 0
total_fecha_parenteses = 0

for c in expressao:
    if c == '(':
        total_abre_parenteses += 1
    if c == ')':
        total_fecha_parenteses += 1

if total_abre_parenteses == total_fecha_parenteses:
    print('Está é uma expressão válida')
else:
    print('Está não é uma expressão válida')
    
# solução do professor
'''
exp = str(input('Digite uma  expressão : ))
pilha = []

for simb in exp:
    if simb == '(':
        pilha.append('(')
    elif simb == ')':
        if len(pilha) > 0:
            pilha.pop()
if len(pilha) == 0 :
    print('Esta é uma espressão válida.)
else:
    print('Esta não é uma expressão válida')
    
'''