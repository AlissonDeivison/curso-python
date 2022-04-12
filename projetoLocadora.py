print('Locadora Agix')
print('Sistema de locação de filmes')
print('Menu Principal: \n1) Lista de filmes disponíveis\n2) Locar um filme disponível\n3) Listar os filmes que loquei\n4) Sair do programa')

# Lista de filmes disponíveis
filmesAcao = ['Resgate', 'Batman: O cavaleiro das trevas', 'John Wick – De Volta ao Jogo', 'Em Ritmo de Fuga',
              'Mad Max: Estrada da Fúria', 'Kingsman: Serviço Secreto']
filmesAventura = ['Logan', 'Operação Dragão', 'Star Trek', 'Star Wars: Os Últimos Jedi', 'Mulher-Maravilha',
                  'Homem-Aranha no Aranhaverso']
filmesFantasia = ['Avatar', 'Oz: Mágico e Poderoso', 'A Bela e a Fera', 'Labirinto - A Magia do Tempo',
                  'A História Sem Fim', 'O Mágico de Oz']

#Lista de Filmes locados
filmesLocados = []
#Menu de opções

while True:
    opcao = int(input('Digite uma opção do menu principal: '))
    #Verificador de opção do menu digitada
    while opcao > 4 or opcao < 1:
        print('Opção inválida.\n1) Lista de filmes disponíveis\n2) Locar um filme disponível\n3) Listar os filmes que loquei\n4) Sair do programa')
        opcao = int(input('Digite uma opção do menu principal: '))

    if opcao == 1:
        print('Categorias:\n1) Ação\n2) Aventura\n3) Fantasia\nPara sair digite qualquer outra tecla')
        escolhaCategoria = int(input('Qual categoria de filmes deseja verificar? '))

        #Verificador de opção de categoria
        while escolhaCategoria > 3 or escolhaCategoria < 1:
            print('Opção inválida\nCategorias:\n1) Ação\n2) Aventura\n3) Fantasia\nPara sair digite qualquer outra tecla')
            escolhaCategoria = int(input('Qual categoria de filmes deseja verificar? '))
        if escolhaCategoria == 1:
            print('A lista de filmes disponíves é: {}'.format(filmesAcao))
        elif escolhaCategoria == 2:
            print('A lista de filmes disponíves é: {}'.format(filmesAventura))
        elif escolhaCategoria == 3:
            print('A lista de filmes disponíves é: {}'.format(filmesFantasia))

    elif opcao == 2:
            print('Escolha uma categoria de filmes disponíveis.\n1) Ação\n2) Aventura\n3) Fantasia')
            escolhaCategoria = int(input('Qual categoria de filmes deseja locar? '))
            # Verificador de opção de categoria
            while escolhaCategoria > 3 or escolhaCategoria < 0:
                print('Opção inválida\nCategorias:\n1) Ação\n2) Aventura\n3) Fantasia\nPara sair digite qualquer outra tecla')
                escolhaCategoria = int(input('Qual categoria de filmes deseja verificar? '))

            if escolhaCategoria == 1:
                n = 0
                print('Qual filme deseja locar?')
                for filme in filmesAcao:
                    n+=1
                    print('{} - {}'.format(n, filme))
                print('Digite o número do filme da lista apresentada')
                filmeEscolhido = int(input('Qual deseja escolher?'))

                #Verificação de opção correta do filme
                while filmeEscolhido > (len(filmesAcao)):
                    print('Opção indisponível')
                    filmeEscolhido = int(input('Qual deseja escolher?'))

                #Atualizando a lista de filmes locados
                if filmeEscolhido == 1:
                        filmesLocados.append(filmesAcao[0])
                elif filmeEscolhido == 2:
                        filmesLocados.append(filmesAcao[1])
                elif filmeEscolhido == 3:
                        filmesLocados.append(filmesAcao[2])
                elif filmeEscolhido == 3:
                        filmesLocados.append(filmesAcao[2])
                elif filmeEscolhido == 4:
                        filmesLocados.append(filmesAcao[3])
                elif filmeEscolhido == 5:
                        filmesLocados.append(filmesAcao[4])
                elif filmeEscolhido == 6:
                        filmesLocados.append(filmesAcao[5])

            elif escolhaCategoria == 2:
                n = 0
                print('Qual filme deseja locar?')
                for filme in filmesAventura:
                    n += 1
                    print('{} - {}'.format(n, filme))
                print('Digite o número do filme da lista apresentada')
                filmeEscolhido = int(input('Qual deseja escolher?'))

                # Verificação de opção correta do filme
                while filmeEscolhido > (len(filmesAventura)):
                    print('Opção indisponível')
                    filmeEscolhido = int(input('Qual deseja escolher?'))
                # Atualizando a lista de filmes locados
                if filmeEscolhido == 1:
                    filmesLocados.append(filmesAventura[0])
                elif filmeEscolhido == 2:
                    filmesLocados.append(filmesAventura[1])
                elif filmeEscolhido == 3:
                    filmesLocados.append(filmesAventura[2])
                elif filmeEscolhido == 3:
                    filmesLocados.append(filmesAventura[2])
                elif filmeEscolhido == 4:
                    filmesLocados.append(filmesAventura[3])
                elif filmeEscolhido == 5:
                    filmesLocados.append(filmesAventura[4])
                elif filmeEscolhido == 6:
                    filmesLocados.append(filmesAventura[5])
            elif escolhaCategoria == 3:
                n = 0
                print('Qual filme deseja locar?')
                for filme in filmesFantasia:
                    n += 1
                    print('{} - {}'.format(n, filme))
                print('Digite o número do filme da lista apresentada')
                filmeEscolhido = int(input('Qual deseja escolher?'))

                # Verificação de opção correta do filme
                while filmeEscolhido > (len(filmesFantasia)):
                    print('Opção indisponível')
                    filmeEscolhido = int(input('Qual deseja escolher?'))

                # Atualizando a lista de filmes locados
                if filmeEscolhido == 1:
                    filmesLocados.append(filmesFantasia[0])
                elif filmeEscolhido == 2:
                    filmesLocados.append(filmesFantasia[1])
                elif filmeEscolhido == 3:
                    filmesLocados.append(filmesFantasia[2])
                elif filmeEscolhido == 3:
                    filmesLocados.append(filmesFantasia[2])
                elif filmeEscolhido == 4:
                    filmesLocados.append(filmesFantasia[3])
                elif filmeEscolhido == 5:
                    filmesLocados.append(filmesFantasia[4])
                elif filmeEscolhido == 6:
                    filmesLocados.append(filmesFantasia[5])
    elif opcao == 3:
        print('Lista de filmes locados: ')
        l = 0
        for locados in filmesLocados:
            l+=1
            print('{} - {}'.format(l,locados))
    elif opcao == 4:
        print('A locadora Agix agradece sua preferência')
        break