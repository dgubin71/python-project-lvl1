import prompt

NUMBER_OF_ROUNDS = 3  # Maximum number of rounds


def play(game_module):
    name = prompt.string('May I have your name? ')
    print(f'Hello, {name}!')
    for attempt in range(0, NUMBER_OF_ROUNDS):
        (question, right_answer) = game_module.get_next_question_right_answer()
        print(f'Question: {question}')
        answer = prompt.string('Your answer: ')
        if answer == right_answer:
            print('Correct !')
        else:
            print(f"'{answer}' is wrong answer ;(."
                  f" Correct answer was  '{right_answer}'.")
            print(f"Let's try again, {name}!")
            break
    else:
        print(f'Congratulations, {name}!')
