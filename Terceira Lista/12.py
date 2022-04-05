# • Faça um Programa que peça uma data no formato dd/mm/aaaa e determine se a mesma é uma data válida.
print('Informe uma data no formado dd/mm/aaaa')
data = input('Data: ')
data = data.split('/')
dia = int(data[0])
mes = int(data[1])
ano = int(data[2])
if mes != 2:
    if (dia > 0 and dia <=31) and (mes > 0 and mes <=12):
        print('{}/{}/{} É uma data válida'.format(dia,mes,ano))
    else:
        print('Não é uma data válida')
elif mes == 2:
    if dia <= 28:
        print('{}/{}/{} É uma data válida'.format(dia,mes,ano))
    else:
        print('{}/{}/{} Não é uma data válida'.format(dia,mes,ano))

