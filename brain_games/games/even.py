from random import randrange

DESCRIPTION = 'Answer "yes" if the number is even, otherwise answer "no".'


def get_next_question_right_answer():
    question = randrange(100)
    right_answer = 'yes' if question % 2 == 0 else 'no'
    return str(question), right_answer
