a1 = input('Informe o nome do primeiro aluno : ')
a2 = input('Informe o nome do segundo aluno : ')
a3 = input('Informe o nome do terceiro aluno : ')
a4 = input('Informe o nome do quarto aluno : ')

alunos = [a1, a2, a3, a4]

from random import choice

sorteado = choice(alunos)
print(f'O aluno sorteado foi {sorteado} !')

