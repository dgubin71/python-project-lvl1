import prompt

NUMBER_OF_ROUNDS = ['1st', '2nd', '3rd']   # Maximum number of rounds


def play(game_module):
    game_on = True
    name = prompt.string('May I have your name? ')
    print(f'Hello, {name}!')
    for attempt in NUMBER_OF_ROUNDS:
        (question, true_answer) = game_module.get_next_question(attempt)
        print(f'Question: {question}')
        answer = prompt.string('Your answer: ')
        if answer == true_answer:
            print('Correct !')
        else:
            print(f"'{answer}' is wrong answer ;(."
                  f" Correct answer was  '{true_answer}'.")
            print(f"Let's try again, {name}!")
            game_on = False
            break
    if game_on:
        print(f'Congratulations, {name}!')
