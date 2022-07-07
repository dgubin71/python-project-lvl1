import random


DESCRIPTION = 'What is the result of the expression?'


def get_next_question_right_answer():
    number1 = random.randrange(20)
    number2 = random.randrange(20)
    operation = random.choice(("+", '-', '*'))
    if operation == '+':
        right_answer = number1 + number2
    elif operation == '-':
        right_answer = number1 - number2
    elif operation == '*':
        right_answer = number1 * number2
    question = f'{number1} {operation} {number2}'
    return question, str(right_answer)
