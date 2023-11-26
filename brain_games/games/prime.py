from random import randint

DESCRIPTION = 'Answer "yes" if given number is prime. Otherwise answer "no".'


def game_data():
    num = randint(1, 200)
    right_answer = 'yes' if is_prime(num) else 'no'
    return str(num), right_answer, DESCRIPTION


def is_prime(num):
    count = 0
    for i in range(2, num // 2 + 1):
        if num % i == 0:
            count += 1
    if count <= 0:
        return True
    else:
        return False
