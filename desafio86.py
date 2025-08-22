# Solução do professor

# matriz = [[0, 0, 0],[0, 0, 0],[0, 0, 0]]

# for l in range(0,3):
#     for c in range(0,3):
#         matriz[l][c] = int(input(f'Digite um valor para [{[l],[c]}] : '))
# print('-=' * 10)
# for l in range(0,3):
#     for c in range(0,3):
#         print(f'[{matriz[l][c]:^5}]', end='')
#     print()

#Solução internet

matriz = []
T = int(input("Digite o número de colunas:"))
U = int(input("Digite o número de linhas:"))
for i in range(T):
    matriz.append([])

for l in range(0,T):
    for c in range(0,U):
        matriz[l].append(int(input(f"Digite um valor para [{l},{c}]: ")))
    
for l in range(0,T):
        for c in range(0,U):
              print(f'[{matriz[l][c]:^5}]', end='')
        print()


'''
Minha solução

lista = []

for c in range(0, 3):
    for i in range(0, 3):
        lista[c].append(int(input(f'Digite um valor para {c, i} : ')))

for c in lista:
    for i in lista:
        print(f'{lista[c][i]}', end='')
    print()
'''