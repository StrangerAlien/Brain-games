from random import randint

DESCRIPTION = "What number is missing in the progression?"


def game_data():
    start = randint(0, 50)
    step = randint(2, 6)
    elements = randint(5, 10)

    progression = list(range(start, (start + elements * step), step))

    hidden_num = randint(0, elements - 1)
    right_answer, progression[hidden_num] = progression[hidden_num], '..'
    expression = ' '.join(str(i) for i in progression)

    return expression, str(right_answer), DESCRIPTION
