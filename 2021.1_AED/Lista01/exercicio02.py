# Exercício 02
# Faça um programa que peça ao usuário para informar dois números reais, conforme especiﬁcado em Entrada. Depois calcule a média desses números e mostre-a na tela, conforme especiﬁcado em Saída.

# Entrada:
# Leia 2 números reais do teclado, um por linha.
# Saída:
# Imprima na tela media, onde media é um real com duas casas decimais que representa a média dos dois reais lidos do teclado

# Input: 4
# Input: 4
# Output: 4.00

# Input: 0
# Input: 1
# Output: 0.50

# Input: 9.525
# Input: 4.2
# Output: 6.86

number1 = float(input())
number2 = float(input())

average = (number1+number2)/2

print("%.2f" % average)
