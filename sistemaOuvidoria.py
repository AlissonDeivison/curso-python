# -*- coding: utf-8 -*-
#----------------------------------------------------------------------------
# Created By  : Alisson Deivison Silva Pereira
# Created Date: 20/04/2022
# version ='1.0'
# ---------------------------------------------------------------------------
""" Sistema de Ouvidoria da Universidade ABC """
# ---------------------------------------------------------------------------
# Imports
import datetime
import time
# ---------------------------------------------------------------------------
#Mensagem de saudação ao usuário e menu
time = time.strftime('%H:%M')
timeSplit = time.split(':')
if int(timeSplit[0]) > 5  and int(timeSplit[0]) < 12:
    print('Bom dia')
elif int(timeSplit[0]) >= 12  and int(timeSplit[0]) < 18:
    print('Boa tarde')
elif int(timeSplit[0]) >= 18  and int(timeSplit[0]) < 5:
    print('Boa noite')
print('Seja bem vindo ao sistema de Ouvidoria da Universidade ABC')
print('Menu Principal:\n1) Listar todas manifestações\n2) Listar todas as sugestões\n3) Listar todas as reclamações\n4) Listar todos os elogios\n5) Criar nova manifestação\n6) Pesquisar manifestação pelo protocolo\n7) Sair')
# --------------------------Variáveis----------------------------------------
menuList = [1,2,3,4,5,6]
demonstrationsList =[]
# ----------------Verificador de entrada do usuário--------------------------
while True:
    userOption = int(input('Digite uma opção do menu principal: '))
    while (userOption) > 7 or (userOption) <= 0:
        print('Opção inválida')
        userOption = int((input('Digite uma opção válida: ')))
# ---------------------------------------------------------------------------
    if (userOption) in menuList: #Condição de entrada para verificações posteriores
        if userOption == 1: #Opção 1 do menu - Listar todas manifestações
            if len(demonstrationsList) == 0:
                print('Não há nenhuma manifestação registrada')
            else:
                for i in range(len(demonstrationsList)):
                    brokenManifestation = demonstrationsList[i].split('/')
                    print (f'ID do chamado: {brokenManifestation[0]} - Usuário: {brokenManifestation[1]} - Categoria da manifestação: {brokenManifestation[2]} - Manifestação: {brokenManifestation[3]}')
        elif userOption == 2: #Opção 2 do menu - Listar todas as sugestões
            if len(demonstrationsList) == 0:
                print('Não há nenhuma manifestação registrada')
            else:
                for i in range(len(demonstrationsList)):
                    brokenManifestation = demonstrationsList[i].split('/')
                    categoryVerification = brokenManifestation[2]
                    if categoryVerification == 'Sugestão':
                        print(f'ID do chamado: {brokenManifestation[0]} - Usuário: {brokenManifestation[1]} - Categoria da manifestação: {brokenManifestation[2]} - Manifestação: {brokenManifestation[3]}')
        elif userOption == 3: #Opção 3 do menu - Listar todas as reclamações
            if len(demonstrationsList) == 0:
                print('Não há nenhuma manifestação registrada')
            else:
                for i in range(len(demonstrationsList)):
                    brokenManifestation = demonstrationsList[i].split('/')
                    categoryVerification = brokenManifestation[2]
                    if categoryVerification == 'Reclamação':
                        print(f'ID do chamado: {brokenManifestation[0]} - Usuário: {brokenManifestation[1]} - Categoria da manifestação: {brokenManifestation[2]} - Manifestação: {brokenManifestation[3]}')
        elif userOption == 4: #Opção 4 do menu - Listar todos os elogios
            if len(demonstrationsList) == 0:
                print('Não há nenhuma manifestação registrada')
            else:
                for i in range(len(demonstrationsList)):
                    brokenManifestation = demonstrationsList[i].split('/')
                    categoryVerification = brokenManifestation[2]
                    if categoryVerification == 'Elogio':
                        print(f'ID do chamado: {brokenManifestation[0]} - Usuário: {brokenManifestation[1]} - Categoria da manifestação: {brokenManifestation[2]} - Manifestação: {brokenManifestation[3]}')
        elif userOption == 5: #Opção 5 do menu - Criar nova manifestação
            # newDemonstration = []
            newDemonstration = ''
            print('Para criar uma nova manifestação você deve  informar seu nome, escolher uma categoria e em seguida digitar  a sua manifestação')
            id = len(demonstrationsList)+1
            user = input('Informe seu nome: ')
            category = int(input('Informe a categoria do seu manifesto, são elas:\n1) Reclamação\n2) Sugestão\n3) Elogio\nQual categoria deseja atribuir a sua manifestação? '))
            categoryList =[1,2,3]
            while not category in categoryList: #Verificador de entrada de categoria do usuário
                print('Opção inválida')
                category = int(input('Informe a categoria do seu manifesto, são elas:\n1) Reclamação\n2) Sugestão\n3) Elogio\nQual categoria deseja atribuir a sua manifestação? '))
            if category == 1: #Atribuindo novos valores a variável category
                category = 'Reclamação'
            elif category == 2: #Atribuindo novos valores a variável category
                category = 'Sugestão'
            elif category == 3: #Atribuindo novos valores a variável category
                category = 'Elogio'
            demonstration = input('Informe sua manifestação: ')
            newDemonstration = f'{id}/{user}/{category}/{demonstration}'
            demonstrationsList.append(newDemonstration)
        elif userOption == 6:  # Pesquisar manifestação pelo protocolo
            if len(demonstrationsList) == 0:
                print('Não há nenhuma manifestação registrada')
            else:
                print('Para fazer a pesquisa da manifestação pelo número do protocolo você deve saber o ID da sua manifestação')
                protocolEntry = int(input('Informe o número do seu protocolo: '))
                for i in range(len(demonstrationsList)):
                    brokenManifestation = demonstrationsList[i].split('/')
                    numberProtocol = int(brokenManifestation[0])
                    if protocolEntry == numberProtocol:
                        print(f'ID do chamado: {brokenManifestation[0]}\nUsuário: {brokenManifestation[1]}\nCategoria da manifestação: {brokenManifestation[2]}\nManifestação: {brokenManifestation[3]}')
                    else:
                        continue
    elif (userOption) == 7:
        print('Obrigado por usar nossos sistemas')
        break
