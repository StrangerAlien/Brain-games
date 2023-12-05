from math import gcd
from random import randint

DESCRIPTION = "Find the greatest common divisor of given numbers."


def get_question_and_answer():
    first_num = randint(1, 100)
    second_num = randint(1, 100)

    expression = f'{first_num} {second_num}'

    right_answer = str(gcd(first_num, second_num))

    return expression, right_answer
