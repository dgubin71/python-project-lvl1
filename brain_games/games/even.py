from random import randrange
from brain_games.brain_engin import welcome_to_play


def even_not_even():
    greeting = 'Answer "yes" if the number is even, otherwise answer "no".'
    game_module_name = 'brain_games.games.even'
    welcome_to_play(greeting, game_module_name)


def ask_next_question():
    question = randrange(100)
    true_answer = 'yes' if question % 2 == 0 else 'no'
    return str(question), true_answer
