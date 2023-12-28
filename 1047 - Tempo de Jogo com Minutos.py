'''
Leia a hora inicial, minuto inicial, hora final e minuto final de um jogo. A seguir calcule a duração do jogo.

Obs: O jogo tem duração mínima de um (1) minuto e duração máxima de 24 horas.

Entrada
Quatro números inteiros representando a hora de início e fim do jogo.

Saída
Mostre a seguinte mensagem: “O JOGO DUROU XXX HORA(S) E YYY MINUTO(S)” .
'''

entrada = input()
valores = entrada.split()
inicio_em_minutos = int(valores[0])*60 + int(valores[1])
final_em_minutos = int(valores[2])*60 + int(valores[3])

duracao_em_minutos = final_em_minutos - inicio_em_minutos


if final_em_minutos == inicio_em_minutos:
    print('O JOGO DUROU 24 HORA(S) E 0 MINUTO(S)')
elif duracao_em_minutos > 0:
    horas = duracao_em_minutos//60
    minutos = duracao_em_minutos%60
    print(f"O JOGO DUROU {horas} HORA(S) E {minutos} MINUTO(S)")
else:
    duracao_em_minutos = (24*60 - inicio_em_minutos) + final_em_minutos
    horas = duracao_em_minutos//60
    minutos = duracao_em_minutos%60
    print(f"O JOGO DUROU {horas} HORA(S) E {minutos} MINUTO(S)")