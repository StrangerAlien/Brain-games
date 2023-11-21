import prompt


def logic_(brain_game):
    print("Welcome to the Brain Games!")
    name = prompt.string("May I have your name? ")
    print(f"Hello, {name}!")

    game_iter_count = 3

    for i in range(game_iter_count):
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
