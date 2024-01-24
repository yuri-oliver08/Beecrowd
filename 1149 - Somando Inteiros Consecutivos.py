'''
Faça um algoritmo para ler um valor A e um valor N. Imprimir a soma de A + i para cada i com os valores (0 <= i <= N-1). 
Enquanto N for negativo ou ZERO, um novo N(apenas N) deve ser lido.

Entrada
A entrada contém somente valores inteiros, podendo ser positivos ou negativos. Todos os valores estão na mesma linha.

Saída
A saída contém apenas um valor inteiro.
'''

entrada = input()
nums = [int(x) for x in entrada.split()]
elementos = [n for n in nums if n > 0]
resultado = []

while True:

    for n in range(0, elementos[1]):
        soma = elementos[0] + n
        resultado.append(soma)
    break

print(sum(resultado))

        

