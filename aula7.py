# Ordem de precedência dos operadores
# 1. ()
# 2. **
# 3. *, /, //, %
# 4. +, -

# 5 + 3 * 2= 11

#pow(4, 2) # 4**2 = 16

#25**(1/2) # Raiz quadrada de 25 = 5.0

# 'oi' + 'ola' # 'oiola'
# 'oi' * 3 # 'oi' + 'oi' + 'oi' = 'oiioiioi'
# '=' * 20 # '===================='

nome = input('Qual é o seu nome? ')
print('Seja bem vindo {}!'.format(nome))
print('Seja bem vindo {:^20}!'.format(nome))  # Centralizado em 20 caracteres
print('Seja bem vindo {:>20}!'.format(nome))  # Alinhado à direita em 20 caracteres
print('Seja bem vindo {:<20}!'.format(nome))  # Alinhado à esquerda em 20 caracteres
print('Seja bem vindo {:=^20}!'.format(nome))  # Centralizado com preenchimento de '=' em 20 caracteres


