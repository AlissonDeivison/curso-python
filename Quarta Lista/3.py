# • Faça um programa que leia e valide as seguintes informações:
# • Nome: maior que 3 caracteres;
# • Idade: entre 0 e 150;
# • Salário: maior que zero;
# • Sexo: 'f' ou 'm';
# • Estado Civil: 's', 'c', 'v', 'd’

nome = input('Digite seu nome: ')
idade = int(input('Digite sua idade: '))
salario = float(input('Informe o seu salário: '))
sexo = input('Qual o seu sexo? ')
estadoCivil = input('Qual o seu estado civil? ')

while len(nome) < 3:
    print('Nome inválido, deve ter no mínimo 4 caracteres')
    nome = input('Digite seu nome: ')
while idade < 0 or idade > 150:
    print('Idade inválida, deve possuir entra 0 e 150 anos')
    idade = int(input('Digite sua idade: '))
while salario < 0:
    print('Salário inválido, deve ser maior que zero')
    salario = float(input('Informe o seu salário: '))
while not sexo[0].upper() in 'FM':
    print('Sexo inválido, digite "F" para femino ou "M" para masculino')
    sexo = input('Qual o seu sexo? ')
while not estadoCivil[0].upper() in 'SCVD':
    print('Estado civil inválido, digite "S" - Solteiro, "C" - Casado, "V" - Viúvo, "D" - Divorciado')
    estadoCivil = input('Qual o seu estado civil? ')
