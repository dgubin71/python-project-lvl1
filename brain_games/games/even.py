from random import randrange


def get_next_question(attempt):
    if attempt == '1st':
        print('Answer "yes" if the number is even, otherwise answer "no".')
    question = randrange(100)
    true_answer = 'yes' if question % 2 == 0 else 'no'
    return str(question), true_answer
