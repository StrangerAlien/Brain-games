from random import randint, choice
import operator

DESCRIPTION = "What is the result of the expression?"


def get_question_and_answer():
    first_num = randint(0, 10)
    second_num = randint(0, 10)

    action = {
        "+": operator.add,
        "-": operator.sub,
        "*": operator.mul
    }

    operation = choice(list(action.keys()))

    expression = f'{first_num} {operation} {second_num}'

    right_answer = str(action[operation](first_num, second_num))

    return expression, right_answer
