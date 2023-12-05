from random import randint

DESCRIPTION = "What number is missing in the progression?"


def get_question_and_answer():
    start = randint(0, 50)
    step = randint(2, 6)
    length = randint(5, 10)
    end = start + length * step

    progression = list(range(start, end, step))

    hidden_num = randint(0, length - 1)
    right_answer, progression[hidden_num] = progression[hidden_num], '..'
    expression = ' '.join(str(i) for i in progression)

    return expression, str(right_answer)
