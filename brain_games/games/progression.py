from random import randrange


def get_next_question(attempt):
    if attempt == '1st':
        print('What number is missing in the progression?')
    number1 = randrange(5)
    number2 = randrange(20)
    double_dot_pos = randrange(1, 11)
    question = ''
    for i in range(1, 11):
        if i == double_dot_pos:
            true_answer = str((i + number1) * number2)
            next_item = '..'
        else:
            next_item = str((i + number1) * number2)
        question = f'{question} {next_item}'
    return question.strip(), true_answer
