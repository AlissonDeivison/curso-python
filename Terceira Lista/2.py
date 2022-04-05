# • Faça um Programa que peça um valor e mostre na tela se o valor é positivo ou negativo.
print('Verificador de números positivos ou negativos')
numero = float(input('Digite o número '))
if numero < 0:
    print('Negativo')
elif numero == 0:
    print('Neutro')
else:
    print('Positivo')