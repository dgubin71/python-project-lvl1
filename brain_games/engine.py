import prompt

NUMBER_OF_ROUNDS = 3  # Maximum number of rounds


def play(game):
    name = prompt.string('May I have your name? ')
    print(f'Hello, {name}!')
    print(game.GAME_DISCRIPTION)
    for _ in range(NUMBER_OF_ROUNDS):
        (question, right_answer) = game.get_next_question_right_answer()
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
