nome = input('Informe o seu nome completo: ')

if 'SILVA' in nome.upper():
    print(f'O nome {nome} contém Silva')
else:
    print(f'O nome {nome} não contém Silva')
# Exemplo de uso do upper para deixar tudo em maiusculo e verificar se contém a #palavra Silva

#outra solução

nome = str(input('Digite seu nome completo: ')).strip()
print('Seu nome tem Sila ?', 'SILVA' in nome.upper())
# Verifica se a palavra Silva está no nome, independente de maiúsculas ou minúsculas.
