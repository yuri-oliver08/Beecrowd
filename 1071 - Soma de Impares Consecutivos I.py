'''
Leia 2 valores inteiros X e Y. A seguir, calcule e mostre a soma dos números impares entre eles.

Entrada
O arquivo de entrada contém dois valores inteiros.

Saída
O programa deve imprimir um valor inteiro. Este valor é a soma dos valores ímpares que estão entre os valores fornecidos na entrada que deverá caber em um inteiro.
'''

def numeros_impares(inicio, fim):
    if inicio < fim:
        lista = [i for i in range(inicio+1, fim -1) if i % 2 != 0]
    else:
        lista = [i for i in range(fim + 1, inicio) if i % 2 != 0]
    return lista

num1,num2 = int(input()),int(input())


impares = numeros_impares(num1,num2)

soma = sum(impares)

print(soma)



    