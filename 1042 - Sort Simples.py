'''
Leia 3 valores inteiros e ordene-os em ordem crescente. 
No final, mostre os valores em ordem crescente, uma linha em branco e em seguida, os valores na sequência como foram lidos.

Entrada
A entrada contem três números inteiros.

Saída
Imprima a saída conforme foi especificado.
'''

entrada = input()
valores = entrada.split()

valoresF = [eval(i) for i in valores]
valoresF.sort()
print(f'{valoresF[0]}\n{valoresF[1]}\n{valoresF[2]}')
print('')


print(f'{valores[0]}\n{valores[1]}\n{valores[2]}')

