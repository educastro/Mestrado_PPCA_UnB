x,y = input().split()

x = int(x)
y = int(y)

found = False

if x > y:
    length_of_the_pile = y
    while found == False:
        if x % length_of_the_pile == 0 and y % length_of_the_pile == 0:
            found = True
        if found == False:
            length_of_the_pile -= 1
elif y > x:
    length_of_the_pile = x
    while found == False:
        if x % length_of_the_pile == 0 and y % length_of_the_pile == 0:
            found = True
        if found == False:
            length_of_the_pile -= 1
else:
    length_of_the_pile = y

print(length_of_the_pile)

