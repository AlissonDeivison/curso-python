# 12 - Faça um programa que lê duas notas parciais obtidas por um aluno numa disciplina ao longo de um semestre, e calcule a sua média. A atribuição de conceitos deve obedecer a tabela:
# Conceito A: Entre 9 e 10, Conceito B: Entre 7.5 e 9, Conceito C: Entre 6 e 7.5, Conceito D: Entre 4 e 6, Conceito E: Entre 0 e 4

#grades
a = 10
b = 9
c = 7.5
d = 6
e = 4

gradeA = float(input('Digite sua primeira nota: '))
gradeB = float(input('Digite sua segunda nota: '))
media = (gradeA+gradeB)/2

if media < e:
    print('Conceito E')
elif media >= e and media<d:
    print('Conceito D')
elif media >= d and < c:
    print('Conceito C')
elif media >=c and media<b:
    print('Conceito B')
else:
    print('Conceito A')