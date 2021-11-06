import random
number1 = random.randint(1, 9999)
number2 = random.randint(1, 9999)
if number1 != number2:
    if number1 < number2:
        print(number1, "<", number2)
    else:
        print(number1, ">", number2)
else:
    print(number1, "=", number2)
print(number1 + number2)
print(number1 - number2)
print(number1*number2)
print(number1/number2)