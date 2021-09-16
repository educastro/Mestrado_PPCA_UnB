# A dieta KLX é feita para pessoas enjoadas, que não conseguem repetir a mesmo cardápio de forma seguida. Para estas pessoas, a dieta KLX oferece diversas opções de cardápio. Refeições parecidas tem um gosto parecido, ou seja a diferença de gosto entre uma e outra é pequena. Na dieta KLX a pessoa pode optar por 4, 5, 6, . . . , n cardápios. Para diminuir a chance de a pessoa enjoar, os cardápios devem ser alternados de forma que a diferença de sabor entre eles seja maximizada.
#
# Para este fim a KLX fornece uma tabela com as diferenças de sabor entre as suas opções.
#
# Por exemplo, para um cardápio com 4 opções, A, B, C e D, podemos usar a sequência A-B-C-D-A-B-C-D-..... , a sequência A-C-B-D-A-C-B-D-... ou a sequência A-B-D-C-A-B-D-C-.... O objetivo é achar a sequência menos enjoativa, ou seja, que tenha a maior diferença de sabor entre uma e outra refeição.
#
# Entrada: Um número inteiro com a quantidade de opções do cardápio e as n diferenças de opções do cardápio identificadas pelo nome das duas opções e sua diferença, uma por linha. Obviamente a diferença entre o cardápio A e B é igual a diferença  entre o cardápio B e A.
#
# Saída: A sequência de opções, começando pelo primeiro item, e os demais itens de forma que tenham um menor valor ordinal. Por exemplo, A-C-B-D e A-D-B-C na verdade são a mesma sequência, mas no sentido inverso. Coloque na saída apenas a sequência A-C-B-D  que é a sequência que alfabeticamente vem em primeiro.
#
# For example:
#
# Input
# 4
# A B 5
# A C 6
# A D 1
# B C 4
# B D 7
# C D 3
# Output: A B D C
#
# Input
# 4
# A B 1
# A C 1
# A D 1
# B C 1
# B D 1
# C D 1
# Output: A B C D

from itertools import permutations

entrada = int(input())

arestas = int((entrada * (entrada - 1 ))/2)

grafo = {}

for iterador in range(arestas):

    a1, a2, valor = input().split()

    valor = int(valor)

    grafo[(a1, a2)] = valor

vertices = []

for iterador2 in grafo.keys():
    if iterador2[0] not in vertices:
        vertices.append(iterador2[0])
    if iterador2[1] not in vertices:
        vertices.append(iterador2[1])
vertices.sort()

maximo = 0

for recorte in permutations(vertices, entrada):
    minimo = 0
    for i in range(entrada):
        if (i+1 < entrada):
            minimo = minimo + grafo.get((recorte[i], recorte[i+1]), grafo.get((recorte[i+1], recorte[i]), 0 ))
        else:
            minimo = minimo + grafo.get((recorte[i], recorte[0]), grafo.get((recorte[0], recorte[i]), 0 ))
    if minimo > maximo:
        maximo = minimo
        sequencia_maxima = recorte[:]

for iterador3 in sequencia_maxima:
    print(iterador3, end=" ")
