quantidade_valores = int(input())

tipos_de_moedas = input().split()

for i in range(quantidade_valores):
    tipos_de_moedas[i] = float(tipos_de_moedas[i])
    tipos_de_moedas[i] = int(tipos_de_moedas[i] * 100)

nota_entrada, valor_da_compra = input().split()

nota_entrada = float(nota_entrada)
valor_da_compra = float(valor_da_compra)

valor_do_troco = nota_entrada - valor_da_compra
valor_do_troco = int(valor_do_troco * 100)

moedas_minimo = [0] * 100
moedas_usadas = [0] * 100

for valor_cent in range(valor_do_troco + 1):
    contador = valor_cent
    moedaN = 1

    for iterador in [i for i in tipos_de_moedas if i <= valor_cent]:
        if moedas_minimo[valor_cent - iterador] + 1 < contador:
            contador = moedas_minimo[valor_cent - iterador] + 1
            moedaN = iterador

    moedas_minimo[valor_cent] = contador
    moedas_usadas[valor_cent] = moedaN

moeda = valor_do_troco

while moeda > 0:
    moedat = moedas_usadas[moeda]

    print("%.2f" % (moedat / 100))

    moeda = moeda - moedat
