# Exercício 01
class Pilha :

    def __init__(self):
        self.lista = []

    def empilha(self, item) :
        self.lista.append(item)
    def desempilha(self) :
        return self.lista.pop()
    def tamanho(self):
        return len(self.lista)
    def estaVazio(self):
        if self.tamanho() == 0 :
            return True
        else :
            return False

def decimal2binario(valor_decimal) :
    p = Pilha()

    dividendo = valor_decimal
    while (True) :
        quociente = dividendo // 2
        resto = dividendo % 2
        p.empilha(resto)
        if quociente == 0 :
            break
        else :
            dividendo = quociente
    output = ""

    while (not p.estaVazio()) :
        output += str(p.desempilha())

    return output
