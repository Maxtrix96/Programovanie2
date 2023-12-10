number = 999_999_999_989
steps = 0

#pick an integet thats greater than 0
#if it is even, divide it by 2
#if it is odd, multiply it by 3 and add 1
#eventually, ever number will end up as 1

while number != 1:
    if number % 2 == 0:
        number /= 2
        steps += 1
    elif number % 2 != 0:
        number *= 3
        number += 1
        steps += 1
    
if number == 1:
    print("It took", steps, "steps")
else:
    print("The number didn't reach 1 yet")