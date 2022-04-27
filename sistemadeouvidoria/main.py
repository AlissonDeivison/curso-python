# -*- coding: utf-8 -*-
#----------------------------------------------------------------------------
# Created By  : Alisson Deivison Silva Pereira
# Created Date: 27/04/2022
# version ='4.0'
# ---------------------------------------------------------------------------
""" Sistema de Ouvidoria da Universidade ABC """
# ---------------------------------------------------------------------------
# Imports
import manifestation
import functions
from manifestation import Manifastation
from functions import saudacao
from functions import menu
from functions import case1
from functions import case2
from functions import case3
from functions import case4
from functions import case6

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
    match userOption: #Verificando opções do menu
        case 1:
            case1(demonstrationList)
        case 2:
            case2(demonstrationList)
        case 3:
            case3(demonstrationList)
        case 4:
            case4(demonstrationList)
        case 5:
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
            newManifest = Manifastation() #Atribuindo a variável newManifest o objeto Manifastation()
            newManifest.id = len(demonstrationList)+1
            newManifest.nick = nickName
            newManifest.type = manifestType
            newManifest.manifestation = description
            demonstrationList.append(newManifest) #Adicinando newManifest a lista demonstrationList
        case 6:
            case6(demonstrationList)
        case 7:
            print('Obrigado por usar nossos sistemas')
            break
