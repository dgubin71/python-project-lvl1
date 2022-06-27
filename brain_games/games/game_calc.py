from random import randrange
from brain_games.input_output import welcome_user
from brain_games.input_output import start_the_match


def calculator():
    name = welcome_user('What is the result of the expression?')
    if start_the_match(ask_calc, name):
        print(f'Congratulations, {name}!')


def ask_calc():
    operation_list = ["+", '-', '*']
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
    return question, true_answer
