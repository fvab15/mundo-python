# desenvolva um programa que leia as duas notas de um aluno, calcule e mostre a sua média

n1 = int(input('nota 1: '))
n2 = int(input('nota 2: '))
n3 = int(input('nota 3: '))
c = (n1 + n2 + n3) / 3
print('a média é {:.2f}'.format(c))
