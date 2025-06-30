dia = int(input('Foi alugado por quantos dias ? '))
km = float(input('Andou quantos Km ? '))

diaria = dia * 60
kmr = km * 0.15
total = diaria + kmr

print(f'O total a pagar será R${total:.2f}. \nSendo R${diaria:.2f} referente ao aluguel e R${kmr:.2f} referente aos km rodados.')