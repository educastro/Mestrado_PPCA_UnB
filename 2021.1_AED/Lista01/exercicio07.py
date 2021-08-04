# Escreva uma função compare que dado dois números x e y, retorne 1 se x for maior que y, 0 se for igual a y, e -1 se x for menor que y. Usando o retorno da função, imprima na tela: "x e maior que y" se o retorno for 1, "x e igual a y" se o retorno for 0, e "x e menor que y", caso contrário.
# Entrada
# Duas linhas de entrada correspondentes aos inteiros x e y.
# Saída
# Será impresso na tela a mensagem "x e maior que y" se o retorno da função for 1, "x e igual a y" se o retorno da função for 0, e "x e menor que y", caso contrário.

# Input: 4
# Input: 5
# Output: x e menor que y

# Input: 3
# Input: 3
# Output: x e igual a y

# Input: -1
# Input: -2
# Output: x e maior que y

def compare(x,y):
    if x > y:
        return 1
    elif x == y:
        return 0
    else:
        return -1

x = float(input())
y = float(input())

if compare(x,y) == 1:
    print("x e maior que y")
elif compare(x,y) == -1:
    print("x e menor que y")
else:
    print("x e igual a y")


