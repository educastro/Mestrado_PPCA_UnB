def fibonacci (numero) :
    lista = {}

    for elemento in range (numero+1) :
        if elemento <= 1 :
            lista[elemento] = elemento
        else :
            lista[elemento] = lista[elemento-1] + lista[elemento-2]
    return lista[numero]

elemento = int(input())
print (fibonacci(elemento))
