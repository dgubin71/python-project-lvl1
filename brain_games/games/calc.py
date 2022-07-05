from random import randrange


def get_next_question_right_answer():
    signs_of_operations = ["+", '-', '*']
    number1 = randrange(20)
    number2 = randrange(20)
    operation = signs_of_operations[randrange(3)]
    if operation == '+':
        right_answer = number1 + number2
    elif operation == '-':
        right_answer = number1 - number2
    elif operation == '*':
        right_answer = number1 * number2
    question = f'{number1} {operation} {number2}'
    return question, str(right_answer)
