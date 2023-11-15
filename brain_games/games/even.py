from random import randint


def game_data():
    print('Answer "yes" if the number is even, otherwise answer "no".')

    expression = randint(1, 100)
    right_answer = 'yes' if expression % 2 == 0 else 'no'

    return expression, right_answer
