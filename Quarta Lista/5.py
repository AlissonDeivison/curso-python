# • Altere o programa anterior permitindo ao usuário informar as populações e as taxas de crescimento iniciais. Valide a entrada e permita
# repetir a operação
while True:
    print(('Gostaria de iniciar o cálculo?\n1) Sim\n2) Não'))
    entrada = (input('Digite sua opção: '))
    if entrada == '1':
        populacaoA = int(input('Digite a primeira população: '))
        populacaoB = int(input('Digite a segunda população: '))
        crescimentoIniciaA = float(input('Digite o crescimento da primeira população: '))
        crescimentoIniciaB = float(input('Digite o crescimento da segunda população: '))
        anos = 0
        if populacaoA > 0 and populacaoB > 0:
            if populacaoA > populacaoB:
                while populacaoA > populacaoB:
                    populacaoA = populacaoA*crescimentoIniciaA
                    populacaoB = populacaoB*crescimentoIniciaB
                    anos += 1
                print(f'Levará {anos} anos para a segunda população se equiparar ou passar a primeira.')
            elif populacaoB > populacaoA:
                while populacaoB > populacaoA:
                    populacaoA = populacaoA*crescimentoIniciaA
                    populacaoB = populacaoB*crescimentoIniciaB
                    anos += 1
                print(f'Levará {anos} anos para a primeira população se equiparar ou passar a segunda.')
        elif populacaoA <= 0 or populacaoB <= 0:
            print('População precisa ser maior que 0')
            continue
    elif entrada == '2':
        break