# • Faça um programa que leia um nome de usuário e a sua senha e não aceite a senha igual ao nome do usuário, mostrando uma mensagem de erro e voltando a pedir as informações.
print('Digite seu usuário e senha')
usuario = input('Digite seu usuário: ')
senha = input('Digite sua senha: ')
while usuario == senha:
    print('Usuário e senha não podem ser iguais')
    usuario = input('Digite seu usuário: ')
    senha = input('Digite sua senha: ')