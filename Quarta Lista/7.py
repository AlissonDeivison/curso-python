# • Faça um programa que leia 5 números e informe o maior número.

numeroUm = float(input('Digite um número: '))
numeroDois = float(input('Digite um número: '))
numeroTres = float(input('Digite um número: '))
numeroQuatro = float(input('Digite um número: '))
numeroCinco = float(input('Digite um número: '))
listaNumero = (numeroUm,numeroDois,numeroTres,numeroQuatro,numeroCinco)
print(f'{max(listaNumero)} foi o maior número digitado')
