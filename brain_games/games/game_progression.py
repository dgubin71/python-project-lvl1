#!/usr/bin/env python3
from random import randrange
from brain_games.input_output import welcome_user
from brain_games.input_output import chek_answer


def progression():
    name = welcome_user()
    print('What number is missing in the progression?')
    answer_ok = 0            # counter correct answer
    while answer_ok != 3:
        number1 = randrange(5)
        number2 = randrange(20)
        double_point_pos = randrange(1, 11)
        question = ''
        for i in range(1, 11):
            if i == double_point_pos:
                true_answer = str((i + number1) * number2)
                next_item = '..'
            else:
                next_item = str((i + number1) * number2)
            question = f'{question} {next_item}'

        if chek_answer(question, str(true_answer), name):
            answer_ok += 1
        else:
            break
    else:
        print(f'Congratulations, {name}!')
