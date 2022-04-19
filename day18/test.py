from random import randint

print(tuple(randint(0, 255) for color in range(3)))