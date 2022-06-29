import prompt
import importlib

NUMBER_OF_ROUNDS = 3     # Maximum number of successful rounds


def welcome_to_play(greetings, game_module):
    name = prompt.string('May I have your name? ')
    print(f'Hello, {name}!')
    print(f'{greetings}')
    game_module = importlib.import_module(game_module)
    answer_ok = 0
    while answer_ok != NUMBER_OF_ROUNDS:
        (question, true_answer) = game_module.ask_next_question()
        print(f'Question: {question}')
        answer = prompt.string('Your answer: ')
        if answer == true_answer:
            print('Correct !')
            answer_ok += 1
        else:
            print(f"'{answer}' is wrong answer ;(."
                  f" Correct answer was  '{true_answer}'.")
            print(f"Let's try again, {name}!")
            break
    if answer_ok == NUMBER_OF_ROUNDS:
        print(f'Congratulations, {name}!')
