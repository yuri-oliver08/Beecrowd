'''
Escreva um programa para ler as coordenadas (X,Y) de uma quantidade indeterminada de pontos no sistema cartesiano. 
Para cada ponto escrever o quadrante a que ele pertence. O algoritmo será encerrado quando pelo menos uma de duas coordenadas for NULA (nesta situação sem escrever mensagem alguma).

Entrada
A entrada contém vários casos de teste. Cada caso de teste contém 2 valores inteiros.

Saída
Para cada caso de teste mostre em qual quadrante do sistema cartesiano se encontra a coordenada lida, conforme o exemplo.

'''

check = 1

while True:

    entrada = input()
    valores = entrada.split()

    X,Y = int(valores[0]), int(valores[1])

    nums = [X,Y]

    for n in nums:
        if n == 0:
            check = 0

    if check == 0:
        break
    else:
        if X > 0 and Y > 0:
            print('primeiro')
        elif X < 0 and Y > 0:
            print('segundo')
        elif X < 0 and Y < 0:
            print('terceiro')
        elif X > 0 and Y < 0:
            print('quarto')