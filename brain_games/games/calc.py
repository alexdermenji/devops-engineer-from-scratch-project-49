from random import choice, randint

MIN_NUMBER = 0
MAX_NUMBER = 100
OPERATORS = ('+', '-', '*')
DESCRIPTION = 'What is the result of the expression?'


def calculate(first_number, second_number, operator):
    match operator:
        case '+':
            return first_number + second_number
        case '-':
            return first_number - second_number
        case '*':
            return first_number * second_number


def generate_round():
    first_number = randint(MIN_NUMBER, MAX_NUMBER)
    second_number = randint(MIN_NUMBER, MAX_NUMBER)
    operator = choice(OPERATORS)
    question = f'{first_number} {operator} {second_number}'
    correct_answer = str(calculate(first_number, second_number, operator))
    return question, correct_answer
