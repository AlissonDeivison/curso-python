# • Faça um Programa para um caixa eletrônico. O programa deverá perguntar ao usuário a valor do saque e depois informar quantas notas de
# cada valor serão fornecidas. As notas disponíveis serão as de 1, 5, 10, 50 e 100 reais. O valor mínimo é de 10 reais e o máximo de 600 reais. O
# programa não deve se preocupar com a quantidade de notas existentes na máquina.
# • Exemplo 1: Para sacar a quantia de 256 reais, o programa fornece duas notas de 100, uma nota de 50, uma nota de 5 e uma nota
# de 1;
# • Exemplo 2: Para sacar a quantia de 399 reais, o programa fornece três notas de 100, uma nota de 50, quatro notas de 10, uma nota
# de 5 e quatro notas de 1

print('Bem vindo ao banco ABC')
print('Selecione uma das opçoes para prosseguir\n1) Saque\n2) Sair')
while True:
    opcao = int(input('Digite sua opção: '))
    if opcao == 1:
        print('Por favor, digite o valor do saque: ')
        saque = float(input('Digite o valor: '))
        if saque >= 10 and saque <= 600:
            notasCem = int(saque/100)
            notasCinquenta = int((saque-(notasCem*100))//50)
            notasDez = int(saque-((notasCem*100)+(notasCinquenta*50)))//10
            notasCinco = int((saque-((notasCem*100)+(notasCinquenta*50)+(notasDez*10)))/5)
            notasUm = int((saque-((notasCem*100)+(notasCinquenta*50)+(notasDez*10)+(notasCinco*5))))
            # print (notasCem,notasCinquenta,notasDez,notasCinco,notasUm)
            lista = [notasCem,notasCinquenta,notasDez,notasCinco,notasUm]
            if notasCem == 0 or notasCem > 1:
                tempCem = 'notas'
            elif notasCem == 1 :
                tempCem = 'nota'
            if notasCinquenta == 0 or notasCinquenta > 1:
                tempCin = 'notas'
            elif notasCinquenta == 1:
                tempCin = 'nota'
            if notasDez == 0 or notasDez > 1:
                tempDez = 'notas'
            elif notasDez == 1:
                tempDez = 'nota'
            if notasCinco == 0 or notasCinco > 1:
                tempCinco = 'notas'
            elif notasCinco == 1:
                tempCinco = 'nota'
            if notasUm == 0 or notasUm > 1:
                tempUm = 'notas'
            elif notasUm == 1:
                tempUm = 'nota'
            print('Aguarde enquanto contamos as notas')
            print('Confira o valor impresso:\n{} {} se R$ 100,00\n{} {} de R$ 50,00\n{} {} de R$ 10,00\n{} {} de R$ 5,00\n{} {} de R$ 1,00'.format(notasCem,tempCem,notasCinquenta, tempCin,notasDez,tempDez,notasCinco,tempCinco,notasUm,tempUm))
            break
        else:
            print('Valor não disponível para o saque.')
            break
    else:
        print('Esperamos ver você em breve novamente.')
        break