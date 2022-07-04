from random import randrange
from math import gcd

greeting_on = True       # greeting is "ON" only for first round


def get_next_question_right_answer():
    global greeting_on
    if greeting_on is True:
        print('Find the greatest common divisor of given numbers.')
        greeting_on = False
    number1 = randrange(20)
    number2 = randrange(20)
    right_answer = gcd(number1, number2)
    question = f'{number1} {number2}'
    return question, str(right_answer)
