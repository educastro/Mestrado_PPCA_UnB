number = int(input())

for iterator in range(1,number+1):
    if number % iterator == 0:
        print(iterator)