from brain_games.cli import welcome_user


def game_data():
    name = welcome_user()
    print(f"{name} this calc")
