# • Faça um Programa que leia três números e mostre o maior e o menor deles.
# • Faça um Programa que leia três números e mostre o maior deles.
print('Verificador de número maior entre três')
numeroUm = float(input('Digite o primeiro número '))
numeroDois = float(input('Digite o segundo número '))
numeroTres = float(input('Digite o terceiro número '))
listaNumeros = [numeroUm,numeroDois,numeroTres]
print('O maior número digitado foi {}\nO menor número digitado foi {}'.format(max(listaNumeros),min(listaNumeros)))