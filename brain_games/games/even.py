from random import randint

DESCRIPTION = 'Answer "yes" if the number is even, otherwise answer "no".'


def get_question_and_answer():

    expression = randint(1, 100)
    right_answer = 'yes' if expression % 2 == 0 else 'no'

    return expression, right_answer
