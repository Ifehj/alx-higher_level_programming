#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)

last_digit = abs(number) % 10
greater = "and is greater than 5"
middle = "and is 0"
lesser = "and is less than 6 and not 0"

if number < 0:
    last_digit = -last_digit

if last_digit > 5:
    print("Last digit of {} is {} {}".format(number, last_digit, greater))

elif last_digit == 0:
    print("Last digit of {} is {} {}".format(number, last_digit, middle))

else:
    print("Last digit of {} is {} {}".format(number, last_digit, lesser))
