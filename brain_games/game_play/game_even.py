#!/usr/bin/env python3
from random import randrange
from brain_games.game_play.input_output import welcome_user
from brain_games.game_play.input_output import chek_answer


def even_not_even():
    name = welcome_user()
    print('Answer "yes" if the number is even, otherwise answer "no".')
    answer_ok = 0               # counter correct answer
    while answer_ok != 3:
        number = randrange(100)
        true_answer = 'yes' if number % 2 == 0 else 'no'
        if chek_answer(number, true_answer, name):
            answer_ok += 1
        else:
            break
    else:
        print(f'Congratulations, {name}!')
