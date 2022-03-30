# 4 - Realize a leitura de 3 floats e imprime a média aritmética
numberOne = float(input('Digite o primeiro número: '))
numberTwo = float(input('Digite o segundo número: '))
numberThree = float(input('Digite o terceiro número: '))
#Cáluclo
arithmeticAverage = (numberOne + numberTwo + numberThree) / 3
print('A média aritmética é {:.2f}'.format(arithmeticAverage))