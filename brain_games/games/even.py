from random import randrange


def get_next_question_right_answer():
    question = randrange(100)
    right_answer = 'yes' if question % 2 == 0 else 'no'
    return str(question), right_answer
