# • Faça um Programa que pergunte em que turno você estuda. Peça para digitar M-matutino ou V-Vespertino ou N-Noturno. Imprima a
# mensagem "Bom Dia!", "Boa Tarde!" ou "Boa Noite!" ou "Valor Inválido!", conforme o caso.
print('Informe seu turno\nDigite "M" para matutino, "V" para vespertino ou "N" para noturno.')
entradaTurno = input('Turno: ')
if entradaTurno.upper() == "M":
        print('Bom dia')
elif entradaTurno.upper() == "V":
        print('Boa tarde')
elif entradaTurno.upper() == "N":
        print('Boa noite')
else:
        print('Não é uma entrada válida')