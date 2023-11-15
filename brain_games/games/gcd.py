from math import gcd
from random import randint


def game_data():
    print("Find the greatest common divisor of given numbers.")

    first_num = randint(1, 100)
    second_num = randint(1, 100)

    expression = f'{first_num} {second_num}'

    right_answer = str(gcd(first_num, second_num))

    return expression, right_answer
