# • Faça um programa que calcule o fatorial de um número inteiro fornecido pelo usuário. Ex.: 5!=5.4.3.2.1=120

numero = int(input('Digite um inteiro para verificar o fatorial: '))
listaNumero = []
fatoracaoFinal = 1
if numero < 0:
    print('Não é possível fatorar um número negativo')
elif numero == 0:
    print('Fatorial de 0 é 1')
else:
    for n in range(1,numero+1):
        listaNumero.append(n)
    listaNumero.sort(reverse=True)
    for num in listaNumero:
        fatoracaoFinal = fatoracaoFinal*num
    print(fatoracaoFinal)