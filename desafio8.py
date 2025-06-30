metro = float(input('Informe o valor em metros : '))

centimetros = metro * 100
milimetro = metro * 1000

print(f'Convertendo {metro} metros em centimetros temos : {centimetros} cm \nConvertendo {metro} m em milimetros temos : {milimetro} mm')

# todas as medidas

km = metro / 1000
hc = metro / 100
dam = metro / 10
dm = metro * 10



print(f'O valor de {metro} metros equivale a : \n{km:.3f} kilometros \n{hc:.3f} hectometros \n{dam:.3f} decametros \n{dm:.3f} decimetros')