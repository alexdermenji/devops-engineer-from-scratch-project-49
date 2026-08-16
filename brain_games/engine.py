import prompt

ROUNDS_COUNT = 3


def play_round(game):
    question, correct_answer = game.generate_round()
    print(f"Question: {question}")
    answer = prompt.string("Your answer: ")
    if answer == correct_answer:
        print('Correct!')
        return True
    print(
        f"'{answer}' is wrong answer ;(. "
        f"Correct answer was '{correct_answer}'."
    )
    return False


def play_game(game, name):
    for _ in range(ROUNDS_COUNT):
        if not play_round(game):
            print(f"Let's try again, {name}!")
            return
    print(f'Congratulations, {name}!')


def run(game):
    print('Welcome to the Brain Games!')
    name = prompt.string('May I have your name? ')
    print(f'Hello, {name}!')
    print(game.DESCRIPTION)
    play_game(game, name)