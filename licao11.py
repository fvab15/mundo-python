# Faça um programa que leia a largura e a altura de uma parede em metros,
# calcule sua área
# e a quantidade de tinta necessária para pintá-la, sabendo que cada litro de tinta
# pinta uma área de 2m^2

l = int(input('largura: '))
a = int(input('altura: '))
area = l * a
tinta = area / 2
print('A área da parede em metros quadrados é igual a {}, e a \nquantidade de latas tinta necessaria para pinta-lá é {}'
      .format(area, tinta))