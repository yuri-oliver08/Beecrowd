'''
Leia 1 valor inteiro N, que representa o número de casos de teste que vem a seguir. Cada caso de teste consiste de 3 valores reais, cada um deles com uma casa decimal. Apresente a média ponderada para cada um destes conjuntos de 3 valores, sendo que o primeiro valor tem peso 2, o segundo valor tem peso 3 e o terceiro valor tem peso 5.

Entrada
O arquivo de entrada contém um valor inteiro N na primeira linha. Cada N linha a seguir contém um caso de teste com três valores com uma casa decimal cada valor.

Saída
Para cada caso de teste, imprima a média ponderada dos 3 valores, conforme exemplo abaixo.
'''

num = int(input())
entradas = [input() for x in range(num)]

for i in range(len(entradas)):
    valores = entradas[i].split()

    calc = (float(valores[0])*2 + float(valores[1])*3 + float(valores[2])*5)/10
    print(f'{calc:.1f}')