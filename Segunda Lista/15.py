# • Faça um Programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês. Calcule e mostre o total do seu
# salário no referido mês, sabendo-se que são descontados 11% para o Imposto de Renda, 8% para o INSS e 5% para o sindicato, faça um
# programa que nos dê:
# • salário bruto.
# • quanto pagou ao INSS.
# • quanto pagou ao sindicato.
# • o salário líquido.
# • calcule os descontos e o salário líquido, conforme a tabela à direita.

valorHora = float(input('Valor recebido por hora de trabalho: '))
horasMes = float(input('Horas trabalhadas no mês: '))
salarioBruto = valorHora*horasMes
inss = salarioBruto*0.08
sindicato = salarioBruto*0.05
deducoes = inss+sindicato
salarioLiquidoTemp = salarioBruto-deducoes
impostoDeRenda = salarioLiquidoTemp*0.11
salarioLiquido = salarioLiquidoTemp-impostoDeRenda

print('Valor do salário Bruto R$ {:.2f}\nValor do  INSS R$ {:.2f}\nValor do Sindicato R$ {:.2f}\nSalário Líquido R$ {:.2f}'.format(salarioBruto,inss,sindicato,salarioLiquido))



