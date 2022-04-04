# • Faça um Programa que peça 2 números inteiros e um número real. Calcule e mostre:
# • o produto do dobro do primeiro com metade do segundo .
# • a soma do triplo do primeiro com o terceiro.
# • o terceiro elevado ao cubo.
print ('Em ordem digite dois números inteiros e um real')
numeroUm = int(input('Primeiro inteiro '))
numeroDois = int(input('Segundo inteiro '))
numeroTres = float(input('Número real '))
calculoUm = (numeroUm*2)*(numeroDois/2)
calculoDois = (numeroUm*3)+numeroTres
calculoTres = numeroTres**3
print('O produto do dobro do primeiro com metade do segundo é {}\nA soma do triplo do primeiro com o terceiro é {}\nO terceiro elevado ao cubo é {}'.format(calculoUm,calculoDois,calculoTres))