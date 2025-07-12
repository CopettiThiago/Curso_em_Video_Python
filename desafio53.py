frase = str(input('Digite uma frase : ')).upper().strip()
palavra = frase.split() #separa a frase em palavras
junto = ''.join(palavra) #junta as palavras
inverso = '' #inicializa a string inverso
for letra in range(len(junto) -1, -1, -1): #inverte a string
    inverso += junto[letra] #adiciona a letra invertida)
print(f'A frase {frase} tem a forma {junto} e invertida fica {inverso}.')
if inverso == junto: #verifica se a string invertida é igual a original
    print(f'A frase {frase} é um palíndromo!')
else:
    print(f'A frase {frase} não é um palíndromo!')


#utilizando fatiamento
'''
frase = str(input('Digite uma frase : ')).upper().strip()
palavra = frase.split() #separa a frase em palavras
junto = ''.join(palavra) #junta as palavras
inverso = junto[::-1]'' #inicializa a string inverso
print(f'A frase {frase} tem a forma {junto} e invertida fica {inverso}.')
if inverso == junto: #verifica se a string invertida é igual a original
    print(f'A frase {frase} é um palíndromo!')
else:
    print(f'A frase {frase} não é um palíndromo!')
'''

# Exemplos de palíndromos

#apos a sopa
#a sacada da casa
#a torre da derrota
#o lobo ama o bolo
#a mala nada na lama
#a cara rajada da jararaca
#anotaram a data da maratona

