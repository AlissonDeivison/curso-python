# • Faça um Programa que leia 2 números e em seguida pergunte ao usuário qual operação ele deseja realizar. O resultado da operação deve
# ser acompanhado de uma frase que diga se o número é:
# • par ou ímpar;
# • positivo ou negativo;
# • inteiro ou decimal.

numeroUm = float(input('Digite o primeiro número: '))
numeroDois = float(input('Digite o segundo número: '))
print('Qual operação deseja realizar?\n1) Par ou ímpar\n2) Positivo ou negativo\n3) Inteiro ou decimal')
opcao = int(input('Digite sua opção: '))
#Operações
##Par ou ímpar
if opcao == 1:
    if numeroUm %2 == 0:
        print('{} é par'.format(numeroUm))
    elif numeroUm %2 != 0:
        print('{} é ímpar'.format(numeroUm))
    if numeroDois %2 == 0:
        print('{} é par'.format(numeroDois))
    elif numeroDois %2 != 0:
        print('{} é ímpar'.format(numeroDois))
##Positivo e negativo
if opcao == 2:
    if numeroUm >= 0:
        print('{} é positivo'.format(numeroUm))
    elif numeroUm < 0:
        print('{} é negativo'.format(numeroUm))
    if numeroDois >= 0:
        print('{} é positivo'.format(numeroDois))
    elif numeroDois < 0:
        print('{} é negativo'.format(numeroDois))
##Inteiro ou decimal
if opcao == 3:
    if numeroUm == round(numeroUm):
        print('{} é inteiro'.format(numeroUm))
    elif numeroUm != round(numeroUm):
        print('{} é decimal'.format(numeroUm))
    if numeroDois == round(numeroDois):
        print('{} é inteiro'.format(numeroDois))
    elif numeroDois != round(numeroDois):
        print('{} é decimal'.format(numeroDois))
