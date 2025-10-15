'''
Задание 2
'''
def check_winners(scores, student_score):
    scores.sort(reverse=True)
    if student_score in scores[:3]:
        return "Вы в тройке победителей!"
    return "Вы не попали в тройку победителей."
