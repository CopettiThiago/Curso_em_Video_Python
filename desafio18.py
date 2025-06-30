from math import sin, cos, tan, radians
angulo = float(input('Informe o ângulo : '))

seno = sin(radians(angulo))
cosseno = cos(radians(angulo))
tangente = tan(radians(angulo))

print(f'O seno de {angulo} ° é {seno:.2f}')
print(f'O cosseno de {angulo}° é {cosseno:.2f}')
print(f'A tangente de {angulo}° é {tangente:.2f}')

