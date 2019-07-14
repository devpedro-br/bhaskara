# coding: utf-8
import math
a = float(input('A: '))
b = float(input('B: '))
c = float(input('C: '))
print('')
delta = math.pow(b, 2) - 4 * a * c

if delta < 0:
    print('O valor de Delta é negativo: {}'.format(delta))
    print('########################')
else:
    x1 = (-(b) + math.sqrt(delta)) / 2 * a
    x2 = (-(b) - math.sqrt(delta)) / 2 * a
    print('Para a equação de segundo grau temos:')
    print('##########################')
    print('A: {}  B: {}  C: {}'.format(a, b, c))
    print('Delta: {}'.format(delta))
    print('##########################')
    print('O valor de x1: {}\nO valor de x2: {}'.format(x1, x2))
    print('##########################')
