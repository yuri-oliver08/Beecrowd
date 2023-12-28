'''
Leia um valor inteiro. A seguir, calcule o menor número de notas possíveis (cédulas) no qual o valor pode ser decomposto.
As notas consideradas são de 100, 50, 20, 10, 5, 2 e 1. 
A seguir mostre o valor lido e a relação de notas necessárias.

Entrada
O arquivo de entrada contém um valor inteiro N (0 < N < 1000000).

Saída
Imprima o valor lido e, em seguida, a quantidade mínima de notas de cada tipo necessárias, conforme o exemplo fornecido. 
Não esqueça de imprimir o fim de linha após cada linha, caso contrário seu programa apresentará a mensagem: “Presentation Error”.
'''

cedulas = [100, 50, 20, 10, 5, 2, 1]
N = int(input())
msg = []
iter = 0

while iter != N:
    for cedula in cedulas:
        count = 0
        while iter + cedula <= N:
            iter += cedula
            count += 1
        msg.append(f'{count} nota(s) de R$ {cedula},00')

separador = '\n'
msgF = separador.join(msg)

print(f'{N}\n{msgF}')