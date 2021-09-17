# sequencia_1 = "CAGGGTAGTC"#input()
# sequencia_2 = "TCATATC"#input()

sequencia_1 = input()
sequencia_2 = input()

tamanho_sequencia_2 = len(sequencia_2)
tamanho_sequencia_1 = len(sequencia_1)

sequencia = []

for iterador in range(0,tamanho_sequencia_1):
    sequencia.append(-1)

sequencia.append(0)

combinacao = []

for iterador in range(0,tamanho_sequencia_2):
    combinacao.append(sequencia[0:len(sequencia)])

sequencia = []

for iterador in range(0,tamanho_sequencia_1+1):
    sequencia.append(0)

combinacao.append(sequencia)

for iterador1 in range(tamanho_sequencia_2-1, -1, -1):
    for iterador2 in range(tamanho_sequencia_1-1, -1, -1):
        if sequencia_1[iterador2]==sequencia_2[iterador1]:
            combinacao[iterador1][iterador2] = 1 + combinacao[iterador1+1][iterador2+1]
        else:
            combinacao[iterador1][iterador2] = max(combinacao[iterador1+1][iterador2], combinacao[iterador1][iterador2+1])

maior_sequencia = ""

contador1 = 0
contador2 = 0

while ((contador1<tamanho_sequencia_2) and (contador2<tamanho_sequencia_1)):
    if sequencia_1[contador2]==sequencia_2[contador1]:
        maior_sequencia = maior_sequencia + sequencia_1[contador2]
        contador1 = contador1+1
        contador2 = contador2+1

    elif combinacao[contador1+1][contador2] >= combinacao[contador1][contador2+1]:
        contador1 += 1

    else:
        contador2 += 1

print(maior_sequencia)
