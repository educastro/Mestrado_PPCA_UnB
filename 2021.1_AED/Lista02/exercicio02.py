expressao_matematica = input()

lista = []

for elemento in expressao_matematica.split(' ') :
    if elemento in ['+','*'] :
        numero_1 = int(lista.pop())
        numero_2 = int(lista.pop())
        if elemento == '+' :
            lista.append(numero_1 + numero_2)
        elif elemento == '*' :
            lista.append(numero_1 * numero_2)

    elif elemento.isnumeric() :
        lista.append(int(elemento))

print (str(lista[0]))
