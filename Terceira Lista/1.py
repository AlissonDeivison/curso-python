# • Faça um Programa que peça dois números e imprima o maior deles.
print('Verificação de número maior')
numeroUm = float(input('Digite o primeiro número '))
numeroDois = float(input('Digite o segundo número '))
lista = [numeroUm,numeroDois]
print ('{} É maior'.format(max(lista)))
