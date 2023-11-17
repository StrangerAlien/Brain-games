from random import randint


def game_data():
    print('Answer "yes" if given number is prime. Otherwise answer "no".')

    num = randint(1, 200)

    count = 0
    for i in range(2, num // 2 + 1):
        if num % i == 0:
            count = count + 1
    if count <= 0:
        right_answer = 'yes'
    else:
        right_answer = 'no'

    return str(num), right_answer
