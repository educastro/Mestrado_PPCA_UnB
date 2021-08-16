def fibonnaci(number_of_iterations):
    fibonnaci_list = [0,1,1]

    for iterator in range(3,number_of_iterations+1):
        fibonnaci_list.append(fibonnaci_list[iterator-1]+fibonnaci_list[iterator-2])

    return fibonnaci_list

def factorial(number_of_iterations):
    factorial = 1

    while number_of_iterations > 0:
        factorial = factorial * number_of_iterations
        number_of_iterations -= 1
    
    return factorial

number_of_months = int(input())

number_of_couples = fibonnaci(number_of_months)[-1]

if number_of_couples % 2 == 0:
    print(str(number_of_couples) + " " + str(factorial(number_of_months)) + " " + str(fibonnaci(number_of_months+1)[-1]-fibonnaci(number_of_months)[-1]))
else:
    print(str(number_of_couples) + " " + str(factorial(number_of_months)))





    
# while number_of_months >= f3:
#     f3 = f2 + f1
#     f1 = f2
#     f2 = f3

# print(f3)