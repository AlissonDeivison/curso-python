# • Faça um programa que imprima na tela apenas os números ímpares entre 1 e 50.
lista = []
for n in range (1,50+1):
    if n%2!=0:
        lista.append(n)
print(lista)