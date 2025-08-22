# lanche.append() adiciona um item a lista
# lanche.append(3, item) adiciona um item a posição 3

# del lanche[3] 
# lanche.pop() remove o último item
# lanche.pop(3) remove o item da posição 3
# lanche.remove(item)

# if 'item' in lanche:
#     lanche.remove('item')

# valores = list(range(4,11)) cria uma lista com range

# valores = [8,2,5,4,9,3,0]

# valores.sort() ordena todos os valores
# valores.sorte(reverse=true) ordena os valores de forma inversa

# num = [2, 5, 9, 1]
# num[2] = 3      # substitui o índice 2
# num.append(7)   # adiciona o numero 7 ao final da lista
# num.sort(reverse=True)  # lista inversa
# num.insert(2, 2)    #insere o número 2 no índice 2
# if 5 in num:
#     num.remove(5)   # se houver o numer o5 ele é apagado
# else:
#     print('Não achei o número 5')
# print(num)
# print(f'Essa lista tem {len(num)} elementos')

# valores = []
# valores.append(5)
# valores.append(9)
# valores.append(4)

# for c , v in enumerate(valores):
#     print(f'Na posição {c} enconrei o valor {v} !')
# print('Cheguei ao final da lista')

# para receber valores do usuário
# for cont in range(0, 5):
    # valores.append(int(input('Digite um valor')))
    
a = [2, 3, 4, 7]
b = a
b = a[:]        # nesse caso é feita uma cópia dos valores de a, sendo possivel alterar os valores apenas na lista a posteriormente
b[2] = 8        # altera o valor nas duas listas, pois faz uma ligação

print(f'Lista {a}')
print(f'Lista {b}')
