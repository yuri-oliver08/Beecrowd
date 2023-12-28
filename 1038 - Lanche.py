'''
Com base na tabela abaixo, escreva um programa que leia o código de um item e a quantidade deste item. 
A seguir, calcule e mostre o valor da conta a pagar.


Entrada
O arquivo de entrada contém dois valores inteiros correspondentes ao código e à quantidade de um item conforme tabela acima.

Saída
O arquivo de saída deve conter a mensagem "Total: R$ " seguido pelo valor a ser pago, com 2 casas após o ponto decimal.
'''

input1 = input()

prod = input1.split()

code = int(prod[0])

produtos = {
    1: {
        "nome": "Cachorro Quente",
        "preco": 4.00
    },
    2: {
        "nome": "X-Salada",
        "preco": 4.50
    },
    3: {
        "nome": "X-Bacon",
        "preco": 5.00
    },
    4: {
        "nome": "Torrada simples",
        "preco": 2.00
    },
    5: {
        "nome": "Refrigerante",
        "preco": 1.50
    },
}

produto = produtos.get(code)

calc = produto["preco"] * int(prod[1])

print(f'Total: R$ {calc:.2f}')
