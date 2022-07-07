from random import randrange

DESCRIPTION = 'What number is missing in the progression?'


def get_next_question_right_answer():
    lenght_progression = randrange(5, 10)
    start_progression = randrange(1, 20)
    step_progression = randrange(1, 50)
    end_progression = start_progression + lenght_progression * step_progression
    random_index = randrange(0, lenght_progression - 1)
    progression = []
    for i in range(start_progression, end_progression, step_progression):
        progression.append(str(i))
    right_answer = progression[random_index]
    progression[random_index] = '..'
    question = ' '.join(progression)
    return question, right_answer
