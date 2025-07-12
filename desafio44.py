preco = float(input('Informe o valor do produto : R$ '))
modo = str(input('Formas de pagamento \n'
                 '1 - Á vista com dinheiro/cheque 10% desconto\n'
                 '2 - Á vista com cartão 5% desconto\n'
                 '3 - Cartão em 2 vezes não há desconto\n'
                 '4 - Cartão em 3x ou mais, acréscimo de 20%\n'
                 'Informe a opção desejada : '))

if modo == '1':
    valorf = preco - (preco * 10/100)
    print(f'Pagando á vista você recebeu 10% de desconto e pagará R$ {valorf:.2f}')
elif modo == '2':
    valorf = preco - (preco * 5/100)
    print(f'Pagando á vista com cartão você recebeu 5% de desconto e pagará R$ {valorf:.2f}')
elif modo == '3':
    valorf = preco
    print(f'Pagando em duas vezes não há desconto, o valor é R$ {valorf:.2f}')
elif modo == '4' :
    valorf = preco + (preco * 20/100)
    print(f'Pagando em 3x ou mais, há um acréscimo de 20% e você pagará R$ {valorf:.2f}')