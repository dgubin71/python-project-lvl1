from random import randrange
from math import sqrt


DESCRIPTION = 'Answer "yes" if given number is prime. \
Otherwise answer "no".'


def get_next_question_right_answer():
    question = randrange(1, 33)
    right_answer = 'yes' if is_prime(question) else 'no'
    return question, right_answer


def is_prime(number):
    if number < 2:
        return False
    for d in range(2, int(sqrt(number) + 1)):
        if number % d == 0:
            return False
    return True
