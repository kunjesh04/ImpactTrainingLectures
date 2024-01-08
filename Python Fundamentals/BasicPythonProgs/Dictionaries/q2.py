student_performance = {
    'Subject 1' : {
        'T' : 90,
        'L' : 95,
        'A' : 88
    },
    'Subject 2' : {
        'T' : 80,
        'L' : 95,
        'A' : 88
    },
    'Subject 3' : {
        'T' : 85,
        'L' : 90,
        'A' : 92
    }
}

score = 0
subj_keys = student_performance.keys()
theory_marks = []
lab_marks = []
asg_marks = []

for subject in subj_keys:
    marks_dict = student_performance[subject]
    theory_marks.append(marks_dict['T'])
    lab_marks.append(marks_dict['L'])
    asg_marks.append(marks_dict['A'])

#  Score = 60% of T + 30% of L + 10% of A
score = ((0.6*(sum(theory_marks)/300)) + (0.3*(sum(lab_marks)/300)) + (0.1*(sum(asg_marks)/300)))*100
score = round(score, 2)
print(score)