'''
Pedrinho está organizando um evento em sua Universidade. O evento deverá ser no mês de Abril, iniciando e terminando dentro do mês. 
O problema é que Pedrinho quer calcular o tempo que o evento vai durar, uma vez que ele sabe quando inicia e quando termina o evento.

Sabendo que o evento pode durar de poucos segundos a vários dias, você deverá ajudar Pedrinho a calcular a duração deste evento.

Entrada
Como entrada, na primeira linha vai haver a descrição “Dia”, seguido de um espaço e o dia do mês no qual o evento vai começar. 
Na linha seguinte, será informado o momento no qual o evento vai iniciar, no formato hh : mm : ss. 
Na terceira e quarta linha de entrada haverá outra informação no mesmo formato das duas primeiras linhas, indicando o término do evento.

Saída
Na saída, deve ser apresentada a duração do evento, no seguinte formato:

W dia(s)
X hora(s)
Y minuto(s)
Z segundo(s)

Obs: Considere que o evento do caso de teste para o problema tem duração mínima de 1 minuto.
'''

from datetime import datetime

#Entrada
diaI = input()
horaI = input()
diaF = input()
horaF = input()

#Juntando os horários no dia específico
inicio = f'{diaI} {horaI}'
fim = f'{diaF} {horaF}'

#Conversão das strings para datetime objects
timestampI = datetime.strptime(inicio,'Dia %d %H : %M : %S')
timestampF = datetime.strptime(fim,'Dia %d %H : %M : %S')

horaI = timestampI.time().hour
minutoI = timestampI.time().minute
horaF = timestampF.time().hour
minutoF = timestampF.time().minute
diaI = int(timestampI.day)
diaF = int(timestampF.day)

diferencaMinutos = minutoF - minutoI
diferencaHoras = horaF - horaI


#Calculando a diferença 
difference = timestampF - timestampI

days = difference.days
hours, remainder = divmod(difference.seconds, 3600)
minutes, seconds = divmod(remainder, 60)

#Saída
print(f'{days} dia(s)\n{hours} hora(s)\n{minutes} minuto(s)\n{seconds} segundo(s)')