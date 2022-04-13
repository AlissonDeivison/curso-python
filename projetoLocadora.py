print('Locadora Agix')
print('Sistema de locação de filmes')
print('Menu Principal: \n1) Lista de filmes disponíveis\n2) Locar um filme disponível\n3) Listar os filmes que loquei\n4) Devolver um filme\n5) Sair do programa')

# Lista de filmes disponíveis
filmesAcao = ['Resgate - (Categoria: Ação)', 'Batman: O cavaleiro das trevas - (Categoria: Ação)', 'John Wick – De Volta ao Jogo - (Categoria: Ação)', 'Em Ritmo de Fuga - (Categoria: Ação)',
              'Mad Max: Estrada da Fúria (Categoria: Ação)', 'Kingsman: Serviço Secreto - (Categoria: Ação)']
filmesAventura = ['Logan - (Categoria: Aventura)', 'Operação Dragão - (Categoria: Aventura)', 'Star Trek - (Categoria: Aventura)', 'Star Wars: Os Últimos Jedi - (Categoria: Aventura)', 'Mulher-Maravilha - (Categoria: Aventura)',
                  'Homem-Aranha no Aranhaverso - (Categoria: Aventura)']
filmesFantasia = ['Avatar - (Categoria: Fantasia)', 'Oz: Mágico e Poderoso - (Categoria: Fantasia)', 'A Bela e a Fera - (Categoria: Fantasia)', 'Labirinto - A Magia do Tempo - (Categoria: Fantasia)',
                  'A História Sem Fim - (Categoria: Fantasia)', 'O Mágico de Oz - (Categoria: Fantasia)']

#Lista de Filmes locados
filmesLocados = []
filmesDevolvidos = []
#Menu de opções

while True:
    opcao = int(input('Digite uma opção do menu principal: '))
    #Verificador de opção do menu digitada
    while opcao > 5 or opcao < 1:
        print('Opção inválida.\n1) Lista de filmes disponíveis\n2) Locar um filme disponível\n3) Listar os filmes que loquei\n4) Sair do programa')
        opcao = int(input('Digite uma opção do menu principal: '))

    if opcao == 1:
        print('Categorias:\n1) Ação\n2) Aventura\n3) Fantasia')
        escolhaCategoria = int(input('Qual categoria de filmes deseja verificar? '))
        #Verificador de opção de categoria
        while escolhaCategoria > 3 or escolhaCategoria < 1:
            print('Opção inválida\nCategorias:\n1) Ação\n2) Aventura\n3) Fantasia')
            escolhaCategoria = int(input('Qual categoria de filmes deseja verificar? '))

        if escolhaCategoria == 1:
            for n in range(len(filmesAcao)):
                print('{} - {}'.format(n+1,filmesAcao[n]))
        elif escolhaCategoria == 2:
            for n in range(len(filmesAventura)):
                print('{} - {}'.format(n + 1, filmesAventura[n]))
        elif escolhaCategoria == 3:
            for n in range(len(filmesFantasia)):
                print('{} - {}'.format(n + 1, filmesFantasia[n]))

    elif opcao == 2:

        print('Deseja adicionar um novo filme a sua lista de locações? Digite "1" para sim e "2" para não')
        continuar = int(input('1 - Sim\n2 - Não\n'))
        while continuar != 1 and continuar != 2:
                print('Opção inválida')
                continuar = int(input('Digite "1" para sim e "2" para não: '))
        if continuar == 1:
            print('Escolha uma categoria de filmes disponíveis.\n1) Ação\n2) Aventura\n3) Fantasia')
            escolhaCategoria = int(input('Qual categoria de filmes deseja locar? '))
            # Verificador de opção de categoria
            while escolhaCategoria > 3 or escolhaCategoria < 0:
                print('Opção inválida\nCategorias:\n1) Ação\n2) Aventura\n3) Fantasia')
                escolhaCategoria = int(input('Qual categoria de filmes deseja verificar? '))

            if escolhaCategoria == 1: # Categoria 1 - Filmes de Ação
                n = 0
                print('Qual filme deseja locar?')
                for filme in filmesAcao:
                    n+=1
                    print('{} - {}'.format(n, filme))
                print('Digite o número do filme da lista apresentada')
                filmeEscolhido = int(input('Qual deseja escolher?'))
                while filmeEscolhido > (len(filmesAcao)): # Verificação de opção correta do filme
                    print('Opção indisponível')
                    filmeEscolhido = int(input('Qual deseja escolher?'))
                filmesLocados.append(filmesAcao[filmeEscolhido-1])
                filmesAcao.remove(filmesAcao[filmeEscolhido-1])
            elif escolhaCategoria == 2: # Categoria 2 - Filmes de Aventura
                n = 0
                print('Qual filme deseja locar?')
                for filme in filmesAventura:
                    n += 1
                    print('{} - {}'.format(n, filme))
                print('Digite o número do filme da lista apresentada')
                filmeEscolhido = int(input('Qual deseja escolher?'))
                while filmeEscolhido > (len(filmesAventura)): # Verificação de opção correta do filme
                    print('Opção indisponível')
                    filmeEscolhido = int(input('Qual deseja escolher?'))
                filmesLocados.append(filmesAventura[filmeEscolhido-1])
                filmesAventura.remove(filmesAventura[filmeEscolhido-1])
            elif escolhaCategoria == 3: # Categoria 2 - Filmes de Fantasia
                n = 0
                print('Qual filme deseja locar?')
                for filme in filmesFantasia:
                    n += 1
                    print('{} - {}'.format(n, filme))
                print('Digite o número do filme da lista apresentada')
                filmeEscolhido = int(input('Qual deseja escolher?'))
                while filmeEscolhido > (len(filmesFantasia)):  # Verificação de opção correta do filme
                    print('Opção indisponível')
                    filmeEscolhido = int(input('Qual deseja escolher?'))
                filmesLocados.append(filmesFantasia[filmeEscolhido - 1])
                filmesFantasia.remove(filmesFantasia[filmeEscolhido - 1])
        elif continuar == 2:
            continue

    elif opcao == 3:
        print('Lista de filmes locados: ')
        l = 0
        for locados in filmesLocados:
            l+=1
            print('{} - {}'.format(l,locados))

    elif opcao == 4:
        print('Qual filme quer devolver? ')
        a = 0
        for locados in filmesLocados:
            a += 1
            print('{} - {}'.format(a, locados))
        devolucao = int(input('Digite o número correspondente ao filme que deseja devolver: '))
        while devolucao > (len(filmesLocados)):
            print('Opção inválida')
            devolucao = int(input('Digite o número correspondente ao filme que deseja devolver: '))
        filmesDevolvidos.append(filmesLocados[devolucao-1])
        filmesLocados.remove(filmesLocados[devolucao - 1])
        print('{} - Devolvido'.format(filmesDevolvidos))
