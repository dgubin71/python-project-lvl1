#!/usr/bin/env python3
from random import randrange
from math import gcd
from brain_games.input_output import welcome_user
from brain_games.input_output import chek_answer
from brain_games.input_output import ask_question
from brain_games.input_output import start_the_match


def gcd_fun():
    name = welcome_user('Find the greatest common divisor of given numbers.')
    if start_the_match(ask_gcd, name):
        print(f'Congratulations, {name}!')
        
    
def ask_gcd():    
    number1 = randrange(20)
    number2 = randrange(20)
    true_answer = gcd(number1, number2)
    question = f'{number1} {number2}'
    return question, true_answer

