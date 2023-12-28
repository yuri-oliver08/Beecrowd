'''
A empresa ABC resolveu conceder um aumento de salários a seus funcionários de acordo com a tabela abaixo:

Salário	Percentual de Reajuste
0 - 400.00 => 15%
400.01 - 800. => 12%
800.01 - 1200. => 10%
1200.01 - 2000. => 7%
Acima de 2000. => 4%

Leia o salário do funcionário e calcule e mostre o novo salário, bem como o valor de reajuste ganho e o índice reajustado, em percentual.

Entrada
A entrada contém apenas um valor de ponto flutuante, com duas casas decimais.

Saída
Imprima 3 linhas na saída: o novo salário, o valor ganho de reajuste (ambos devem ser apresentados com 2 casas decimais) e o percentual de reajuste ganho.
'''

salario = float(input())
perc = 0

if 0 <= salario <= 400.00:
    perc = 0.15
elif 400.01 <= salario <= 800.00:
    perc = 0.12
elif 800.01 <= salario <= 1200.00:
    perc = 0.10
elif 1200.01 <= salario <= 2000.00:
    perc = 0.07
elif salario > 2000.00:
    perc = 0.04

salarioNew = (salario * perc) + salario
reajuste = salarioNew - salario

print(f'Novo salario: {salarioNew:.2f}')
print(f'Reajuste ganho: {reajuste:.2f}')
print(f'Em percentual: {perc*100:.0f} %')