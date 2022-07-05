import prompt

NUMBER_OF_ROUNDS = 3  # Maximum number of rounds
GREETING_CALC = 'What is the result of the expression?'
GREETING_EVEN = 'Answer "yes" if the number is even, otherwise answer "no".'
GREETING_PRIME = 'Answer "yes" if given number is prime. Otherwise answer "no".'
GREETING_GCD = 'Find the greatest common divisor of given numbers.'
GREETING_PROGRESSION = 'What number is missing in the progression?'


def play(game):
    name = prompt.string('May I have your name? ')
    print(f'Hello, {name}!')
    match game.__name__:
        case 'brain_games.games.calc':
            print(GREETING_CALC)
        case 'brain_games.games.even':
            print(GREETING_EVEN)
        case 'brain_games.games.gcd':
            print(GREETING_GCD)
        case 'brain_games.games.prime':
            print(GREETING_PRIME)
        case 'brain_games.games.progression':
            print(GREETING_PROGRESSION)
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
