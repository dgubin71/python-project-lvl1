#!/usr/bin/env python3
from random import randrange
from math import gcd
from brain_games.input_output import welcome_user
from brain_games.input_output import chek_answer


def gcd_fun():
    name = welcome_user()
    print('Find the greatest common divisor of given numbers.')
    answer_ok = 0             # counter correct answer
    NUMBER_OF_ROUNDS = 3      # Maximum number of successful rounds
    while answer_ok != NUMBER_OF_ROUNDS:
        number1 = randrange(20)
        number2 = randrange(20)
        true_answer = gcd(number1, number2)
        question = f'{number1} {number2}'
        if chek_answer(question, str(true_answer), name):
            answer_ok += 1
        else:
            break
    else:
        print(f'Congratulations, {name}!')
