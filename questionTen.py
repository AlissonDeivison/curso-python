# 10 - Faça um programa que pede dois inteiros e armazene em duas variáveis. Em seguida, troque o valor das variáveis e exiba na tela.
numberOne = int(input('Digite o primeiro número: '))
numberTwo = int(input('Digite o segundo número: '))
temp = numberOne
numberOne = numberTwo
numberTwo = temp

print('Número 1: {}\nNúmero 2: {}'.format(numberOne,numberTwo))