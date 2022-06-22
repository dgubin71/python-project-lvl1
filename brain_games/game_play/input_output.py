#!/usr/bin/env python3
import prompt


def welcome_user():
    name = prompt.string('May I have your name? ')
    print(f'Hello, {name}!')
    return name


def chek_answer(question, true_answer, name):
    print(f'Question: {question}')
    answer = prompt.string('Your answer: ')
    if answer == true_answer:
        print('Correct !')
        return True
    else:
        print(f"'{answer}' is wrong answer ;(."
              f" Correct answer was  '{true_answer}'.")
        print(f"Let's try again, {name}!")
        return False
