#!/usr/bin/env python3
from random import randrange
from brain_games.input_output import welcome_user
from brain_games.input_output import chek_answer


def prime_number():
    name = welcome_user()
    print('Answer "yes" if given number is prime. Otherwise answer "no".')
    answer_ok = 0               # counter correct answer
    NUMBER_OF_ROUNDS = 3        # Maximum number of successful rounds
    while answer_ok != NUMBER_OF_ROUNDS:
        number = randrange(31)
        true_answer = 'yes' if is_prime(number) else 'no'
        if chek_answer(number, true_answer, name):
            answer_ok += 1
        else:
            break
    else:
        print(f'Congratulations, {name}!')


def is_prime(n):
    if n == 0:
        return False
    d = 2
    while d * d <= n and n % d != 0:
        d += 1
    return d * d > n
