def concat(s1, s2):
    if not s1:
        return s2
    else:
        return s1[0:1] + concat(s1[1:], s2)
    
""" Para o primeiro  if vamos testar se a string s1 não é vazia.
No else, temos que s1[0:1] pega o primeiro elemento da string
e s1[1:] pega o resto (operação de fatiar) """

s1 = input()
s2 = input()

print(concat(s1,s2))

""" Função recursiva para length: 
def length(s):
    if not s: (s = nil)
        return 0
    else:
        return 1 + length(s[1:]
Tente fazer função recursiva para mdc, fibonacci e fatorial!
"""
print(s1[::-1])
print(s2.startswith(s1))

        
