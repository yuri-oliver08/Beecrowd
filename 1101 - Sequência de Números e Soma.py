'''
Leia um conjunto não determinado de pares de valores M e N (parar quando algum dos valores for menor ou igual a zero). 
Para cada par lido, mostre a sequência do menor até o maior e a soma dos inteiros consecutivos entre eles (incluindo o N e M).

Entrada
O arquivo de entrada contém um número não determinado de valores M e N. A última linha de entrada vai conter um número nulo ou negativo.

Saída
Para cada dupla de valores, imprima a sequência do menor até o maior e a soma deles, conforme exemplo abaixo.
'''

check = 1

while True:
    nums = input()
    interval = nums.split()
    intervalIn = [int(x) for x in interval]
    intervalIn.sort()
    numbers = []

    for n in intervalIn:
        if n <= 0:
            check = 0
    if check == 0:
        break

    for num in range(intervalIn[0], intervalIn[1]+1):
        numbers.append(num)

    numbersSTR = [str(x) for x in numbers]
    output = ' '.join(numbersSTR)

    print(f'{output} Sum={sum(numbers)}')