from random import randint


def game_data():
    print("What number is missing in the progression?")

    start_num = randint(0, 50)
    step_num = randint(2, 6)
    qty_elem = randint(5, 10)

    progression = []

    for i in range(qty_elem):
        progression.append(start_num + i * step_num)

    hidden_num = randint(0, qty_elem - 1)
    right_answer = str(progression[hidden_num])

    progression[hidden_num] = '..'
    expression = (' '.join(str(i) for i in progression))

    return expression, right_answer
