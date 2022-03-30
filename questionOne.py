# 1 - Realiza a leitura de 2 float e imprime as seguintes operações: soma, subtração, multiplicação, divisão e resto de divisão
numberOne = float(input('Digite o primeiro número: '))
numberTwo = float(input('Digite o segundo número: '))
#Calculations
sum = numberOne+numberTwo
subtraction = numberOne-numberTwo
multiplication = numberOne*numberTwo
division = numberOne/numberTwo
rest = numberOne%numberTwo
print('Soma = {:.2f}\nSubtração = {:.2f}\nMultiplicação = {:.2f}\nDivisão = {:.2f}\nResto da divisão = {:.2f}'.format(sum,subtraction,multiplication,division,rest))