# • Faça um Programa que leia três números e mostre-os em ordem decrescente.
numeroUm = float(input())
numeroDois = float(input())
numeroTres = float(input())
listaNumeros = [numeroUm,numeroDois,numeroTres]
listaNumeros.sort(reverse=True)
for numero in listaNumeros:
    print(numero)
