n1 = float(input('Informe a primeira nota: '))
n2 = float(input('Informe a segunda nota: '))

media = (n1 + n2) / 2

if media < 5.0 :
    print(f'Sua média foi {media:.2f} e você está reprovado.')
elif  media <= 6.9 :
    print(f'Sua média foi {media:.2f} e você está em recuperação.')
else:
    print(f'Sua média foi {media:.2f} e você está aprovado')