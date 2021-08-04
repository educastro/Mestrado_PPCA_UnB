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





