largura = float(input('Informe a largura da parede : '))
altura = float(input('Informe a altura da parede : '))

area = largura * altura

tinta = area/2

print(f'A sua parede tem a largura de {largura:.2f} metros e altura de {altura:.2f} metros. \nA área total equivale a {area:.2f} m² e são necessários {tinta:.2f} litros de tinta para a pintura.')