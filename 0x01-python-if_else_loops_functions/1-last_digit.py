#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
if number >= 0:
    lst_dgt = number % 10
else:
    lst_dgt = ((-number % 10) * -1)

message = f"Last digit of {number} is {lst_dgt}"

if lst_dgt == 0:
    print(f"{message} and is 0")
elif lst_dgt > 5 and lst_dgt % 10 != 0:
    print(f"{message} and is greater than 5")
else:
    print(f"{message} and is less than 6 and not 0")
