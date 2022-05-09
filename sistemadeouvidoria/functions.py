def menu():
    main_menu = ['1) Listar todas manifestações',
                 '2) Listar todas as sugestões',
                 '3) Listar todas as reclamações',
                 '4) Listar todos os elogios',
                 '5) Criar nova manifestação',
                 '6) Pesquisar manifestação pelo protocolo',
                 '7) Sair']
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
