casa = float(input('Informe o valor da casa: R$ '))
salario = float(input('Informe o seu salario : R$ '))
anos = int(input('Informe em quantos anos quer pagar : '))

prestacao = casa / (anos * 12)
maximo = salario * 30/100

print(f'Para comprar uma casa de R$ {casa:.2f} em {anos} anos,\n'
      f' a prestação mensal será de R$ {prestacao:.2f}')
if prestacao > maximo:
    print('Infelizmente seu empréstimo não foi aprovado')
else:
    print('Parabéns, seu empréstimo foi aprovado')