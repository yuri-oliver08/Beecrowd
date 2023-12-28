'''
Leia os quatro valores correspondentes aos eixos x e y de dois pontos quaisquer no plano, p1(x1,y1) e p2(x2,y2) e calcule a distância entre eles, mostrando 4 casas decimais após a vírgula.

Entrada
O arquivo de entrada contém duas linhas de dados. A primeira linha contém dois valores de ponto flutuante: x1 y1 e a segunda linha contém dois valores de ponto flutuante x2 y2.

Saída
Calcule e imprima o valor da distância segundo a fórmula fornecida, com 4 casas após o ponto decimal.
'''

import math

input1 = input()
input2 = input()

quebra1 = input1.split()
quebra2 = input2.split()

p1 = [float(x) for x in quebra1]
p2 = [float(x) for x in quebra2]

distancia = math.sqrt((p2[0] - p1[0])**2 + (p2[1] - p1[1])**2)


print(round(distancia, 4))
