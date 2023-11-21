from random import randint, choice
import operator


def game_data():
    print("What is the result of the expression?")

    num1 = randint(0, 10)
    num2 = randint(0, 10)

    action = {
        "+": operator.add,
        "-": operator.sub,
        "*": operator.mul
    }

    operation = choice(list(action.keys()))

    expression = f'{num1} {operation} {num2}'

    right_answer = str(action[operation](num1, num2))

    return expression, right_answer
