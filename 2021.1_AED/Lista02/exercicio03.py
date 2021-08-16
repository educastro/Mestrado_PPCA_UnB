class Pilha :
    def __init__(self):
        self.lista = []

    def push(self, item) :
        self.lista.append(item)
    def pop(self) :
        return self.lista.pop()
    def tamanho(self):
        return len(self.lista)
    def estaVazio(self):
        if self.tamanho() == 0 :
            return True
        else :
            return False

def verificaParanteses(string) :
    pilha = Pilha()
    for elemento in string :
        if elemento == '(' :
            pilha.push('(')
        if elemento == ')' :
            if pilha.estaVazio() :
                return False
            pilha.pop()

    return pilha.estaVazio()

string = input()
print(verificaParanteses(string))
