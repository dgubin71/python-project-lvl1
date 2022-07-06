from random import randrange
from math import gcd

GAME_DISCRIPTION = 'Find the greatest common divisor of given numbers.'


def get_next_question_right_answer():
    number1 = randrange(20)
    number2 = randrange(20)
    right_answer = gcd(number1, number2)
    question = f'{number1} {number2}'
    return question, str(right_answer)
