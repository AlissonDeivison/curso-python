# • Faça um programa que leia 5 números e informe a soma e a média dos números.


numeroUm = float(input('Digite um número: '))
numeroDois = float(input('Digite um número: '))
numeroTres = float(input('Digite um número: '))
numeroQuatro = float(input('Digite um número: '))
numeroCinco = float(input('Digite um número: '))
soma = numeroUm+numeroDois+numeroTres+numeroQuatro+numeroCinco
media = soma/5
print(f'A soma dos valores é {soma}\nA média é {media}')