times = ('Corinthians','Palmeiras', 'Santos', 'Grêmio',
         'Cruzeiro', 'Flamengo', 'Vasco', 'Chapecoense',
         'Atlético', 'Botafogo', 'Atlético-PR', 'Bahia',
         'São Paulo', 'Fluminense', 'Sport Recife',
         'EC Vitória', 'Coritiba', 'Avaí', 'Ponte Preta')

print('-=' * 30)
print('Lista de times do Brasileirão')
print('-=' * 30)
print(times)
print('-=' * 30)

posicao = int(input('Qual posição você quer saber ?'))
print(f'Quem está na {posicao}ª no campeonato é o {times[posicao -1]}')
print('-=' * 30)
print(f'Os 5 primeiros do campeonato são {times[0:5]}')
print('-=' * 30)
print(f'Os times na zona de rebaixamento são {times[-4:]}')
print(f'Times em ordem alfabética {sorted(times)}')
print('-=' * 30)
procura= str(input('Qual time quer saber a colocação ? ')).strip().title()
if procura in times:
    print(f'O {procura} está na {times.index(procura)+1} posição')