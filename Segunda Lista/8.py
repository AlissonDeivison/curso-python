# • Faça um Programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês.
# • Calcule e mostre o total do seu salário no referido mês.

salarioHora = float(input('Quanto você ganha por hora? '))
horasTrabalhadas = float(input('Quantas horas você trabalhou no mês? '))
salario = salarioHora*horasTrabalhadas
print('Seu salário é de {}'.format(salario))
