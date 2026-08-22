from random import randint

MIN_NUMBER = 1
MAX_NUMBER = 100
MIN_STEP = 1
MAX_STEP = 10
DESCRIPTION = 'What number is missing in the progression?'
PROGRESSION_LENGTH = 10


def make_progression(start, step, length):
    numbers = []
    for i in range(length):
        item = start + i * step
        numbers.append(item)
    return numbers


def hide_number(numbers, hidden_index):
    correct_answer = str(numbers[hidden_index])
    numbers[hidden_index] = '..'
    text_elements = []

    for item in numbers:
        string_item = str(item)
        text_elements.append(string_item)
    question = " ".join(text_elements)
    return question, correct_answer


def generate_round():
    start = randint(MIN_NUMBER, MAX_NUMBER)
    step = randint(MIN_STEP, MAX_STEP)
    numbers = make_progression(start, step, PROGRESSION_LENGTH)
    hidden_index = randint(0, PROGRESSION_LENGTH - 1)
    return hide_number(numbers, hidden_index)
    