preco = float(input('Informe o preço do produto : '))

valorfinal = preco - (preco *5/100)

print(f'O produto que custava R%{preco:.2f}, na promoção com 5% de desconto, sai por R${valorfinal:.2f}')
