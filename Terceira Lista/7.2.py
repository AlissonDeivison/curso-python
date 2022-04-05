# • Faça um programa que pergunte o preço de produtos e informe qual produto você deve comprar, sabendo que a decisão é sempre pelo
# mais barato.
maisBarato=[]
print('Verificação de produto mais barato')
print('Para sair digite "Sair" ou um valor inválido para o produto')
while True:
    valor = input()
    if valor.upper() == 'SAIR':
        break
    valor = float(valor)
    if valor < 0:
        break
    maisBarato.append(valor)
print('O produto mais barato custa R$ {}, para economizar você deve prioriza-lo'.format(min(maisBarato)))