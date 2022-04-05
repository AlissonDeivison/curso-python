# • Faça um Programa que peça um número inteiro e determine se ele é par ou impar. Dica: utilize o operador módulo (resto da divisão).
numero = int(input('Digite o número para saber se é par ou ímpar: '))
if numero%2==0:
    print('O número informado é par')
else:
    print('O número informado é ímpar')