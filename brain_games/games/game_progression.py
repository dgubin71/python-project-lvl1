#!/usr/bin/env python3
from random import randrange
from brain_games.input_output import welcome_user
from brain_games.input_output import start_the_match


def progression():
    name = welcome_user('What number is missing in the progression?')
    if start_the_match(ask_progression, name):
        print(f'Congratulations, {name}!')


def ask_progression():
    number1 = randrange(5)
    number2 = randrange(20)
    double_dot_pos = randrange(1, 11)
    question = ''
    for i in range(1, 11):
        if i == double_dot_pos:
            true_answer = str((i + number1) * number2)
            next_item = '..'
        else:
            next_item = str((i + number1) * number2)
        question = f'{question} {next_item}'
    return question, true_answer
