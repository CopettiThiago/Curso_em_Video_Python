'''
dados = ['Pedro', 25]
pessoas.append(dados[:])

pessoas = [['Pedro', 25], ['Maria', 19], ['João', 32]]

print(pessoas[0][0])  mostra na tela Pedro
print(pessoas[1][1]) mostra 19 na tela
print(pessoas[2][0]) mostra João
print(pessoas[1])  mostra ['Maria', 19]

'''
'''
galera = [['João, 19], ['Ana', 33], ['Joaquim', 13], ['Maria', 45]]

for p in galera:
    print(f'{p[0]} tem {p[1]} anos de idade)

'''
'''
galera = list()
dado = list()

for c in range(0, 3):
    dado.append(str(input('Nome : ')))
    dado.append(int(input('Idade : )))
    galera.append(dado[:])
    dado.clera()
    
print(galera)

'''
'''
galera = list()
dado = list()
totmai = totmen = 0
for c in range(0, 3):
    dado.append(str(input('Nome : ')))
    dado.append(int(input('Idade : )))
    galera.append(dado[:])
    dado.clera()

for p in galera:
    if p[1] >= 21
        print(f'{p[0]} é maior de idade')
        totmai += 1
    else:
        print(f'{p[0]} é menor de idade)
        totmen += 1

print(f'Temos {totmai} maiores e {totmen} menores de idade')

'''