# • Faça um Programa que peça um número correspondente a um determinado ano e em seguida informe se este ano é ou não bissexto.
print('Descubra se o ano informado é ou não bissexto')
ano = int(input('Ano: '))
casoUm = ano % 4
casoDois = ano % 100
casoTres = ano % 400

if casoUm == 0 and casoDois != 0 or casoUm != 0 and casoTres == 0:
    print('É bissexto')
else:
    print('Não é bissexto')
