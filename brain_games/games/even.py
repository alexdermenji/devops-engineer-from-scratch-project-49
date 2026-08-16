from random import randint

MIN_NUMBER = 0
MAX_NUMBER = 100
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
