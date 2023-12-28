'''
Neste problema, você deverá ler 3 palavras que definem o tipo de animal possível.
Em seguida conclua qual dos animais seguintes foi escolhido, através das três palavras fornecidas.


Entrada
A entrada contém 3 palavras, uma em cada linha, necessárias para identificar o animal segundo a figura acima, com todas as letras minúsculas.

Saída
Imprima o nome do animal correspondente à entrada fornecida.
'''

ent1 = input()
ent2 = input()
ent3 = input()

animais = {
    'vertebrado':{
        'ave':{
            'carnivoro':{
                'animal':'aguia'
            },
            'onivoro':{
                'animal':'pomba'
            }
        },
        'mamifero':{
            'onivoro':{
                'animal':'homem'
            },
            'herbivoro':{
                'animal':'vaca'
            }
        }
    },
    'invertebrado':{
        'inseto':{
            'hematofago':{
                'animal':'pulga'
            },
            'herbivoro':{
                'animal':'lagarta'
            }
        },
        'anelideo':{
            'hematofago':{
                'animal':'sanguessuga'
            },
            'onivoro':{
                'animal':'minhoca'
            }
        }
    }
}

resultado = animais[ent1][ent2][ent3].get('animal')
print(resultado)