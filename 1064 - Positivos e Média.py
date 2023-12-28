'''
Leia 6 valores. 
Em seguida, mostre quantos destes valores digitados foram positivos. 
Na próxima linha, deve-se mostrar a média de todos os valores positivos digitados, com um dígito após o ponto decimal.

Entrada
A entrada contém 6 números que podem ser valores inteiros ou de ponto flutuante. 
Pelo menos um destes números será positivo.

Saída
O primeiro valor de saída é a quantidade de valores positivos. 
A próxima linha deve mostrar a média dos valores positivos digitados.
'''

entradas = [float(input()) for x in range(6)]

entradasP = [entrada for entrada in entradas if entrada >= 0]

count = len(entradasP)

sum = 0
for i in range(count):
    
    sum = sum + entradasP[i]

calc = sum / count

print(f'{count} valores positivos\n{calc:.1f}')