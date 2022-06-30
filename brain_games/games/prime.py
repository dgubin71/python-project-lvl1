from random import randrange


def get_next_question(attempt):
    if attempt == '1st':
        print('Answer "yes" if given number is prime. Otherwise answer "no".')
    question = randrange(1, 33)
    true_answer = 'yes' if is_prime(question) else 'no'
    return str(question), true_answer


def is_prime(n):
    if n == 0 or n == 1:
        return False
    d = 2
    while d * d <= n and n % d != 0:
        d += 1
    return d * d > n
