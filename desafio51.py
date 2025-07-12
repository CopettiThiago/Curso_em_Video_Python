primeiro = int(input('Digite o primeiro termo da PA : '))
razao = int(input('Informe a razão da PA : '))
decimo = primeiro + (10 - 1) * razao

print('Os 10 primeiros termos da PA são:')
for c in range(primeiro, decimo + razao , razao):
    print(c, end=' -> ')
print('FIM')