# UNSOLVED

Students = {
    'Student1' : {
        'Subject 1' : {
            'T' : 89,
            'L' : 94,
            'A' : 75
        },
        'Subject 2' : {
            'T' : 99,
            'L' : 64,
            'A' : 85
        },
        'Subject 3' : {
            'T' : 90,
            'L' : 50,
            'A' : 65
        }
    },
    'Student2' : {
        'Subject 1' : {
            'T' : 79,
            'L' : 54,
            'A' : 70
        },
        'Subject 2' : {
            'T' : 55,
            'L' : 73,
            'A' : 71
        },
        'Subject 3' : {
            'T' : 51,
            'L' : 50,
            'A' : 69
        }
    },
    'Student3' : {
        'Subject 1' : {
            'T' : 99,
            'L' : 91,
            'A' : 90
        },
        'Subject 2' : {
            'T' : 99,
            'L' : 94,
            'A' : 95
        },
        'Subject 3' : {
            'T' : 90,
            'L' : 89,
            'A' : 85
        }
    }
}

for student in Students.keys():
    print(student)
    subject_scores_dict = Students[student]
    print(subject_scores_dict)
    subj_keys = subject_scores_dict.keys()
    theory_marks = []
    lab_marks = []
    asg_marks = []
    print(subj_keys)
    for subject in subj_keys:
        marks_dict = subj_keys[subject]
        for sub in marks_dict:  
            theory_marks.append(sub['T'])
            lab_marks.append(sub['L'])
            asg_marks.append(sub['A'])

    #  Score = 60% of T + 30% of L + 10% of A
    score = ((0.6*(sum(theory_marks)/300)) + (0.3*(sum(lab_marks)/300)) + (0.1*(sum(asg_marks)/300)))*100
    score = round(score, 2)
    print(f'Score of {student} = {score}')