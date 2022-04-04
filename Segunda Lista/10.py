# • Faça um Programa que peça a temperatura em graus Celsius, transforme e mostre em graus Fahrenheit.
temperaturaC = float(input('Digite a temperaruta em graus Celsius: '))
conversao = (temperaturaC*(9/5))+32
print('{:.2f} graus Fahrenheit'.format(conversao))