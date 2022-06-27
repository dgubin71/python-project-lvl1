#!/usr/bin/env python3
import prompt


def welcome_user(greetings):
    name = prompt.string('May I have your name? ')
    print(f'Hello, {name}!')
    print(f'{greetings}')
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


def start_the_match(function, name):
    answer_ok = 0            # counter correct answer
    NUMBER_OF_ROUNDS = 3     # Maximum number of successful rounds
    while answer_ok != NUMBER_OF_ROUNDS:
        (question, true_answer) = ask_question(function)
        if chek_answer(question.strip(), str(true_answer), name):
            answer_ok += 1
        else:
            return False
    else:
        return True


def ask_question(function):
    return function()
