from random import randrange
from brain_games.brain_engin import welcome_to_play


def progression():
    greeting = 'What number is missing in the progression?'
    game_module_name = 'brain_games.games.progression'
    welcome_to_play(greeting, game_module_name)


def ask_next_question():
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
