from random import randint

MIN_NUMBER = 1
MAX_NUMBER = 100
DESCRIPTION = 'Find the greatest common divisor of given numbers.'


def gcd(first_number, second_number):
    while second_number != 0:
        remainder = first_number % second_number
        first_number = second_number
        second_number = remainder
    return first_number


def generate_round():
    first_number = randint(MIN_NUMBER, MAX_NUMBER)
    second_number = randint(MIN_NUMBER, MAX_NUMBER)
    answer = str(gcd(first_number, second_number))
    question = f'{first_number} {second_number}'
    return question, answer