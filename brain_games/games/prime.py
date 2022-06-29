from random import randrange
from brain_games.brain_engin import welcome_to_play


def prime_number():
    greeting = 'Answer "yes" if given number is prime. Otherwise answer "no".'
    game_module_name = 'brain_games.games.prime'
    welcome_to_play(greeting, game_module_name)


def ask_next_question():
    question = randrange(31)
    true_answer = 'yes' if is_prime(question) else 'no'
    return str(question), true_answer


def is_prime(n):
    if n == 0 or n == 1:
        return False
    d = 2
    while d * d <= n and n % d != 0:
        d += 1
    return d * d > n
