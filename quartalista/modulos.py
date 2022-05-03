def verifyquestion (question):
    while question < 1 or question > 10:
        question = int(input('Qual questão quer exibir?\nEntradas permitidas de 1 a 10: '))
    return question
def verifyUserEnter (userEnter):
    while userEnter < 1 or userEnter > 3:
        userEnter = int(input('Para qual moeda gostaria de converter?\n1 - Dólar Americano\n2 - Euro\n3 - Peso Argentino\n'))

def currencyOrigin (currencyOrigin):
    while currencyOrigin < 1 or currencyOrigin > 3:
        currencyOrigin = int(input('Para qual moeda gostaria de converter?\n1 - Dólar Americano\n2 - Euro\n3 - Peso Argentino\n'))

# questions
def questionOne (valorReal):
    valorDolar = 0.20
    return valorReal*valorDolar

def questionTwo(valorReal,userEnter):
    valorDolar = 0.20
    valorEuro = 0.19
    valorPeso = 22.98
    match userEnter:
        case 1:
            return valorReal*valorDolar
        case 2:
            return valorReal*valorEuro
        case 3:
            return valorReal*valorPeso

def questionThree(currencyOrigin):
    match currencyOrigin:
    valorDolar = 0.20
    valorEuro = 0.19
    valorPeso = 22.98
        case 1:



# questions
def statementOne ():
    print('Executando a questão 1:  Crie um método que receba um valor em reais e converta a dólares')
def statementTwo ():
    print('Executando a questão 2:  Crie um método que receba 2 parâmetros:um valor em reais e a moeda que deve ser convertida (dólares,euros ou peso argentino).E realize a conversão.')
def statementThree ():
    print('Crie um método quer eceba 3 parâmetros:um valor, moeda de origem e a moeda que deve ser convertida(dolares,euros ou peso argentino).E realize a conversão.')