#!/usr/bin/env python3
from random import randrange
from brain_games.input_output import welcome_user
from brain_games.input_output import chek_answer


def even_not_even():
    name = welcome_user()
    print('Answer "yes" if the number is even, otherwise answer "no".')
    answer_ok = 0               # counter correct answer
    NUMBER_OF_ROUNDS = 3        # Maximum number of successful rounds
    while answer_ok != NUMBER_OF_ROUNDS:
        number = randrange(100)
        true_answer = 'yes' if number % 2 == 0 else 'no'
        if chek_answer(number, true_answer, name):
            answer_ok += 1
        else:
            break
    else:
        print(f'Congratulations, {name}!')
