# -*- coding: utf-8 -*-
#----------------------------------------------------------------------------
# Created By  : Alisson Deivison Silva Pereira
# Created Date: 09/05/2022
# version ='5.0'
# ---------------------------------------------------------------------------
""" Sistema de Ouvidoria da Universidade ABC """
# ---------------------------------------------------------------------------
# Imports
from functions import saudacao, menu
from operacoesbd import *
import mysql.connector
# ---------------------------------------------------------------------------
conn = abrirBancoDados('localhost','root','-','ouvidoria')
saudacao() #Mensagem de saudação ao usuário e menu
while True:
    menu()  # Menu principal
    userOption = int(input('Escolha uma opção do menu: '))
    while int(userOption) <= 0 or int(userOption) > 7:
        print('Opção inválida')
        userOption = int(input('Escolha uma opção do menu: '))
    if userOption == 1:
        sql = "SELECT * FROM manifestacoes"
        resultado = listarBancoDados(conn, sql)
        if len(resultado)==0:
            print('Nenhuma manifestação registrada')
        else:
            for elemento in resultado:
                print(f'Número do protocolo: {elemento[0]} - Requisitante: {elemento[1]} - Tipo: {elemento[2]} - Descrição {elemento[3]}')
    elif userOption == 2:
        sql = "SELECT * FROM manifestacoes where manifestType = 'Sugestão'"
        resultado = listarBancoDados(conn, sql)
        if len(resultado)==0:
            print('Nenhuma manifestação registrada')
        else:
            for elemento in resultado:
                print(f'Número do protocolo: {elemento[0]} - Requisitante: {elemento[1]} - Tipo: {elemento[2]} - Descrição {elemento[3]}')
    elif userOption == 3:
        sql = "SELECT * FROM manifestacoes where manifestType = 'Reclamação'"
        resultado = listarBancoDados(conn, sql)
        if len(resultado)==0:
            print('Nenhuma manifestação registrada')
        else:
            for elemento in resultado:
                print(f'Número do protocolo: {elemento[0]} - Requisitante: {elemento[1]} - Tipo: {elemento[2]} - Descrição {elemento[3]}')
    elif userOption == 4:
        sql = "SELECT * FROM manifestacoes where manifestType = 'Elogio'"
        resultado = listarBancoDados(conn, sql)
        if len(resultado)==0:
            print('Nenhuma manifestação registrada')
        else:
            for elemento in resultado:
                print(f'Número do protocolo: {elemento[0]} - Requisitante: {elemento[1]} - Tipo: {elemento[2]} - Descrição {elemento[3]}')
    elif userOption == 5:
        nickName = input("Digite o nome do requisitante: ")
        manifestType = int(input("Qual a categoria da manifestação?\n1 - Reclamação\n2 - Sugestão\n3 - Elogio\nEscolha: "))
        description = input("Digite a descrição: ")
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
        sql = "INSERT INTO manifestacoes(nickName,manifestType,description) VALUES (%s, %s, %s)"
        dados = (nickName, manifestType, description)
        insertNoBancoDados(conn,sql,dados)

    elif userOption == 6:
        sql = "SELECT * FROM manifestacoes"
        resultado = listarBancoDados(conn, sql)
        if len(resultado) == 0:
            print('Nenhuma manifestação registrada')
        else:
            numberProtocol = int(input('Informe o número do protocolo: '))
            sql = (f"SELECT * FROM manifestacoes where id = '{numberProtocol}'")
            resultado = listarBancoDados(conn, sql)
            for elemento in resultado:
                print(f'Número do protocolo: {elemento[0]}\nRequisitante: {elemento[1]}\nTipo: {elemento[2]}\nDescrição: {elemento[3]}')
    elif userOption == 7:
        encerrarBancoDados(conn)
        print('Obrigado por usar nossos sistemas')
        break

