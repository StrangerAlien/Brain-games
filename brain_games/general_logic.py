import prompt


def logic_(brain_game):
    print("Welcome to the Brain Games!")
    name = prompt.string("May I have your name? ")
    print(f"Hello, {name}!")

    for i in range(3):  # number of correct answers
        expression, right_answer = brain_game.game_data()

        print(f"Question: {expression}")
        answer = prompt.string("Your answer: ")

        if answer == right_answer:
            print('Correct!')
        else:
            print(f"'{answer}' is wrong answer ;(. Correct "
                  f"answer was '{right_answer}'.\n Let's try again, {name}!")
            return

    print(f"Congratulations, {name}!")
