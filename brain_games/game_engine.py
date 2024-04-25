import prompt


def logic_(brain_game):
    print("\033[1;4mWelcome to the Brain Games!")
    name = prompt.string("May I have your name? ")
    print(f"Hello, {name}!")

    game_rounds_count = 3
    for _ in range(game_rounds_count):

        expression, right_answer = brain_game.get_question_and_answer()
        print(brain_game.DESCRIPTION)

        print(f"Question: {expression}")
        answer = prompt.string("Your answer: ")

        if answer == right_answer:
            print('Correct!')
        else:
            print(f"'{answer}' is wrong answer ;(. Correct "
                  f"answer was '{right_answer}'.\n Let's try again, {name}!")
            return

    print(f"Congratulations, {name}!")
