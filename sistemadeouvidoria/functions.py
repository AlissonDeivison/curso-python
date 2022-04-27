def menu():
    main_menu = ['1: Listar todas manifestações',
                 '2: Listar todas as sugestões',
                 '3: Listar todas as reclamações',
                 '4: Listar todos os elogios',
                 '5: Criar nova manifestação',
                 '6: Pesquisar manifestação pelo protocolo',
                 '7: Sair']
    for i in main_menu:
        print(i)
def saudacao():
    import time
    time = time.strftime('%H:%M')
    timeSplit = time.split(':')
    if int(timeSplit[0]) > 5 and int(timeSplit[0]) < 12:
        print('Bom dia, seja bem vindo ao sistema de Ouvidoria da Universidade ABC')
    elif int(timeSplit[0]) >= 12 and int(timeSplit[0]) < 18:
        print('Boa tarde, seja bem vindo ao sistema de Ouvidoria da Universidade ABC')
    elif int(timeSplit[0]) >= 18 and int(timeSplit[0]) < 5:
        print('Boa noite, seja bem vindo ao sistema de Ouvidoria da Universidade ABC')

def interationForList ():
    demonstrationsList = []
    for i in range(len(demonstrationsList)):
        print(f'{i.id}{i.nick}{i.type}{i.manifestation}')

def case1(demonstrationList):
    if len(demonstrationList) == 0:
        print('Nenhuma manifestação registrada até o momento')
    else:
        for item in range(len(demonstrationList)):
            print(
                f'[{item + 1}] - N° do protocolo: {demonstrationList[item].id} | Nome: {demonstrationList[item].nick} | Tipo: {demonstrationList[item].type} | Manifestação: {demonstrationList[item].manifestation}')

def case2(demonstrationList):
    if len(demonstrationList) == 0:
        print('Nenhuma manifestação registrada até o momento')
    else:
        for item in range(len(demonstrationList)):
            if demonstrationList[item].type == 'Sugestão':
                print(
                    f'[{item + 1}] - N° do protocolo: {demonstrationList[item].id} | Nome: {demonstrationList[item].nick} | Tipo: {demonstrationList[item].type} | Manifestação: {demonstrationList[item].manifestation}')


def case3(demonstrationList):
    if len(demonstrationList) == 0:
        print('Nenhuma manifestação registrada até o momento')
    else:
        for item in range(len(demonstrationList)):
            if demonstrationList[item].type == 'Reclamação':
                print(
                    f'[{item + 1}] - N° do protocolo: {demonstrationList[item].id} | Nome: {demonstrationList[item].nick} | Tipo: {demonstrationList[item].type} | Manifestação: {demonstrationList[item].manifestation}')
def case4(demonstrationList):
    if len(demonstrationList) == 0:
        print('Nenhuma manifestação registrada até o momento')
    else:
        for item in range(len(demonstrationList)):
            if demonstrationList[item].type == 'Elogio':
                print(
                    f'[{item + 1}] - N° do protocolo: {demonstrationList[item].id} | Nome: {demonstrationList[item].nick} | Tipo: {demonstrationList[item].type} | Manifestação: {demonstrationList[item].manifestation}')

def case6(demonstrationList):
    if len(demonstrationList) == 0:
        print('Nenhuma manifestação registrada até o momento')
    else:
        numberProtocol = int(input('Informe o número do protocolo: '))
        if numberProtocol > len(demonstrationList):
            print('Número de protocolo não existe')
        else:
            for item in range(len(demonstrationList)):
                if demonstrationList[item].id == numberProtocol:
                    print(f'N° do protocolo: {demonstrationList[item].id}\nNome: {demonstrationList[item].nick}\nTipo: {demonstrationList[item].type}\nManifestação: {demonstrationList[item].manifestation}')
