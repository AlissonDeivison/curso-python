# 8 - Faça um programa que pede duas notas de um aluno. Em seguida deve calculcar a média do aluno e dar o seguinte resultado:
# a) A mensagem Aprovado, se a média alcançada for maior ou igual a sete;
# b) A mensagem Reprovado, se a média for menor que sete;
# c) A mensagem Aprovado com Distinção, se a média for igual a dez.
gradeA = float(input('Digite sua primera nota: '))
gradeB = float(input('Digite sua segunda nota: '))
#Calculations
media = (gradeA+gradeB)/2
if media < 7:
  print('Reprovado')
elif media >= 7 and media != 10:
  print('Aprovado')
elif media == 10:
  print('Aprovado com Distinção')