# Usando uma função, faça um programa que leia 10 números inteiros e imprima na tela o maior deles. No caso de valores iguais, imprima qualquer um dos maiores. Caso o maior número seja múltiplo do primeiro número n lido, imprima n na tela.
# Entrada
# Dez números inteiros, considere que o primeiro número lido nunca será 0.
# Saída
# O maior número m e o primeiro número n lido, caso m=a⋅n,a∈Z.

# Input: 3
# Input: 1
# Input: 2
# Input: 3
# Input: 4
# Input: 5
# Input: 6
# Input: 7
# Input: 8
# Input: 9
# Output: 9
# Output: 3

# Input: -1
# Input: -5
# Input: -4
# Input: 10
# Input: 8
# Input: 0
# Input: 4
# Input: 3
# Input: 2
# Input: 1
# Outpupt: 10
# Output: -1

# Input: -2
# Input: -4
# Input: -8
# Input: -16
# Input: -32
# Input: -64
# Input: -128
# Input: -256
# Input: -512
# Input: -2
# Output: -2
# Output: -2

def check_number(list_of_numbers):
    biggest_number = -9223372036854775807
    for element in list_of_numbers:
        if element > biggest_number:
            biggest_number = element
    return biggest_number

should_i_continue = True
list_of_numbers = []

while should_i_continue:
    first_entry = int(input())

    if first_entry == 0:
        should_i_continue = True
    else:
        should_i_continue = False

list_of_numbers.append(first_entry)

for iterator in range(9):
    entry = int(input())
    list_of_numbers.append(entry)

print(check_number(list_of_numbers))

if check_number(list_of_numbers) % list_of_numbers[0] == 0:
    print(list_of_numbers[0])





