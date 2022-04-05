# • Faça um Programa que verifique se uma letra digitada é "F" ou "M". Conforme a letra escrever: F -Feminino, M -Masculino, Sexo Inválido.
print('Verificador de Sexo')
sexoEntrada = input('Digite "M" ou "H": ')
if sexoEntrada.upper() == 'M':
    print('Mulher')
elif sexoEntrada.upper() == 'H':
    print('Homem')
else:
    print('Entrada inválida')