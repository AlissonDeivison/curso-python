# 5 - Realiza a leitura de 1 float referente ao valor de um produto e imprime o valor com descontos de 10%, 20% e 50%
valor = float(input('Digite o valor do produto: '))
#Calculations
tenPercent = valor * 0.9
twentyPercent = valor * 0.8
fiftyPercent = valor * 0.5
print('O valor do produto com 10% de desconto é: R$ {:.2f}\nO valor do produto com 20% de desconto é: R$ {:.2f}\nO valor do produto com 50% de desconto é: R$ {:.2f}'.format(tenPercent,twentyPercent,fiftyPercent))
