# • Faça um programa que receba dois números inteiros e gere os números inteiros que estão no intervalo compreendido por eles.
# • Altere o programa anterior para mostrar no final a soma dos números.

numeroUm = int(input('Digite o primeiro inteiro: '))
numeroDois = int(input('Digite o segundo inteiro: '))
temp = numeroUm
lista = []
soma = 0
if numeroUm>numeroDois:
    numeroUm = numeroDois
    numeroDois = temp
for n in range (numeroUm,numeroDois+1):
    lista.append(n)
    soma+=n
print (f'A lista de números inteiros no intervalo definido pelo usuário é: {lista}\nA soma desses números é {soma}')