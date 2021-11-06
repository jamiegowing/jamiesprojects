import random


number = random.randint(1, 90)
bingo = random.randint(1, 90)
if number == bingo:
    print("true")
else:
    print("false")