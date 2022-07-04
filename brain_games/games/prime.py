from random import randrange


greeting_on = True   # greeting is "ON" only for first round


def get_next_question_right_answer():
    global greeting_on
    if greeting_on is True:
        print('Answer "yes" if given number is prime. Otherwise answer "no".')
        greeting_on = False
    question = randrange(1, 33)
    true_answer = 'yes' if is_prime(question) else 'no'
    return str(question), true_answer


def is_prime(n):
    if n == 0 or n == 1:
        return False
    d = 2
    for d in range(d, n):
        if d * d >= n and n % d == 0:
            return False
    else:
        return True
