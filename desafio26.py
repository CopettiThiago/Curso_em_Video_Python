frase = str(input('Digite uma frase : ').strip())

print(f'A letra "A" aparece {frase.upper().count('A')} na frase.')
print(f'A primeira letra "A" aparece na posição {frase.upper().find('A')}.')
print(f'A última letra "A" aparece na posição {frase.upper().rfind('A')}.')

#outra solução

frase = str(input('Digite uma frase : ')).upper().strip()

print(f'A letra "A" aparece {frase.count('A')} na frase.')
print(f'A primeira letra "A" aparece na posição {frase.find('A')+1}.')
print(f'A última letra "A" aparece na posição {frase.rfind('A')+1}.')
