import prompt
from brain_games.cli import welcome_user


def logic_(brain_game):
    correct_answer_count = 3
    correct_answer_user = 0

    name = welcome_user()

    while correct_answer_count > correct_answer_user:
        expression, right_answer = brain_game.game_data()

        print(f"Question: {expression}")
        answer = prompt.string("Your answer: ")

        if answer == right_answer:
            print('Correct!')
            correct_answer_user += 1
        else:
            print(f"'{answer}' is wrong answer ;(. Correct "
                  f"answer was '{right_answer}'.\n Let's try again, {name}!")
            break

    if correct_answer_user == 3:
        print(f"Congratulations, {name}!")
