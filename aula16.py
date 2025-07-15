# tuplas são variáveis compostas
#As tuplas são IMUNTÁVEIS
# as variáveis são acessadas por índices
#lanche = ('hamburguer', 'suco', 'pizza', 'pudim')

#print(lanche[1])  # acessa o segundo elemento
#print(lanche[0:2]) # fatia do índice 0 ao 1
# print(lanche[-1])  # acessa o último elemento
#print(lanche[1:]) # fatia do índice 1 até o final

#lanche = ('Hamburguer', 'Suco', 'Pizza','Pudim')
# print(lanche) #mostra todos os itens dentro da tupla
# print(lanche[1]) # mostra Suco pois a contagem começa em 0
# print(lanche[-2]) # mostra pizza, começa pelo último
# print(lanche[1:3]) # mostra Suco e Pizza, pois o item 3 não é contado
# print(lanche[2:]) # mostra Pizza até o final, pudim
# print(lanche[:2]) # mostra hamburguer e suco, o item 2 é ignorado
# print(sorted(lanche)) # mostra em ordem
#print(len(lanche) # 4

# for comida in lanche:
#     print(f'Eu vou comer {comida}')
# print('Comi pra caramba')

# for comida in lanche:
#     print(comida)
#
# for c in range(0, len(lanche)):
#     print(f'eu vou comer {lanche[c]} na posição {c}')
# print('Fim')
#
# for pos, comida in enumerate(lanche):
#     print(f'Eu vou comer {comida} na posição {pos}')

# a = (2, 5, 4)
# b = (5, 8, 1, 2)
# c = a + b
# print(c) # junta as tuplas, a ordem influencia, portanto != b + a
# print(len(c)) # 7 que é a soma das tuplas
# print(c.count(5)) # quantas vezes aparece o 5 dentro de c. 2 vezes
# print(c.index(5)) # mostra a posição de um número
# print(c.index(5, 1)) # mostra a posição do 5 pulando a posição 1

# pessoa = ('Thiago', 36, 'M', 78.50) #tuplas aceitam variáveis de tipos diferentes
# print(pessoa)

#del(pessoa) deleta a tupla inteira