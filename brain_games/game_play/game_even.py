#!/usr/bin/env python3
import prompt
from random import randrange


def even_not_even():
    name = prompt.string('May I have your name? ')
    print(f'Hello, {name}!')
    print('Answer "yes" if the number is even, otherwise answer "no".')

    answer_ok = 0               # counter correct answer
    while answer_ok != 3:
        number = randrange(100)
        true_answer = 'yes' if number % 2 == 0 else 'no'
        print(f'Question: {number}')
        answer = prompt.string('Your answer: ')
        if answer == true_answer:
            answer_ok += 1
            print('Correct !')
        else:
            print(f"'{answer}' is wrong answer ;(."
                  f" Correct answer was  '{true_answer}'.")
            print(f"Let's try again, {name}!")
            break
    else:
        print(f'Congratulations, {name}!')
