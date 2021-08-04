# Leia um valor inteiro N que lê a quantidade de casos de teste que vem a seguir. Cada caso de teste consiste de dois inteiros X e Y. Você deve apresentar a soma de Y ímpares consecutivos a partir de X, inclusive o próprio X se ele for ímpar. Por exemplo: para a entrada 4 5, a saída deve ser 45, que é equivalente a: 5 + 7 + 9 + 11 + 13, para a entrada 7 4, a saída deve ser 40, que é equivalente a: 7 + 9 + 11 + 13. No nal imprima também a maior e a menor soma, e a média destas duas últimas somas.

# Entrada:
# A primeira linha de entrada é um inteiro N > 0 que é a quantidade de casos de teste que vem a seguir. Cada caso de teste consiste em uma linha contendo dois inteiros X e Y, onde Y > 0.
# Saída:
# Imprima a soma S dos Y consecutivos números ímpares a partir do valor X, para cada X e Y lidos. Imprima também a maior e a menor soma S. No final, imprima a média da maior e da menor soma com duas casas decimais após a vírgula, conforme exemplo abaixo.

# Input: 4
# Input: -2 5
# Input: 3 3
# Input: -10 3
# Input: 4 4
# Output: 15
# Output: 15
# Output: -21
# Output: 32
# Output: 32
# Output: -21
# Output: 5.50

# Input: 3
# Input: -5 1
# Input: -3 1
# Input: -10 3
# Output: -5
# Output: -4
# Output: -21
# Output: -4
# Output: -21
# Output: -12.50

# Input: 2
# Input: -5 2
# Input: -5 4
# Output: -8
# Output: -8
# Output: -8
# Output: -8
# Output: -8.00

somatory = []
number_of_cases = int(input())

for iterator in range(number_of_cases):
    somatory.append(0)

for iterator in range(number_of_cases):
    base_number, occurrence_number = input().split()
    
    base_number = int(base_number)
    occurrence_number = int(occurrence_number)

    somatory[iterator] = 0

    if base_number % 2 == 0:
        base_number = base_number + 1
    
    for iterator2 in range(occurrence_number):
        somatory[iterator] += base_number
        base_number += 2
    
    print(somatory[iterator])

biggest_number = -9223372036854775807
smallest_number = 9223372036854775807
average_sum = 0

for element in somatory:
    if element > biggest_number:
        biggest_number = element
    if element < smallest_number:
        smallest_number = element

average_sum = (biggest_number + smallest_number)/2

print(biggest_number)
print(smallest_number)
print("%.2f" % average_sum)
            




