def calc_grade(final_grade,class_grade,final_weight):
    class_weight = 1-final_weight
    overall_grade= final_weight*final_grade+class_weight*class_grade
    return overall_grade
#final_grade = float(input("what is the grade you got on the final"))/100
grade_wanted= .90
class_grade= float(input("what is your grade, please enter as a percent"))/100
final_weight = float(input("what is the weight of the final , please enter as a percent"))/100
final_grade=0



#grade = calc_grade(final_grade,class_grade,final_weight)*100
#print(grade)
while calc_grade(final_grade,class_grade,final_weight)<grade_wanted:
    final_grade+=0.01
print(final_grade*100)