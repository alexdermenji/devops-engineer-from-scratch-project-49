from random import randint

import prompt

MIN_NUMBER = 0
MAX_NUMBER = 100
ROUNDS_COUNT = 3
DESCRIPTION = 'Answer "yes" if the number is even, otherwise answer "no".'


def is_even(number):
    return number % 2 == 0


def get_correct_answer(number):
    if is_even(number):
        return "yes"
    return "no"


def generate_round():
    value = randint(MIN_NUMBER, MAX_NUMBER)
    answer = get_correct_answer(value)
    return value, answer


def play_round():
    number, correct_answer = generate_round()
    print(f"Question: {number}")
    answer = prompt.string("Your answer: ")
    if answer == correct_answer:
        print('Correct!')
        return True
    print(
        f"'{answer}' is wrong answer ;(. "
        f"Correct answer was '{correct_answer}'."
    )
    return False


def play_game(name):
    for _ in range(ROUNDS_COUNT):
        if not play_round():
            print(f"Let's try again, {name}!")
            return
    print(f'Congratulations, {name}!')


def run():
    print('Welcome to the Brain Games!')
    name = prompt.string('May I have your name? ')
    print(f'Hello, {name}!')
    print(DESCRIPTION)
    play_game(name)
