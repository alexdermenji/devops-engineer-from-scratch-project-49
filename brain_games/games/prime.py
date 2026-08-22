from random import randint

MIN_NUMBER = 0
MAX_NUMBER = 100
DESCRIPTION = 'Answer "yes" if given number is prime. Otherwise answer "no".'


def is_prime(number):
    if number < 2:
        return False

    divisor = 2
    while divisor * divisor <= number:
        if number % divisor == 0:
            return False
        divisor += 1

    return True


def get_correct_answer(number):
    if is_prime(number):
        return 'yes'
    return 'no'


def generate_round():
    number = randint(MIN_NUMBER, MAX_NUMBER)
    return number, get_correct_answer(number)
