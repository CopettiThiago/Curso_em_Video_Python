while True:
    n = int(input('Quer saber a tabuada de qual valor ? : '))
    print('-' * 20)
    if n < 0:
        break
    else:
        for c in range(0, 11):
            print(f' [ {n} ] X [ {c} ] = {n * c}')
            print('-' * 20)
            c += 1
print('PROGRAMA TABUADA ENCERRADO. Volte Sempre.')