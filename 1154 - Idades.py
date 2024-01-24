'''
Faça um algoritmo para ler um número indeterminado de dados, contendo cada um, a idade de um indivíduo. 
O último dado, que não entrará nos cálculos, contém o valor de idade negativa. Calcular e imprimir a idade média deste grupo de indivíduos.

Entrada
A entrada contém um número indeterminado de inteiros. A entrada será encerrada quando um valor negativo for lido.

Saída
A saída contém um valor correspondente à média de idade dos indivíduos.

A média deve ser impressa com dois dígitos após o ponto decimal.
'''

lista = []
while True:
    idd = int(input())

    if idd < 0:
        break
    else:
        lista.append(idd)

media = (sum(lista))/len(lista)

print(f'{media:.2f}')   