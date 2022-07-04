from random import randrange

greeting_on = True       # greeting is "ON" only for first round


def get_next_question_right_answer():
    global greeting_on
    if greeting_on is True:
        print('Answer "yes" if the number is even, otherwise answer "no".')
        greeting_on = False
    question = randrange(100)
    right_answer = 'yes' if question % 2 == 0 else 'no'
    return str(question), right_answer
