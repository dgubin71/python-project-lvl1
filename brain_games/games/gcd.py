from random import randrange
from math import gcd


def get_next_question(attempt):
    if attempt == '1st':
        print('Find the greatest common divisor of given numbers.')
    number1 = randrange(20)
    number2 = randrange(20)
    true_answer = gcd(number1, number2)
    question = f'{number1} {number2}'
    return question, str(true_answer)
