# Exercício 03
# Faça um programa que leia 5 números reais e calcule a média ponderada desses números, usando apenas duas variáveis.

# Entrada:
# A entrada contém cinco números reais: x1 , x2 , x3 , x4 e x5.
# Saı́da
# Calcule e imprima a média m (com 3 casas decimais) usando a fórmula:
# m=(1x1 + 2x2 + 3x3 + 4x4 + 5x5)/15

number1 = float(input())
number2 = float(input())
number3 = float(input())
number4 = float(input())
number5 = float(input())

result = (1*number1 + 2*number2 + 3*number3 + 4*number4 + 5*number5)/15

print("%.3f" % result)
