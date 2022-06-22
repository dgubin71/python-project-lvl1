#!/usr/bin/env python3
from random import randrange
from brain_games.input_output import welcome_user
from brain_games.input_output import chek_answer


def calculator():
    name = welcome_user()
    print('What is the result of the expression?')
    answer_ok = 0
    operation_list = ["+", '-', '*']              # counter correct answer
    while answer_ok != 3:
        number1 = randrange(20)
        number2 = randrange(20)
        operation = operation_list[randrange(3)]
        if operation == '+':
            true_answer = number1 + number2
        elif operation == '-':
            true_answer = number1 - number2
        else:
            true_answer = number1 * number2
        question = f'{number1} {operation} {number2}'
        if chek_answer(question, str(true_answer), name):
            answer_ok += 1
        else:
            break
    else:
        print(f'Congratulations, {name}!')
