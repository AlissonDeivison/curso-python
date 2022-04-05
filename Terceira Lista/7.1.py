# • Faça um programa que pergunte o preço de três produtos e informe qual produto você deve comprar, sabendo que a decisão é sempre pelo
# mais barato.
precoUm = float(input('Digite o valor do primeiro produto '))
precoDois = float(input('Digite o valor do segundo produto '))
precoTres = float(input('Digite o valor do terceiro produto '))
listaPrecos = [precoUm,precoDois,precoTres]
print('O produto com menor valor custa R$ {}'.format(min(listaPrecos)))