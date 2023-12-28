'''
Leia 4 valores inteiros A, B, C e D. A seguir, se: 
B for maior do que C 
e se D for maior do que A, 
e a soma de C com D for maior que a soma de A e B 
e se C e D, ambos, forem positivos 
e se a variável A for par 
escrever a mensagem "Valores aceitos", senão escrever "Valores nao aceitos".

Entrada
Quatro números inteiros A, B, C e D.

Saída
Mostre a respectiva mensagem após a validação dos valores.
'''

entrada = input()
valores = entrada.split()

A = int(valores[0])
B = int(valores[1])
C = int(valores[2])
D = int(valores[3])

def conds(v1, v2, v3, v4):
    if (v2 > v3) and (v4 > v1) and ((v3 + v4) > (v1 + v2)) and (v3 and v4 > 0) and (v1 % 2 == 0):
        print('Valores aceitos') 
    else:
        print('Valores nao aceitos')

conds(A, B, C, D)
