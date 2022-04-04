# • Tendo como dados de entrada a altura de uma pessoa, construa um algoritmo que calcule seu peso ideal, usando a seguinte fórmula:
# (72.7*altura)–58
altura = float(input('Digite sua altura (utilize o formato 1.87, para 1m e 87cm) '))
pesoIdeal = (72.7*altura)-58
print('Seu peso ideal é {:.2f}'.format(pesoIdeal))