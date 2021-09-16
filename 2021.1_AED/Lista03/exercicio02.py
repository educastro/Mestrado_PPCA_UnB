# Um grupo de alunos da disciplina Estrutura de Dados, experts em grafos, resolveu abrir uma startup para armazenamento e distribuição de produtos comprados pela Internet. O objetivo deles é colocar pontos de distribuição em cidades de tal forma que os moradores de qualquer cidade fiquem distantes do ponto de distribuição apenas a uma aresta de distância. Para diminuir os custos eles querem minimizar a quantidade de pontos de distribuição.
#
# Entrada: Uma lista de adjacências de um grafo não dirigido, com a comprimento em Km de cada aresta. A lista termina quando aparece uma distância negativa.
#
# Saída: A quantidade de pontos de distribuição em uma linha e na outra as cidades onde estão os mesmos, em ordem alfabética. Se houver mais de uma solução, colocar a solução com a menor ordem lexicográfica das cidades.
#
# For example:
#
# Input
# A B 1
# A E 2
# A D 3
# B C 4
# B E 5
# C D 6
# C E 7
# D E 8
# X X -1
# Output: 1
# Output: E
#
# Input:
# A B 1
# A F 2
# A E 3
# B C 4
# B F 5
# B I 6
# B G 7
# C D 8
# C F 9
# C I 10
# D E 12
# D F 13
# E F 14
# G I 16
# A A -1
# Output: 2
# Output: B
# Output: D

from itertools import permutations

grafo = {}

a1, a2, distancia = input().split()

distancia = int(distancia)

while distancia > 0:
    grafo[(a1, a2)] = distancia
    a1, a2, distancia = input().split()
    distancia = int(distancia)

vertices = []

for iterador in grafo.keys():
    if iterador[0] not in vertices:
        vertices.append(iterador[0])
    if iterador[1] not in vertices:
        vertices.append(iterador[1])

vertices.sort()

armazem_aux = len(vertices)
armazem = []
cidades = []

for iterador in range(0, len(grafo)):
    for recorte in permutations(vertices, iterador):
        for iterador2 in recorte:
            if iterador2 not in cidades:
                cidades.append(iterador2)
            for iterador3 in vertices:
                a1=grafo.get((iterador2, iterador3), False)
                if  a1!=False:
                    if iterador3 not in cidades:
                        cidades.append(iterador3)
                a1=grafo.get((iterador3, iterador2), False)
                if  a1!=False:
                    if iterador3 not in cidades:
                        cidades.append(iterador3)
        cidades.sort()

        def testa(cidades_tamanho, vertices):
            cidades_tamanho = len(cidades)
            vertices_tamanho = len(vertices)
            if cidades_tamanho == vertices_tamanho:
                for iterador5 in range(cidades_tamanho):
                    if cidades[iterador5] != vertices[iterador5]:
                        return False
                return True
            return False

        if testa(cidades, vertices):
            if iterador < armazem_aux:
                armazem_aux = iterador
                armazem = recorte

        cidades = []

print(armazem_aux)

for iterador4 in armazem:
    print(iterador4)
