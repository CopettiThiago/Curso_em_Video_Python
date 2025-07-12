n1 = int(input('Informe o primeiro número : '))
n2 = int(input('Informe o segundo numero : '))

opcao = 0
while opcao != 5:
    print('-=' * 15)
    print('Qual a operação desejada ?')

    print('[1] Somar')
    print('[2] Multiplicar')
    print('[3] Maior')
    print('[4] Novos números')
    print('[5] Sair do programa')
    opcao = int(input('Informe a operação : '))
    if opcao == 1:
        soma = n1 + n2
        print(f'A soma de {n1} e {n2} é {soma}')
    elif opcao == 2:
        mult = n1 * n2
        print(f'O resultado de {n1} X {n2} é {mult}')
    elif opcao == 3:
        if n1 > n2:
            print(f'O número {n1} é maior que {n2}')
        elif n1 < n2:
            print(f'O número {n2} é maior que {n1}')
        else:
            print(f'O número {n1} é igual a {n2}')
    elif opcao == 4:
        n1 = int(input('Informe o primeiro número : '))
        n2 = int(input('Informe o segundo numero : '))
    elif opcao == 5:
        print('Saindo do programa...')
    else:
        print('Opção inválida, tente novamente.')
    print('-=' * 15)
print('Fim do programa, volte sempre!')
