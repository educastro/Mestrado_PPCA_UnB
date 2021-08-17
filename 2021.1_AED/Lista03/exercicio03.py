# A Galáxia está em perigo! O Império Galáctico iniciou uma ofensiva para acabar de vez com a República. Diversas frentes de batalha espalhadas pela Galáxia pretendem eliminar o que resta da oposição. Sua missão é montar um simulador que teste você, jovem Padwan, em diversos tipos de missão de forma que consiga usar a Força contra o Império nas diversas frentes de batalha.
#
# São 3 as missões de treinamento Padwan descritas a seguir:
#
# Reconhecimento:  a inteligência rebelde irá passar um mapa convencional em coordenadas cartesianas de sistemas estelares de uma região desconhecida da galáxia que podem ser verdadeiros ou não. Os espiões rebeldes também conseguiram informações de possíveis caminhos de minhoca (wormhole) que ligam estes sistemas e seu comprimento. Esta informação é passada como um grafo representado por meio de lista de adjacência. O comprimento de um caminho de minhoca entre dois sistemas estelares pode ser muito mais curto que as distâncias no espaço tridimensional clássico. O espaço tridimensional clássico da galáxia GFFA (Galaxy Far Far Away, alguns acreditam que ela seja a NGC 224), tem como origem o buraco negro no centro da galáxia. A galáxia GFFA tem formato de espiral. O plano XY contém a espiral, sendo o eixo X alinhado com o eixo maior do disco, e o sentido do eixo Z é dextrógiro (vide regra de Flemming para se estabelecer um sistema de coordenadas tridimensional ortogonal padrão). As distâncias intra-galáxias são medidas em parsecs.
#
# O grafo com os caminhos de minhoca da região desconhecida não é conexo. Cada subgrafo forma uma grupo de sistemas estelares conectada por caminhos de minhoca conexo. Sua missão de reconhecimento tem como objetivo identificar estes grupos e gerar um grafo conexo completo que ligue estes grupos/subgrafos pela adição de uma ou mais rotas mais curtas no espaço cartesiano ligando dois ou mais sistemas estelares pertencentes a estes grupos/subgrafos. Diga quais são as rotas mais curtas que precisam ser adicionadas para interligar os grupos/subgrafos para toná-lo um grafo completo, colocando o par início, destino em ordem alfabética, e os pares também em ordem alfabética.
#
# Para isto a inteligência rebelde fornecerá mapas de alguma região da galáxia, com a localização dos sistemas estelares em coordenadas cartesianas e um grafo onde os vértices são os sistemas estelares e as arestas são caminhos no hiperespaço (caminhos de minhoca) que interligam os sistemas estelares.
#
# Logística: Você tem a missão de reabastecer as bases rebeldes com uma nave cargueiro. Você deve partir da primeira base rebelde e retornar a ela passando em todas as bases rebeldes uma só vez sem repetir os caminhos de minhoca.  A inteligência rebelde te passou um mapa com todos os caminhos de minhocas conhecidos entre as bases. Estude o mapa e diga ao seu mestre qual o tamanho do percurso total da viagem, se ela for possível. Caso não seja possível, diga a ele que é Impossível. Cada caminho de minhoca tem no máximo 9 u.a. e o número de sistemas estelares a ser reabastecido é menor que 100.
#
# Ataque: A inteligência vai te passar uma árvore de decisão em uma estrutura linear. Dependendo do alvo e das condições ambientais você pode usar diferentes tipos de armas ou diferentes combinações delas para cumprir a sua missão. Para cada alvo você receberá as informações necessárias para decidir com o que atingirá o objetivo.  Por exemplo, se o alvo puder ser um caça ou helicóptero do império ele usará um míssil para abater um caça blindado, um laser para um caça não blindado, um canhão para o helicóptero blindado e uma metralhadora para um helicóptero não blindado, de acordo com a seguinte árvore binária de decisão.
#
# (? (caça  (blindado (míssil)) (não (laser)) (helicóptero (blindado (canhão)) (não (metralhadora))))
#
# A inteligência repassa esta informação em uma estrutura linear parecida com uma estrutura de heap binária:
#
# ? caça  helicóptero blindado não blindado não míssil laser canhão metralhadora
#
# -----------------------------------------------------------------------------------------------------------------------------
#
# Entrada:
#
# Uma linha com um símbolo indicando o tipo da missão. A missão pode ser de:
#
# R - reconhecimento;
# L - logística; e
# A - ataque.
# Seguidas de várias linhas com as informações conseguidas pela inteligência.
#
# Descrição da tarefa em cada missão.
#
# Exemplo de entrada para a missão de reconhecimento (R):
#
# R
#
# 4
#
# A 999,10,8
#
# B 1005,50,-20
#
# C 955,-25,15
#
# D 1019,-20,-7
#
# A B,1
#
# B
#
# C D,1
#
#
# D
#
# -------------------------------------------------------------------------------
#
# Saída da missão de reconhecimento:
#
# Caminhos euclidianos a serem acrescentados em ordem alfabética ou a frase "Não precisa novos caminhos".
#
# Exemplo de saída para a missão de reconhecimento (R):
#
# A - D
#
# --------------------------------------------------------------------------------------------
#
# Exemplo de entrada para a missão de Logística (L):
#
# L
#
# 3
#
# A B,3 C,4
#
# B A,3 C,5
#
# C A,4 B, 5
#
# Exemplo de entrada para a missão de Logística (L):
#
# 12
#
# -----------------------------------------------------------------------------------------------------------------------
#
# Exemplo para a missão de Ataque (A):
#
# Entrada:
#
# A
#
# ? caça helicóptero blindado não blindado não míssil laser canhão metralhadora
#
# caça blindado
#
# caça não
#
# helicóptero blindado
#
# helicóptero não
#
#
#
# Exemplo de saída para a missão de ataque:
#
# míssil
#
# laser
#
# canhão
#
# metralhadora
#
#
#
# For example:
#
# Input
# R
# 5
# A 999,10,8
# B 1005,50,-20
# C 955,-25,15
# D 1019,-20,-7
# E 1009,20,7
# A B,1
# B A,1
# C D,1
# D C,1
# E
# Output: A-D
# Output: A-E
# Output: D-E

# Input
# R
# 4
# A 999,10,8
# B 1005,50,-20
# C 955,-25,15
# D 1019,-20,-7
# A B,1 D,1
# B A,1
# C D,1
# D A,1 C,1
# Output: Não precisa novos caminhos

# Input
# L
# 4
# A B,1 C,2 D,3
# B A,1 C,4 D,6
# C A,2 B,4 D,5
# D A,3 B,6 C,5
# Output: 13

# Input
# L
# 4
# Aleph Centauri,2 Deneb,3
# Beta Centauri,4 Deneb,6
# Centauri Aleph,2 Beta,4 Deneb,5
# Deneb Aleph,3 Beta,6 Centauri,5
# Output: 15

# Input
# A
# ? caça não escudo não escudo não visível não visível não não visível não visível A B AB AC C CC AA BB
# caça não visível
# não não não
# caça escudo visível
# fim, missão acabou
# Output: AB
# Output: AA
# Output: A

# Input
# A
# ? caça não escudo não escudo não A B AA BB
# não não
# não escudo
# caça não
# caça escudo
# fim
# Output: BB
# Output: AA
# Output: B
# Output: A
