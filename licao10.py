# Crie um programa que leia quanto dinheiro uma pessoa tem na carteira e mostre quantos dólares ela pode comprar

n = float(input('digite o valor: '))
d = 1/4.79 * n
print('o valor em reais é {}, e em dolares é {:.2f}'.format(n, d))