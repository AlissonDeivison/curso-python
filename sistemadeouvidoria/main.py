# -*- coding: utf-8 -*-
#----------------------------------------------------------------------------
# Created By  : Alisson Deivison Silva Pereira
# Created Date: 27/04/2022
# version ='4.0'
# ---------------------------------------------------------------------------
""" Sistema de Ouvidoria da Universidade ABC """
# ---------------------------------------------------------------------------
# Imports
from functions import saudacao, menu, case1, case2, case3, case4
from manifestation import Manifastation
# ---------------------------------------------------------------------------
# Variables
demonstrationList = []
# ---------------------------------------------------------------------------
saudacao() #Mensagem de saudação ao usuário e menu
while True:
    menu()  # Menu principal
    userOption = int(input('Escolha uma opção do menu: '))
    while int(userOption) <= 0 or int(userOption) > 7:
        print('Opção inválida')
        userOption = int(input('Escolha uma opção do menu: '))
    if userOption == 1:
        case1(demonstrationList)
    elif userOption == 2:
        case2(demonstrationList)
    elif userOption == 3:
            case3(demonstrationList)
    elif userOption == 4:
            case4(demonstrationList)
    elif userOption == 5:
        nickName = input("Digite o nome do requisitante: ")
        manifestType = int(input("Digite o tipo (1 para reclamação, 2 para sugestão e 3 para elogio): "))
        # ------ Validador da entrada do usuário
        while manifestType < 1 or manifestType > 3:
            print('Tipo de manifestação inválida')
            manifestType = int(input("Digite o tipo (1 para reclamação, 2 para sugestão e 3 para elogio): "))
        # ------ Atribuindo novos valores a entrada type do usuário
        if (manifestType) == 1:
            manifestType = 'Reclamação'
        elif (manifestType) == 2:
            manifestType = 'Sugestão'
        elif (manifestType) == 3:
            manifestType = 'Elogio'
        # ------
        description = input("Digite a descrição: ")
        newManifest = Manifastation() #Atribuindo a variável newManifest ao objeto Manifastation()
        newManifest.id = len(demonstrationList)+1
        newManifest.nick = nickName
        newManifest.type = manifestType
        newManifest.manifestation = description
        demonstrationList.append(newManifest) #Adicinando newManifest a lista de objetos demonstrationList
    elif userOption == 6:
        if len(demonstrationList) == 0:
            print('Nenhuma manifestação registrada até o momento')
        else:
            numberProtocol = int(input('Informe o número do protocolo: '))
            manifestacaoProcurada = demonstrationList[numberProtocol - 1]
            print(f'N° do protocolo: {manifestacaoProcurada.id} | Nome: {manifestacaoProcurada.nick} | Tipo: {manifestacaoProcurada.type} | Manifestação: {manifestacaoProcurada.manifestation}')
    elif userOption == 7:
        print('Obrigado por usar nossos sistemas')
        break
