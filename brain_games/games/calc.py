from random import randrange

greeting_on = True         # greeting is "ON" only for first round


def get_next_question_right_answer():
    global greeting_on
    if greeting_on is True:
        print('What is the result of the expression?')
        greeting_on = False
    operation_list = ["+", '-', '*']
    number1 = randrange(20)
    number2 = randrange(20)
    operation = operation_list[randrange(3)]
    if operation == '+':
        right_answer = number1 + number2
    elif operation == '-':
        right_answer = number1 - number2
    else:
        right_answer = number1 * number2
    question = f'{number1} {operation} {number2}'
    return question, str(right_answer)
