from random import randrange
from brain_games.brain_engin import welcome_to_play


def calculator():
    greeting = 'What is the result of the expression?'
    game_module_name = 'brain_games.games.calc'
    welcome_to_play(greeting, game_module_name)


def ask_next_question():
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
    return question, str(true_answer)
