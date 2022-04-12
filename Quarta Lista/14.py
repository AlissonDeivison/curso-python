# • Faça um programa que peça 10 números inteiros, calcule e mostre a quantidade de números pares e a quantidade de números impares.
print('Abaixo você digitará 10 números para verificar quais são ímpar e quais são par')
numeroUm = int(input('Digite um valor: '))
numeroDois = int(input('Digite um valor: '))
numeroTres = int(input('Digite um valor: '))
numeroQuatro = int(input('Digite um valor: '))
numeroCinco = int(input('Digite um valor: '))
numeroSeis = int(input('Digite um valor: '))
numeroSete = int(input('Digite um valor: '))
numeroOito = int(input('Digite um valor: '))
numeroNove = int(input('Digite um valor: '))
numeroDez = int(input('Digite um valor: '))
par = []
impar = []
lista = [numeroUm,numeroDois,numeroTres,numeroQuatro,numeroCinco,numeroSeis,numeroSete,numeroOito,numeroNove,numeroDez]
for n in lista:
    if n % 2 == 0:
        par.append(n)
    elif n % 2 != 0:
        impar.append(n)
print(f'Você digitou {len(par)} números par e {len(impar)} números ímpar')