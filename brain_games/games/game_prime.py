from random import randrange
from brain_games.input_output import welcome_user
from brain_games.input_output import start_the_match


def prime_number():
    name = welcome_user('Answer "yes" if given number is prime.'
                        ' Otherwise answer "no".')
    if start_the_match(ask_prime, name):
        print(f'Congratulations, {name}!')


def ask_prime():
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
