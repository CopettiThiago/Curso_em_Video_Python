salario = float(input('Informe o valor do salário R$ '))

if salario > 1250:
    novosal = salario + (salario * 10/100)
    print(f'O funcionário recebia R$ {salario:.2f} e com um aumento de 10% \n passará a receber R$ {novosal:.2f}')
else:
    novosal = salario + (salario *15/100)
    print(f'O funcionário recebia R$ {salario:.2f} e com um aumento de 15% \n passará a receber R$ {novosal:.2f}')
