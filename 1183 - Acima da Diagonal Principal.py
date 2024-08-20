'''
Leia um caractere maiúsculo, que indica uma operação que deve ser realizada e uma matriz M[12][12]. 
Em seguida, calcule e mostre a soma ou a média considerando somente aqueles elementos que estão acima da diagonal principal da matriz, conforme ilustrado abaixo (área verde).

Entrada
A primeira linha de entrada contem um único caractere Maiúsculo O ('S' ou 'M'), indicando a operação (Soma ou Média) que deverá ser realizada com os elementos da matriz. Seguem os 144 valores de ponto flutuante que compõem a matriz.

Saída
Imprima o resultado solicitado (a soma ou média), com 1 casa após o ponto decimal.
'''

op = input()
m = [[0 for _ in range(12)] for _ in range(12)]

for i in range(12):
    for j in range(12):
        m[i][j] = float(input())


elementos_acima_diagonal = []

for i in range(12):
    for j in range(i + 1, 12):
        elementos_acima_diagonal.append(m[i][j])

if op == 'S':
    soma = sum(elementos_acima_diagonal)
    print(f'{soma:.1f}')
elif op == 'M':
    media = sum(elementos_acima_diagonal) / len(elementos_acima_diagonal)
    print(f'{media:.1f}')