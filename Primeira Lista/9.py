# 9 - Faça um Programa que leia dois números inteiros e moste o maior deles.
numberOne = int(input('Digite o primeiro número: '))
numberTwo = int(input('Digite o segundo número: '))
if numberOne > numberTwo:
    print('{} é maior que {}'.format(numberOne, numberTwo))
elif numberOne < numberTwo:
    print('{} é maior que {}'.format(numberTwo, numberOne))
else:
    print('São iguais')