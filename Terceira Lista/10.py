# • Faça um Programa que leia um número e exiba o dia correspondente da semana. (1-Domingo, 2-Segunda, etc.), se digitar outro valor deve
# aparecer valor inválido.
print('Use o intervalo de 1 a 7 para receber o dia da semana, considere "1" para domingo')
diaEntrada = int(input())
dia = ''
if diaEntrada == 1:
    dia ='Domingo'
elif diaEntrada == 2:
    dia ='Segunda'
elif diaEntrada == 3:
    dia ='Terça'
elif diaEntrada == 4:
    dia ='Quarta'
elif diaEntrada == 5:
    dia ='Quinta'
elif diaEntrada == 6:
    dia ='Sexta'
elif diaEntrada == 7:
    dia = 'Sábado'
else:
    dia = 'Não é uma entrada válida'
print(dia)