from random import randint
import prompt


def even_():
    print("Welcome to the Brain Games!")
    name = prompt.string("May I have your name? ")
    print(f"Hello, {name}!")

    print('Answer "yes" if the number is even, otherwise answer "no".')
    correct_answer_count = 3
    correct_answer_user = 0

    while correct_answer_count > correct_answer_user:

        random_num = randint(1, 100)
        right_answer = 'yes' if random_num % 2 == 0 else 'no'
        print(f"Question: {random_num}")
        answer = prompt.string("Your answer: ")

        if random_num % 2 == 0 and answer == 'yes':
            print('Correct!')
            correct_answer_user += 1
        elif random_num % 2 != 0 and answer == 'no':
            print('Correct!')
            correct_answer_user += 1
        else:
            print(f"'{answer}' is wrong answer ;(. Correct "
                  f"answer was {right_answer}.\n Let's try again, {name}")
            break

    if correct_answer_user == 3:
        print(f"Congratulations, {name}")
