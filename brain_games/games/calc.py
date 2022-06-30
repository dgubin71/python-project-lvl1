from random import randrange


def get_next_question(attempt):
    if attempt == '1st':
        print('What is the result of the expression?')
    operation_list = ["+", '-', '*']
    number1 = randrange(20)
    number2 = randrange(20)
    operation = operation_list[randrange(3)]
    if operation == '+':
        true_answer = number1 + number2
    elif operation == '-':
        true_answer = number1 - number2
    else:
        true_answer = number1 * number2
    question = f'{number1} {operation} {number2}'
    return question, str(true_answer)
