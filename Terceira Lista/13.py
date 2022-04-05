# • Faça um Programa que leia um número inteiro menor que 1000 e imprima a quantidade de centenas, dezenas e unidades do mesmo.
# • Observando os termos no plural a colocação do "e", da vírgula entre outros. Exemplo:
# • 326 = 3 centenas, 2 dezenas e 6 unidades
# • 12 = 1 dezena e 2 unidades Testar com: 326, 300, 100, 320, 310,305, 301, 101, 311, 111, 25, 20, 10, 21, 11, 1, 7 e 16

print('Contador de centenas, dezenas e unidades')
valor = int(input('Digite um valor menor que 1000: '))
centenas = int(valor/100)
dezenas = int((valor-(centenas*100))//10)
unidades = int(valor-(centenas*100+dezenas*10))

if centenas == 1:
    cent = 'centena'
elif centenas > 1 or centenas == 0:
    cent = 'centenas'
if dezenas > 1 or dezenas == 0:
    dez = 'dezenas'
elif dezenas == 1 :
    dez = 'dezena'
if unidades == 1:
    uni = 'unidade'
elif unidades > 1 or unidades == 0:
    uni = 'unidades'
if centenas > 0:
    # print(centenas,dezenas,unidades)
    print('{} {} , {} {} e {} {}'.format(centenas,cent,dezenas,dez,unidades,uni))
elif centenas == 0:
    print('{} {} , {} {} e {} {}'.format(centenas,cent,dezenas,dez,unidades,uni))
