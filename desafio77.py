palavras = (
        'APRENDER', 'PROGRAMAR', 'LINGUAGEM', 'PYTHON',
        'CURSO', 'GRATIS', 'ESTUDAR', 'PRATICAR', 'TRABALHAR',
        'MERCADO', 'PROGRAMADOR', 'FUTURO', 'DRTWS'
        )

for palavra in palavras:
    vogais_encontradas = []
    
    for letra in palavra:
        if letra.lower() in 'aeiou':
            vogais_encontradas.append(letra)
            
    if vogais_encontradas:
        print(f'\nNa palavra {palavra} temos as vogais ', end= '')
        for vogal in vogais_encontradas:
            print(vogal, end= ' ')
    else:
        print(f'\nA palavra {palavra.upper()} não tem vogais')
        
'''
Solução Gemini

# Itera sobre cada palavra na tupla
for palavra in palavras:
    # Cria uma lista vazia para guardar as vogais encontradas em cada palavra
    vogais_encontradas = []
    
    # Itera sobre cada letra da palavra atual
    for letra in palavra:
        # Verifica se a letra (convertida para minúscula) é uma vogal
        if letra.lower() in 'aeiou':
            # Se for, adiciona a letra original à nossa lista
            vogais_encontradas.append(letra)
    
    # Após verificar todas as letras, checa se a lista de vogais não está vazia
    if vogais_encontradas:
        # Se encontrou vogais, imprime a mensagem original
        print(f'\nNa palavra {palavra.upper()} temos as vogais: ', end='')
        # Imprime cada vogal encontrada, separada por espaço
        for vogal in vogais_encontradas:
            print(vogal, end=' ')
    else:
        # Se a lista estiver vazia, significa que não há vogais
        print(f'\nA palavra {palavra.upper()} não tem vogais.')
'''
            
