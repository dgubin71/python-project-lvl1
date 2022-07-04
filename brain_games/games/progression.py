from random import randrange


greeting_on = True       # greeting is "ON" only for first round


def get_next_question_right_answer():
    global greeting_on
    if greeting_on is True:
        print('What number is missing in the progression?')
        greeting_on = False
    number1 = randrange(5)
    number2 = randrange(20)
    double_dot_pos = randrange(1, 11)
    question = ''
    for i in range(1, 11):
        if i == double_dot_pos:
            right_answer = str((i + number1) * number2)
            next_item = '..'
        else:
            next_item = str((i + number1) * number2)
        question = f'{question} {next_item}'
    return question.strip(), right_answer
