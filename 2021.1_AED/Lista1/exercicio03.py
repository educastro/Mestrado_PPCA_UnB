# Exercício 03
# Faça um programa que leia 5 números reais e calcule a média ponderada desses números, usando apenas duas variáveis.

# Entrada:
# A entrada contém cinco números reais: x1 , x2 , x3 , x4 e x5.
# Saı́da
# Calcule e imprima a média m (com 3 casas decimais) usando a fórmula:
# m=(1x1 + 2x2 + 3x3 + 4x4 + 5x5)/15

numero1 = float(input())
numero2 = float(input())
numero3 = float(input())
numero4 = float(input())
numero5 = float(input())

resultado = (1*numero1 + 2*numero2 + 3*numero3 + 4*numero4 + 5*numero5)/15

print("%.3f" % resultado)
