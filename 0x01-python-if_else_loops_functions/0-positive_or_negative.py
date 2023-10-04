#!/usr/bin/python3
import random
number = random.randint(-10, 10)
if (number < 0):
    print(f"{number} is negaitive")
elif (number > 0):
    print(f"{number} is positive")
else:
    print(f"{number} is zero")
