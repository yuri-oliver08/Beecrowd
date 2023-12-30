'''
Maria acabou de iniciar seu curso de graduação na faculdade de medicina e precisa de sua ajuda para organizar os experimentos de um laboratório o qual ela é responsável. 
Ela quer saber no final do ano, quantas cobaias foram utilizadas no laboratório e o percentual de cada tipo de cobaia utilizada.

Este laboratório em especial utiliza três tipos de cobaias: sapos, ratos e coelhos. 
Para obter estas informações, ela sabe exatamente o número de experimentos que foram realizados, o tipo de cobaia utilizada e a quantidade de cobaias utilizadas em cada experimento.

Entrada
A primeira linha de entrada contém um valor inteiro N que indica os vários casos de teste que vem a seguir. 
Cada caso de teste contém um inteiro Quantia (1 ≤ Quantia ≤ 15) que representa a quantidade de cobaias utilizadas e um caractere Tipo ('C', 'R' ou 'S'), indicando o tipo de cobaia (R:Rato S:Sapo C:Coelho).

Saída
Apresente o total de cobaias utilizadas, o total de cada tipo de cobaia utilizada e o percentual de cada uma em relação ao total de cobaias utilizadas.
O percentual deve ser apresentado com dois dígitos após o ponto.
'''

num = int(input())

entradas = [input() for x in range(num)]

R,S,C = 0,0,0

for i in range(len(entradas)):
    atual = entradas[i]
    sep = atual.split()
    quant = int(sep[0])
    let = sep[1]
    #print(sep,quant,let)

    match let:
        case 'R':
            R = R + quant
        case 'S':
            S = S + quant
        case 'C':
            C = C + quant

total = R + S + C

print(f'Total: {total} cobaias')
print(f'Total de coelhos: {C}\nTotal de ratos: {R}\nTotal de sapos: {S}')
print(f'Percentual de coelhos: {((C*100)/total):.2f} %\nPercentual de ratos: {((R*100)/total):.2f}\nPercentual de sapos: {((S*100)/total):.2f} %')
