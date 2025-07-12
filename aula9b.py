frase = 'Curso em Vídeo Python'

print(frase[3:13:2]) #fatiamento com passo
print(frase[::2]) # salto 2 sem saber o inicio e o fim

# para um texto com várias linhas pode-se usar o print com ''' no inicio e final

print(len(frase.strip())) # len conta o numero de caracteres, strip remove os espaços no inicio e no final
print(frase.count('o')) # conta quantos 'o' minusculos tem na frase
print(frase.upper().count('O')) # upper coloca tudo em maiusculo e conta o total de 'O'
print(len(frase.strip())) # strip remove os espaços e len conta os caracteres
print(frase.replace('Python', 'Android')) # para substituir na frase, frase deve = a string
print('Curso' in frase) # mostra se existe a palavra Curso na string
print(frase.lower().find('vídeo')) # lower transforma toda a string em minuscula, find mostra a posição

print(frase.split())

dividido = frase.split()

print(dividido[2][3]) # split divide a frase, nesse caso o dividido mostra a terceira palavra e a quarta letra