from random import randrange
from math import gcd
from brain_games.brain_engin import welcome_to_play


def gcd_fun():
    greeting = 'Find the greatest common divisor of given numbers.'
    game_module_name = 'brain_games.games.gcd'
    welcome_to_play(greeting, game_module_name)


def ask_next_question():
    number1 = randrange(20)
    number2 = randrange(20)
    true_answer = gcd(number1, number2)
    question = f'{number1} {number2}'
    return question, str(true_answer)
