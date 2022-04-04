# 11 - As organizações Hamurabi Medeiros resolveram dar um aumento de salário a seus colaboradores e lhe contrataram para desenvolver o programa que calculará os reajustes.
# Faça um programa que recebe o salário de um colaborador e o reajuste segundo o seguinte critério, baseado no salário atual:
# • salários até R$ 280,00 (incluindo) : aumento de 20%
# • salários entre R$ 280,00 e R$ 700,00 : aumento de 15%
# • salários entre R$ 700,00 e R$ 1500,00 : aumento de 10%
# • salários de R$ 1500,00 em diante : aumento de 5%
# • Após o aumento ser realizado, informe na tela:
# • o salário antes do reajuste;
# • o percentual de aumento aplicado;
# • o valor do aumento;
# • o novo salário, após o aumento.

employeerSalary = float(input('Digite seu salário (No formato 1000.00): ' ))
if employeerSalary <= 280:
    increaseSalary = employeerSalary*1.2
    percet = 20
    increase = increaseSalary-employeerSalary
    print ('O salário atual é {:.2f}\nO percetual de ajuste adotado foi de {}%\nO valor do aumento foi de R$ {:.2f}\nSeu novo salário é R$ {:.2f}'.format(employeerSalary,percet,increase,increaseSalary))
elif employeerSalary > 280 and employeerSalary < 700:
    increaseSalary = employeerSalary*1.15
    percet = 15
    increase = increaseSalary-employeerSalary
    print ('O salário atual é {:.2f}\nO percetual de ajuste adotado foi de {}%\nO valor do aumento foi de R$ {:.2f}\nSeu novo salário é R$ {:.2f}'.format(employeerSalary,percet,increase,increaseSalary))
elif employeerSalary > 700 and employeerSalary < 1500:
    increaseSalary = employeerSalary*1.10
    percet = 10
    increase = increaseSalary-employeerSalary
    print ('O salário atual é {:.2f}\nO percetual de ajuste adotado foi de {}%\nO valor do aumento foi de R$ {:.2f}\nSeu novo salário é R$ {:.2f}'.format(employeerSalary,percet,increase,increaseSalary))
else:
    increaseSalary = employeerSalary * 1.05
    percet = 5
    increase = increaseSalary - employeerSalary
    print('O salário atual é {:.2f}\nO percetual de ajuste adotado foi de {}%\nO valor do aumento foi de R$ {:.2f}\nSeu novo salário é R$ {:.2f}'.format(employeerSalary, percet, increase, increaseSalary))