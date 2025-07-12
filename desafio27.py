nome = str(input('Digite seu nome : ')).strip()

print(f'Seu primeiro nome é {nome.split()[0]}')
print(f'Seu último nome é {nome.split()[-1]}')  # -1 pega o último elemento da lista

#outra solução

n = str(input('Digite seu nome : ')).strip()
nome = n.split()

print(f'Muito prazer em te conhecer {n}!')
print(f'Seu primeiro nome é {nome[0]}')
print(f'Seu último nome é {nome[len(nome)-1]}')  # len(nome)-1 pega o último elemento da lista
