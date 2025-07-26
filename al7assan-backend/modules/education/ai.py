# modules/education/ai.py
def predict_final_grade(midterm, attendance):
    return midterm * 0.4 + (attendance * 100) * 0.6

def recommend_intervention(student_avg, attendance):
    if student_avg < 60 or attendance < 0.7:
        return "توصية: دعم أكاديمي فوري"
    return "الأداء مقبول"
