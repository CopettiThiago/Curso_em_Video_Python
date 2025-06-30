from random import shuffle

a1 = input('Informe o nome do primeiro aluno : ')
a2 = input('Informe o nome do segundo aluno : ')
a3 = input('Informe o nome do terceiro aluno : ')
a4 = input('Informe o nome do quarto aluno : ')

lista = [a1, a2, a3, a4]

shuffle(lista)
print(f'A ordem de apresentação será: ')
print(lista)
# O código acima sorteia um aluno aleatoriamente, enquanto este embaralha a lista de alunos.
# O uso de random.shuffle() embaralha a lista em ordem aleatória, enquanto choice() escolhe um único elemento aleatório da lista.
# Ambos os métodos são úteis, mas servem a propósitos diferentes.