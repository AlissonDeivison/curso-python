# • Faça um programa que peça uma nota, entre zero e dez. Mostre uma mensagem caso o valor seja inválido e continue pedindo até que o
# usuário informe um valor válido
print('Digite uma nota entre 0 e 10.')
nota = float(input('Digite sua nota: '))
while nota < 0 or nota > 10:
    print('Inválida, a nota tem que ficar no intervalo entre 0 e 10.')
    nota = float(input('Digite sua nota: '))
