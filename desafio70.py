print('-'*30)
print('     LOJA SUPER BARATÃO      ')
print('-'*30)
total = mil = maisbarato = cont =0
menor = ''
while True:
    produto = str(input('Nome do produto : ' ))
    preco = float(input('Preço : R$ '))
    total += preco
    if preco >= 1000:
       mil  += 1
    cont += 1
    if cont == 1 or preco < maisbarato:
        maisbarato = preco
        menor = produto
    continua = ' '
    while continua not in 'SN':
        continua = str(input('Deseja continuar? [S/N] ')).strip().upper()[0]
    if continua == 'N':
            break
print('-'*15, 'FIM DO PROGRAMA', '-'*15)
print(f'O total da compra foi R$ {total:.2f}')
print(f'Temos {mil} produto(s) custando mais de R$ 1000.00')
print(f'O produto mais barato foi {menor} que custa R${maisbarato:.2f}')
