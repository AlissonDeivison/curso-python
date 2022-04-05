# • Faça um Programa que verifique se uma letra digitada é vogal ou consoante.
print('Verificador de letras')
msg = 'é uma consoante'
letraEntrada = input('Digite uma letra: ')
vogais = ['A','E','I','O','U']
for vogal in vogais:
    if letraEntrada.upper() == vogal:
        msg = 'é uma vogal'
        break
print('"{}" {}'.format(letraEntrada.upper(),msg))