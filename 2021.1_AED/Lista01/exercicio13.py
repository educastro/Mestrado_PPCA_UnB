number = int(input())

found = False

while found == False:
    number_guessed = int(input())
    
    if number_guessed > number:
        print("O número correto é menor.")
    elif number_guessed < number:
        print("O número correto é maior.")
    else:
        print("Parabéns! Você acertou.")
        found = True