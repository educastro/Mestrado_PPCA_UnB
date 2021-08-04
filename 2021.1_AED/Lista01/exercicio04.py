# Leia quatro valores correspondentes aos eixos x e y de dois pontos quaisquer no plano:
# (x 1 , y 1 ) e (x 2 , y 2 ) e calcule a distância entre eles, mostrando 4 casas decimais após a vı́rgula, segundo a fórmula:
# Distancia = ((x2 − x1 )2 + (y2 − y1 )2)1/2

# Python possui complex como tipo de dados. Um número complexo tem um componente real e imaginário, ambos representados pelo tipo float em Python (é possı́vel acessá-los separadamente). Leia também um número complexo z = a + bj e calcule seu módulo |z| (distância até a origem), mostrando 4 casas decimais após a vı́rgula, usando a fórmula:
# |z| = ((a 2 + b 2 ))1/2

# Entrada:
# A entrada contém três linhas de dados. A primeira linha contém dois valores de ponto flutuante x1 e y1 , a segunda também contém dois valores de ponto flutuante x2 e y2 e a terceira contém um número complexo.
# Saı́da:
# Calcule e imprima o valor da distância e do módulo segundo as fórmulas fornecidas, com 4 casas decimais.

# Nota:
# Para ler vários valores em uma mesma linha, use input().split(). Se o argumento de split for vazio, o separador das variáveis é um espaço em branco. Porém, lembre-se que input lê apenas strings do teclado, portanto você deverá converter as strings em floats.
# No exemplo a seguir, o usuário digita valores separados por um espaço em branco e aperta enter para enviá-los, então, o programa lê esses valores separados por espaços como strings (na ordem em que aparecem), guardados nas variáveis correspondentes e os converte para floats:
# A, B, C = input().split()
# A, B, C = [float(A), float(B), float(C)]

# Input: 1.0 7.0
# Input: 5.0 9.0
# Input: 2j
# Output: 4.4721
# Output: 2.0000

# Input: -2.5 0.4
# Input: 12.1 7.3
# Input: 1+2j
# Output: 16.1484
# Output: 2.2361

x1, y1 = input().split()
x2, y2 = input().split()
imaginario = input().split("+")

x1 = float(x1)
x2 = float(x2)

y1 = float(y1)
y2 = float(y2)

distancia = (((x2-x1)**2) + ((y2-y1)**2))**0.5

if len(imaginario) == 1:
    imaginario1 = float(imaginario[0].replace("j", ""))
    z = (imaginario1**2)**0.5
else:
    imaginario1 = float(imaginario[0].replace("j", ""))
    imaginario2 = float(imaginario[1].replace("j", ""))
    z = ((imaginario1**2) + (imaginario2**2))**0.5

print("%.4f" % distancia)
print("%.4f" % z)
