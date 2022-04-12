# • Desenvolva um gerador de tabuada, capaz de gerar a tabuada de qualquer número inteiro entre 1 a 10. O usuário deve informar de qual
# numero ele deseja ver a tabuada. A saída deve ser conforme o exemplo abaixo:
numeroUsuario = int(input('Digite o valor entre 1 e 10: '))

while numeroUsuario <= 1 or numeroUsuario > 10:
    print('Entrada inválida, o número inteiro deve ser maior que 1 e menor que 10')
    numeroUsuario = int(input('Digite o valor entre 1 e 10: '))

print(f'Tabuada de {numeroUsuario}: ')
for n in range(1,11):
    multi = n * numeroUsuario
    print(f'{numeroUsuario} x {n} = {multi}')
