from random import randint, choice


def game_data():
    print("What is the result of the expression?")

    sign = ['+', '-', '*']

    expression = f'{randint(0, 10)} {choice(sign)} {randint(0, 10)}'

    right_answer = str(eval(expression))

    return expression, right_answer
