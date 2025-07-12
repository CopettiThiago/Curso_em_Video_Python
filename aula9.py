# fatiamento

# [0 : 0 : 0]    inicio, final e passo
#  [:5] inicio ate 4
#  [15:] indica o inicio e vai ate o final
#  [9::3]  começa no 9 e vai ate o final, pulando de 3 em 3

frase = 'Curso em video python'

print(frase[0:13:2]) # 0 é sempre o espaço 1, o último valor não é lido

#análise

print(len(frase)) # mostra o numero de espaços/caracteres na frase
print(frase.count('o')) # quantas vezes aparece a letra o minuscula
# frase.count('o', 0, 13) # conta quantas vezes aparece a letra o minuscula, do inicio até a posição 13
print(frase.find('deo')) # mostra a posição onde começou o deo
print(frase.find('Android')) # retorna o valor -1, que não foi encontrado
print('Curso' in frase) # existe a palavra entre aspas na frase? retorna True/False para o que foi pedido


# Transformação

frase.replace('Python', 'Android') # substitui Python por Android, não substitui a string original, deve-se #atribuir a uma nova variável ou a mesma variável
frase.upper() # transforma minusculas em maiusculas
frase.lower() # transforma tudo em minusculas
frase.capitalize() # primeira letra em maiuscula e todo o resto em minuscula
frase.title() # primeira letra de cada palavra em maiuscula, ele vê os espaços e considera cada palavra
frase.strip() # remove espaços inuteis no inicio e final da string
frase.rstrip() # remove espaços no final(r = direita)
frase.lstrip() # remove espaços no inicio(l = esquerda)

# Divisão

frase.split() # cria uma divisão onde tem espaços na string, as palavras recebem nova posição, e a frase vira uma lista
# ['Curso', 'em', 'video', 'python'] # exemplo de como fica a lista

# Junção

'-'.join(frase) # insere o item escolhido onde tem espaços, juntando a string



