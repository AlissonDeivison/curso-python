#imports
import modulos
# --------------------------

print('Lista de questões 4')
question = int(input('Qual questão quer exibir?\nEntradas permitidas de 1 a 10: '))
modulos.verifyquestion(question)

match question:
    case 1:
        modulos.statementOne()
        valorReal = float(input('Informe o valor em real: '))
        print('R$ {} convertido para dólar é US${:.2f}'.format(valorReal, modulos.questionOne(valorReal)))
    case 2:
        modulos.statementTwo()
        valorReal = float(input('Informe o valor em real: '))
        userEnter = int(input('Para qual moeda gostaria de converter?\n1 - Dólar Americano\n2 - Euro\n3 - Peso Argentino\n'))
        modulos.verifyUserEnter(userEnter)
        modulos.questionTwo(valorReal,userEnter)
        if userEnter == 1:
            currencyType = 'Dólar Americano'
            symbolType = 'US$'
        elif userEnter == 2:
            currencyType = 'Euro'
            symbolType = '€'
        elif userEnter == 3:
            currencyType = 'Peso Argentino'
            symbolType = '$'
        print('R$ {:.2f} convertido para {} é {} {:.2f}'.format(valorReal,currencyType,symbolType,modulos.questionTwo(valorReal,userEnter)))
    case 3:
        modulos.statementThree()
        valor = float(input('Informe um valor: '))
        currencyOrigin = int(input('Moeda de origem\n1) Dólar Americano\n2) Euro\n3) Peso Argentino\n'))
        modulos.verifyUserEnter(currencyOrigin)
        userEnter = int(input('Para qual moeda gostaria de converter?\n1 - Dólar Americano\n2 - Euro\n3 - Peso Argentino\n'))
        modulos.verifyUserEnter(userEnter)
