# • Faça um programa que receba dois números inteiros e gere os números inteiros que estão no intervalo compreendido por eles.
numeroUm = int(input('Digite o primeiro inteiro: '))
numeroDois = int(input('Digite o segundo inteiro: '))
temp = numeroUm
lista = []
if numeroUm>numeroDois:
    numeroUm = numeroDois
    numeroDois = temp
for n in range (numeroUm,numeroDois+1):
    lista.append(n)
print (lista)