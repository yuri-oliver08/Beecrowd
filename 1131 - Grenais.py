'''
A Federação Gaúcha de Futebol contratou você para escrever um programa para fazer uma estatística do resultado de vários GRENAIS. 
Escreva um programa para ler o número de gols marcados pelo Inter e pelo Grêmio em um GRENAL. 
Logo após escrever a mensagem "Novo grenal (1-sim 2-nao)" e solicitar uma resposta. 
Se a resposta for 1, o algoritmo deve ser executado novamente solicitando o número de gols marcados pelos times em uma nova partida, caso contrário deve ser encerrado imprimindo:

- Quantos GRENAIS fizeram parte da estatística.
- O número de vitórias do Inter.
- O número de vitórias do Grêmio.
- O número de Empates.
- Uma mensagem indicando qual o time que venceu o maior número de GRENAIS (ou "Nao houve vencedor", caso termine empatado).

Entrada
O arquivo de entrada contém 2 valores inteiros, correspondentes aos gols marcados pelo Inter e pelo Grêmio respectivamente. 
Em seguida háverá um inteiro (1 ou 2), correspondente à repetição do programa.

Saída
Após cada leitura dos gols, deve ser impressa a mensagem "Novo grenal (1-sim 2-nao)". 
Quando o algoritmo for encerrado devem ser mostradas as estatísticas conforme a descrição apresentada acima. Obs: a palavra "Gremio" deve ser impressa sem acento, conforme o exemplo abaixo.
'''


inter, gremio, empate, count = 0,0,0,1

while True:
    ent = input()
    entradas = ent.split()
    lista = [int(x) for x in entradas]
    
    if lista[0] == lista[1]:
        empate += 1
    elif lista [0] > lista[1]:
        inter += 1
    else:
        gremio += 1

    print('Novo grenal (1-sim 2-nao)')
    resp = int(input())
    if resp == 1:
        count += 1
        continue
    elif resp == 2:
        break

print(f'{count} grenais\nInter:{inter}\nGremio:{gremio}\nEmpates:{empate}')

casos = [inter, gremio, empate]

if max(casos) == inter:
    print('Inter venceu mais')
elif max(casos) == gremio:
    print('Gremio venceu mais')
elif max(casos) == empate:
    print('Nao houve vencedor')

