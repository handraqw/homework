'''
Задание 2
'''
def check_winners(scores, student_score):
    scores.sort()
    if student_score in scores[0] or scores[1] or scores[2]:
        return "Вы в тройке победителей!"
    return "Вы не попали в тройку победителей."