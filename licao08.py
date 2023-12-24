# Escreva um programa que leia um valor em metros e o exiba convertido em centímetros e milímetros

valor = float(input('Valor em metros: '))
valor_cm = valor*100
valor_mm = valor*1000
print('o valor em cm é {}, e o valor em mm é {}'.format(valor_cm, valor_mm))