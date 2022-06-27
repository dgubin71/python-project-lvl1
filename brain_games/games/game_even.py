#!/usr/bin/env python3
from random import randrange
from brain_games.input_output import welcome_user
from brain_games.input_output import chek_answer
from brain_games.input_output import ask_question
from brain_games.input_output import start_the_match


def even_not_even():
    name = welcome_user('Answer "yes" if the number is even, otherwise answer "no".')
    if start_the_match(ask_even,name):
        print(f'Congratulations, {name}!')

def ask_even():        
    question = randrange(100)
    true_answer = 'yes' if question % 2 == 0 else 'no'
    return str(question), true_answer
