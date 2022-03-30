#6 - Realiza a leitura de 1 float referente ao salário do cidadão e apresenta o salário com reajuste de 10% da inflação
salary = float(input('Digite seu salário (No formato: 1030.00): '))
salary = salary*1.1
print('Seu salário corrigido pela inflação é de: R$ {:.2f}'.format(salary))
