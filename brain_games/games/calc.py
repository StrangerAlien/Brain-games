import random
from random import randint


def game_data():
    print("What is the result of the expression?")

    sign = ['+', '-', '*']

    expression = f'{randint(0, 10)} {random.choice(sign)} {randint(0, 10)}'

    right_answer = str(eval(expression))

    return expression, right_answer
