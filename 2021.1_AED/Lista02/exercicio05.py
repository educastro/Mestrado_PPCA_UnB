class Stack :
    def __init__(self):
        self.list = []

    def push(self, item) :
        self.list.append(item)
    def pop(self) :
        return self.list.pop()
    def size(self):
        return len(self.list)
    def isEmpty(self):
        if self.size() == 0 :
            return True
        else :
            return False

def verificador(string) :
    pilha = Stack()

    for a in string :
        if a == "(" or a == "[" or a == "{":
            pilha.push(a)
        else:
            if pilha.isEmpty():
                return False

            b = pilha.pop()

            if a == ")":
                if b != "(":
                    return False
            if a == "]":
                if b != "[":
                    return False
            if a == "}":
                if b != "{":
                    return False


    return pilha.isEmpty()

string = input()
print(verificador(string))
