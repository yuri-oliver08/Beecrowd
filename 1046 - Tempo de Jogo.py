'''
Leia a hora inicial e a hora final de um jogo. 
A seguir calcule a duração do jogo, sabendo que o mesmo pode começar em um dia e terminar em outro.
Duração mínima de 1 hora e máxima de 24 horas.

Entrada
A entrada contém dois valores inteiros representando a hora de início e a hora de fim do jogo.

Saída
Apresente a duração do jogo conforme exemplo abaixo.
'''

horas = [x for x in range(0,24)]
entrada = input()
entradas = entrada.split()
inicio, fim = [int(h) for h in entradas]

i = horas.index(inicio)
counter = 0

if inicio == fim:
    counter = 24
else:
    while i != horas.index(fim):
        i = i + 1
        counter = counter + 1
        if i == 24:
            i = 0
            continue

print(f'O JOGO DUROU {counter} HORA(S)')